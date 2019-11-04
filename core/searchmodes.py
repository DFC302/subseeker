import requests
import re
import json
import os
import concurrent.futures
import core.useragents
import platform
import subprocess
from core.options import options
from colorama import Fore, Style

class SubSeeker():
	if options().domain:
		# domain_regex = r"([^\.]*.(?=com).+)"
		domain_regex = r"[a-zA-Z0-9].*"
		domain = re.findall(domain_regex, options().domain)[0]

	# if user uses api, search for config file, that way no matter what directory user is in,
	# subseeker can find config file.
	if options().api:
		for root, dirs, files in os.walk("/"):
			filename = "subseeker_config.json"
			if filename in files:
				config_file = os.path.join(root, filename)
				#print(config_file)

	GREEN = Fore.GREEN
	RED = Fore.RED
	YELLOW = Fore.YELLOW
	BLUE = Fore.BLUE
	WHITE = Fore.WHITE
	RESET = Style.RESET_ALL

	domains = set()

	# Default value for API key is false, if user does not have one.
	def __init__(self, apikey=False, params=None, page=1):
		self.apikey = apikey
		self.params = params
		self.page = page
		self.threads = 20

	def crtsh(self):
		org_domain = options().domain.replace("*", "%25")
		url = f"https://crt.sh/?q={org_domain}&output=json"

		try:
			response = requests.get(url, headers={'User-Agent':core.useragents.useragent()})
			regex = r'[^%*].*'
			data = response.json()

			if data:
				for row in data:
					row = re.findall(regex, row["name_value"])[0]
					self.domains.add(row)

			elif not data:
				print(f"{self.RED}[x] No data found for {options().domain} using {self.WHITE}crtsh.{self.RESET}")

		except ValueError:
			pass

	def certspotter(self):
		try:
			if options().api:
				with open(self.config_file, "r") as f:
					jfile = json.load(f)
					self.apikey = jfile["API_INFO"][0]["key"]
					params = {'Authorization': 'Bearer ' + self.apikey}

			url = f"https://api.certspotter.com/v1/issuances?domain={self.domain}&include_subdomains=true&expand=dns_names&expand=cert"
			response = requests.get(url, params=self.params, headers={'User-Agent':core.useragents.useragent()})
			data = response.json()

			if data:
				for row in data:
					row = row["dns_names"]

					for domain in row:
						self.domains.add(row)

			elif not data:
				print(f"{self.RED}[x] No data found for {options().domain} using {self.WHITE}certspotter.{self.RESET}")

		except TypeError as e:
			pass

		except IndexError:
			pass

		except KeyError:
			pass

	def certdb(self):
		if options().page:
			page = options().page

		else:
			page = self.page

		try:
			# Default false
			if options().api:
				with open(self.config_file, "r") as f:
					jfile = json.load(f)
					self.apikey = jfile["API_INFO"][1]["key"]

			url = f"https://api.spyse.com/v1/subdomains?api_token={self.apikey} \
			&domain={self.domain}&page={page}"

			response = requests.get(url, headers={'User-Agent':core.useragents.useragent()})
			data = response.json()

			i = 0

			if data:
				for row in data:
					subdomains = data['records'][i]['domain']
					i += 1
					self.domains.add(subdomains)

			elif not data:
				print(f"{self.RED}[x] No data found for {options().domain} using {self.WHITE}certdb. {self.YELLOW}Page: {page}{self.RESET}")

		except KeyError:
			pass

		except IndexError:
			pass

	def censys(self):
		if options().page:
			page = options().page

		else:
			page = self.page

		try:
			if options().api:
				with open(self.config_file, "r") as f:
					jfile = json.load(f)
					self.apikey = jfile["API_INFO"][2]["id"]
					secret = jfile["API_INFO"][2]["secret"]

				api_url = "https://censys.io/api/v1/search/certificates"

				regex = r'(?:CN=).+'
				params = {"query":f"{self.domain}", "page":page}

				response = requests.post(api_url, json=params, auth=(self.apikey, secret), headers={'User-Agent':core.useragents.useragent()})
				data = response.json()

				if data:
					for row in data["results"]:
						CN = row["parsed.subject_dn"].splitlines()

						for line in CN:
							line = re.findall(regex, line)[0][3:]
							self.domains.add(line)

				elif not data:
					print(f"{self.RED}[x] No data found for {options().domain} using {self.WHITE}censys. {self.YELLOW}Page: {page}{self.RESET}")

			elif not options().api:
				#print(f"{self.YELLOW}[!] API credentials not found!{self.WHITE} Censys{self.RESET}")
				pass

		except IndexError:
			pass

		except KeyError:
			pass

	def virustotal(self):
		try:
			if options().api:
				with open(self.config_file, "r") as f:
					jfile = json.load(f)
					self.apikey = jfile["API_INFO"][3]["key"]

				api_url = "https://www.virustotal.com/vtapi/v2/domain/report"
				params = {"apikey":f"{self.apikey}", "domain":f"{self.domain}"}

				response = requests.get(api_url, params=params, headers={'User-Agent':core.useragents.useragent()})

				data = response.json()

				if data:
					subdomains = "\n".join(data["subdomains"])
					self.domains.add(subdomains)

				elif not data:
					print(f"{self.RED}[x] No data found for {options().domain} using {self.WHITE}virustotal.{self.RESET}")

			elif not options().api:
				#print(f"{self.YELLOW}[!] API credentials not found!{self.WHITE} VirusTotal{self.RESET}")
				pass

		except KeyError:
			pass

		except IndexError:
			pass

	def threatcrowd(self):
		try:
			api_url = "http://www.threatcrowd.org/searchApi/v2/domain/report/"
			params = {"domain":f"{self.domain}"}

			response = requests.get(api_url, params=params, headers={'User-Agent':core.useragents.useragent()})

			data = json.loads(response.text)
			data = data["subdomains"]

			if data:
				for row in data:
					self.domains.add(row)

			elif not data:
				print(f"{self.RED}[x] No data found for {options().domain} using {self.WHITE}threatcrowd.{self.RESET}")

		except KeyError:
			pass

		except IndexError:
			pass


	def thread_execution(self):
		domains = []

		if options().file:
			with open(options().file, "r") as f:
				for sub in f:

					if sub == "":
						pass
					else:
						sub = str(sub.strip("\n"))
						domains.append(sub)

		elif options().keywords:
			for sub in options().keywords:
				domains.append(sub)

		if options().threads:
			threads = options().threads
		else:
			threads = self.threads

		with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
			executor.map(self.multi_keyword_search, domains)

	# Parse crt.sh for each sub domain keyword
	def multi_keyword_search(self, sub):
		try:
			url = f"https://crt.sh/?q=%25{sub}%25.{self.domain}&output=json"
			response = requests.get(url, headers={'User-Agent':core.useragents.useragent()})
			regex = r'[^%*].*'
			data = response.json()

			if data:
				for row in data:
					row = re.findall(regex, row["name_value"])[0]
					self.domains.add(row)

			elif not data:
				print(f"{self.RED}[x] No data found:{self.WHITE} {sub}{self.RESET}")

		# JSON Decode Error
		except ValueError:
			print(f"{self.YELLOW}[!]{self.RED} JSON value error:{self.WHITE} {sub}{self.RESET}")
			pass

	def print_domains(self):
		subdomains = "\n".join(self.domains)
		print(f"{self.BLUE}{subdomains}{self.RESET}")

		if options().out:
			with open(options().out, "a") as f:
				f.write(str(subdomains))
				f.write("\n")