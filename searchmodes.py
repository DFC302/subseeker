#!/usr/bin/env python3

import requests
import re
import json
import concurrent.futures
import useragents
import platform
import subprocess
from resources import options
from termcolor import colored

def crtsh():
	# Display only if verbose mode is on
	if options().verbose:
		print(colored(f"\n\tCRT.SH", "yellow"))
		print(colored(f"\t======\n", "yellow"))

	# Replace * with url encode
	domain = options().domain.replace("*","%25")

	# Wildcards and dot notation needed
	# Example *.domain or *test*.domain
	url = f"https://crt.sh/?q={domain}&output=json"

	try:
		request = requests.get(url, headers={'User-Agent':useragents.useragent()})
		regex = r'[^%*].*'
		data = request.json()

		if data:
			for row in data:
				row = re.findall(regex, row["name_value"])[0]
				print(colored(row, "blue"))

				if options().out:
					with open(options().out, "a") as f:
						f.write(str(row + "\n"))

		elif not data:
			print(colored(f"\nNo data found for {options().domain}", \
				"yellow"))

	# JSON Decode Error
	except ValueError:
		if options().verbose:
			# Verbose override to help user understand zero results
			print(colored(f"\nJSON value error!\n", "red"))
			print(colored(f"This could mean no data was found or crt.sh failed\
				to return data.", "yellow"))
			print(colored(f"Parsing domains with a large number of subdomains\
				can sometimes crash results.", "yellow")) 
			print(colored(f"Try again for possibly a different result.\n", \
			"yellow"))
			pass
		else:
			pass

	# User cancels program
	except KeyboardInterrupt:
		print(colored(f"User cancelled search.", "yellow"))
		sys.exit(0)

def certspotter(headers=None):
	if options().verbose:
		print(colored(f"\n\tCERTSPOTTER", "yellow"))
		print(colored(f"\t===========\n", "yellow"))

	if options().domain.startswith("*."):
		domain = options().domain[2:]

	elif options().domain.startswith("*"):
		domain = options().domain[1:]

	else:
		domain = options().domain

	subs = []

	try:
		if options().api:
			with open("config.json", "r") as f:
				jfile = json.load(f)
				key = jfile["API_INFO"][0]["key"]
				#print(key)
				headers = {'Authorization': 'Bearer ' + key}

		url = f"https://api.certspotter.com/v1/issuances?domain={domain}&\
		include_subdomains=true&expand=dns_names&expand=cert"

		response = requests.get(url, headers=headers)

		data = response.json()

		if data:
			for row in data:
				row = row["dns_names"]

				subs.append(row)

				if options().out:
					with open(options().out, "a") as f:
						f.write(str(row + "\n"))
		elif not data:
			print(colored(f"\nNo data found for {options().domain}", \
				"yellow"))

	except TypeError:
		if options().verbose:
			print(colored(f"No data found for {domain}\n", "yellow"))
			pass
		else:
			pass

	except IndexError:
		if options().verbose:
			print(colored(f"Index error", "yellow"))
			pass
		else:
			pass

	except KeyError:
		if options().verbose:
			print(colored(f"Key Error!", "yellow"))
			pass
		else:
			pass

	# User cancels program
	except KeyboardInterrupt:
		print(colored(f"User cancelled search.", "yellow"))
		sys.exit(0)
			
	for s in subs:
		print(colored("\n".join(s), "blue"))

def certdb(key=False):
	if options().verbose:
		print(colored(f"\n\tCERTDB", "yellow"))
		print(colored(f"\t======\n", "yellow"))

	if options().domain.startswith("*."):
		domain = options().domain[2:]

	elif options().domain.startswith("*"):
		domain = options().domain[1:]

	else:
		domain = options().domain

	try:
		# Default false
		if options().api:
			with open("config.json", "r") as f:
				jfile = json.load(f)
				key = jfile["API_INFO"][1]["key"]
				#print(key)

		url = f"https://api.spyse.com/v1/subdomains?api_token={key} \
		&domain={domain}&page=1"

		request = requests.get(url)
		data = request.json()

		i = 0

		if data:
			for row in data:
				subdomain = data['records'][i]['domain']
				i += 1
				print(colored(subdomain, "blue"))

				if options().out:
					with open(options().out, "a") as f:
						f.write(subdomain + "\n")

		elif not data:
			print(colored(f"\nNo data found for {options().domain}", \
				"yellow"))

		print("\n")

	except KeyError:
		if options().verbose:
			print(colored(f"No data found for {domain}\n", "yellow"))
			pass
		else:
			pass

	except IndexError:
		if options().verbose:
			print(colored(f"Index error", "yellow"))
			pass
		else:
			pass

	except KeyError:
		if options().verbose:
			print(colored(f"Key Error!", "yellow"))
			pass
		else:
			pass

	# User cancels program
	except KeyboardInterrupt:
		print(colored(f"User cancelled search.", "yellow"))
		sys.exit(0)

