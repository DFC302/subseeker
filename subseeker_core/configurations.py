#!/usr/bin/env python3

from colorama import Fore, Style
from subseeker_core.options import options
import os
import re

class Process():
	GREEN = Fore.GREEN
	CYAN = Fore.CYAN
	MAG = Fore.MAGENTA
	RED = Fore.RED
	YELLOW = Fore.YELLOW
	BLUE = Fore.BLUE
	RESET = Style.RESET_ALL


	def process(self):
		print(f"{self.MAG}[~]{self.CYAN} Checking Crtsh...{self.RESET}")
		print(f"{self.MAG}[~]{self.CYAN} Checking Certspotter...{self.RESET}")
		print(f"{self.MAG}[~]{self.CYAN} Checking CertDB...{self.RESET}")
		print(f"{self.MAG}[~]{self.CYAN} Checking Censys...{self.RESET}")
		print(f"{self.MAG}[~]{self.CYAN} Checking VirusTotal...{self.RESET}")
		print(f"{self.MAG}[~]{self.CYAN} Checking ThreatCrowd...{self.RESET}")
		print("\n")

	def title(self):
		if options().domain:
			domain_regex = r"[a-zA-Z0-9].*"
			domain = re.findall(domain_regex, options().domain)[0]

		print(f"{self.RED}\t\tSUBSEEKER{self.RESET}")
		print(f"{self.RED}\t========================={self.RESET}")
		print(f"{self.BLUE}\t  DOMAIN:{self.RESET} {domain}")

		# Display choosen header, if not chosen, display default
		if options().useragent:
			print(f"{self.BLUE}\t  User-Agent:{self.RESET} {options().useragent}")
		elif not options().useragent:
			print(f"{self.BLUE}\t  User-Agent:{self.RESET} Firefox")

		# If user uses a file or keywords option, count number of subdomain keywords being used
		if options().file:
			print(f"{self.BLUE}\t  File:{self.RESET} {options().file}")
			count_lines = sum(1 for line in open(options().file))
			print(f"{self.BLUE}\t  Keywords:{self.RESET} {count_lines}")

		elif options().keywords:
			print(f"{self.BLUE}\t  Keywords:{self.RESET} {len(options().keywords)}")

		if options().threads:
			print(f"{self.BLUE}\t  Threads:{self.RESET} {options().threads}")
		elif not options().threads:
			print(f"{self.BLUE}\t  Threads:{self.RESET} 20")

		print("\n")

	def version(self):
		if options().version:
			print(f"{self.YELLOW}\t Title:{self.RESET}   Subseeker")
			print(f"{self.YELLOW}\t Version:{self.RESET} 2.2.2")
			print(f"{self.YELLOW}\t Author:{self.RESET}  Matthew Greer")
			print(f"{self.YELLOW}\t Twitter:{self.RESET} https://twitter.com/Vail__")
			print(f"{self.YELLOW}\t Github:{self.RESET}  https://github.com/DFC302")

	def path_to_config():
		name = "subseeker_config.json"
		path = "/"
		for root, dirs, files in os.walk(path):
			if name in files:
				filename = os.path.join(root, name)
				return filename