def censys():
	if options().verbose:
		print(colored(f"\n\tCENSYS", "yellow"))
		print(colored(f"\t======\n", "yellow"))

	if options().domain.startswith("*."):
		domain = options().domain[2:]

	elif options().domain.startswith("*"):
		domain = options().domain[1:]

	else:
		domain = options().domain

	try:
		if options().api:
			with open("config.json", "r") as f:
				jfile = json.load(f)
				key = jfile["API_INFO"][2]["id"]
				#print(key)
				secret = jfile["API_INFO"][2]["secret"]
				#print(secret)

			api_url = "https://censys.io/api/v1/search/certificates"

			regex = r'(?:CN=).+'
			params = {"query":f"{domain}", "page":1}

			response = requests.post(api_url, json=params, auth=(key, secret))
			data = response.json()

			if data:
				for row in data["results"]:
					CN = row["parsed.subject_dn"].splitlines()

					for line in CN:
						line = re.findall(regex, line)[0][3:]
						print(colored(line, "blue"))

					if options().out:
						with open(options().out, "a") as f:
							f.write(line + "\n")

			elif not data:
				print(colored(f"\nNo data found for {options().domain}", \
					"yellow"))

	except KeyError:
		if options().verbose:
			print(colored(f"No data found for {domain}\n", "yellow"))
			pass
		else:
			pass

	except IndexError:
		if options().verbose:
			print(colored(f"Index error", "yellow"))
			pass
		else:
			pass

	except KeyError:
		if options().verbose:
			print(colored(f"Key Error!", "yellow"))
			pass
		else:
			pass

	# User cancels program
	except KeyboardInterrupt:
		print(colored(f"User cancelled search.", "yellow"))
		sys.exit(0)

# sub keyord search mode
# Multi-search mode
# Open file to read sub keywords, start threads
def generate_sub_keywords():
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
		threads = 10

	with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
		executor.map(multi, domains)

# Parse crt.sh for each sub domain keyword
def multi(sub):
	# Make sure each subdomain returned, is unique
	subset=set()
	# Log how many successful searches and record successful subs
	ssubs = []
	# Log how many searches returned zero results and subs with no results
	nosubs = []
	# Log failed searches and failed subs
	fsubs = []

	domain = options().domain

	try:
		url = f"https://crt.sh/?q=%25{sub}%25.{domain}&output=json"
		request = requests.get(url, headers={'User-Agent':useragents.useragent()})
		regex = r'[^%*].*'
		data = request.json()

		if data:
			for row in data:
				row = re.findall(regex, row["name_value"])[0]

				subset.add(row)

			if options().verbose:
				print(colored(f"Data found for: {sub}", "green"))
				print(colored("\n".join(subset), "blue"))
			else:
				print(colored("\n".join(subset), "blue"))

		elif not data:
			if options().verbose:
				print(colored(f"No data found for: {sub}", "yellow"))

	# JSON Decode Error
	except ValueError:
		if options().verbose:
			print(colored(f"JSON value error for: {sub}", "red"))
		pass

	# User cancels program
	except KeyboardInterrupt:
		print(colored(f"User cancelled search.", "red"))
		sys.exit(0)

	if options().out:
		with open(options().out, "a") as f:
			f.write("\n")
			f.write("\n".join(subset))

# Create sub domain keywords to search from
def create():
	if options().domain.startswith("*."):
		domain = options().domain[2:]

	elif options().domain.startswith("*"):
		domain = options().domain[1:]

	else:
		domain = options().domain

	# Specify regex to be used
	# Regex should grab every sub domain after domain
	regex = f"\w*\.(?={domain})"

	# Create a set to remove duplicates
	subset=set()

	with open(options().file, "r") as f:
		try:
			for domains in f:
				# Remove new line character
				domains = domains.strip("\n")
				domains = re.findall(regex, domains)[0]
				# Remove "." after sub domain output
				subset.add(domains.strip("."))

		# If there is an index error, pass and keep parsing
		except IndexError:
			pass

	# If write to outfile is specified
	if options().out:
		with open(options().out, "a") as wf:
			wf.write("\n".join(subset))
		print(colored(f"\nYour output has been written too {options().out}", \
			"yellow"))
		
		if platform.system() == "Linux" or platform.system() == "Darwin":
			stdoutdata = subprocess.getoutput(f"wc -l {options().out}")
			print(colored(f"Your results have returned {stdoutdata} unique subdomains\n", "yellow"))

	elif not options().out:
		print("\n".join(subset))
