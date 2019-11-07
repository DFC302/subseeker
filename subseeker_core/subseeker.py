#!/usr/bin/env python3

from subseeker_core.options import options
from subseeker_core.searchmodes import SubSeeker
from subseeker_core.configurations import Process
from subseeker_core.create import GenerateKeywords
from colorama import Fore, Style
import sys
import re
import json

def main():
	GREEN = Fore.GREEN
	CYAN = Fore.CYAN
	MAG = Fore.MAGENTA
	RED = Fore.RED
	YELLOW = Fore.YELLOW
	BLUE = Fore.BLUE
	RESET = Style.RESET_ALL

	if options().version:
		Process().version()
		sys.exit(0)

	elif options().generate:
		if not options().domain:
			print(f"\n{RED}Error: Need domain to parse against!{RESET}\n")
			sys.exit(1)

		elif not options().file:
			print(f"\n{RED}Error: Need file to generate keywords from!{RESET}\n")
			sys.exit(1)

		elif options().file and options().domain:
			GenerateKeywords().create()
			sys.exit(0)

	elif options().file or options().keywords and not options().singlesearch:
		if not options().domain:
			print(f"\n{RED}Error: Missing domain.{RESET}\n")
			sys.exit(1)

		try:
			Process().title()
			Process().process()
			SubSeeker().thread_execution()
			SubSeeker().certspotter()
			SubSeeker().certdb()
			SubSeeker().threatcrowd()
			SubSeeker().censys()
			SubSeeker().virustotal()
			SubSeeker().securitytrails()
			SubSeeker().print_domains()
			sys.exit(0)

		except KeyboardInterrupt:
			sys.exit(0)

	elif options().singlesearch:
		if options().singlesearch.lower() == "options":
			print("\tcrtsh\t\tSearch crtsh database.")
			print("\tmcrtsh\t\tSearch crtsh database using keywords.")
			print("\tcertspotter\tSearch certspotter database.")
			print("\tcertdb\t\tSearch certdb database.")
			print("\tcensys\t\tSearch censys database.")
			print("\tvirustotal\tSearch virustotal database.")
			print("\tthreatcrowd\tSearch threatcrowd database.")
			print("\tsecuritytrails\tSearch securitytrails database.")
		
		if not options().domain and not options().singlesearch == "options":
			print(f"\n{RED}Error: Missing domain.{RESET}\n")
			sys.exit(1)

		if options().singlesearch.lower() == "crtsh":
			Process().title()
			print(f"{MAG}[~]{CYAN} Checking Crtsh...{RESET}")
			SubSeeker().crtsh()
			SubSeeker().print_domains()
			sys.exit(0)

		elif options().singlesearch.lower() == "certspotter":
			Process().title()
			print(f"{MAG}[~]{CYAN} Checking Certspotter...{RESET}")
			SubSeeker().certspotter()
			SubSeeker().print_domains()
			sys.exit(0)

		elif options().singlesearch.lower() == "certdb":
			Process().title()
			print(f"{MAG}[~]{CYAN} Checking CertDB...{RESET}")
			SubSeeker().certdb()
			SubSeeker().print_domains()
			sys.exit(0)

		elif options().singlesearch.lower() == "threatcrowd":
			Process().title()
			print(f"{MAG}[~]{CYAN} Checking threatcrowd...{RESET}")
			SubSeeker().threatcrowd()
			SubSeeker().print_domains()
			sys.exit(0)

		elif options().singlesearch.lower() == "censys":
			Process().title()
			print(f"{MAG}[~]{CYAN} Checking Censys...{RESET}")
			SubSeeker().censys()
			SubSeeker().print_domains()
			sys.exit(0)

		elif options().singlesearch.lower() == "virustotal":
			Process().title()
			print(f"{MAG}[~]{CYAN} Checking VirusTotal...{RESET}")
			SubSeeker().virustotal()
			SubSeeker().print_domains()
			sys.exit(0)

		elif options().singlesearch.lower() == "securitytrails":
			Process().title()
			print(f"{MAG}[~]{CYAN} Checking SecurityTrails...{RESET}")
			SubSeeker().securitytrails()
			SubSeeker().print_domains()
			sys.exit(0)

		elif options().singlesearch.lower() == "mcrtsh":
			if options().file or options().keywords and options().domain:
				Process().title()
				print(f"{MAG}[~]{CYAN} Checking Crtsh...{RESET}")
				SubSeeker().thread_execution()
				SubSeeker().print_domains()
				sys.exit(0)

			elif not options().file or not options().keywords:
				print(f"\n{RED}Error! Need --file with list of keywords or at least one --keyword.\n")
				sys.exit(1)

	else:
		if not options().domain:
			print(f"\n{RED}Error: Missing domain.{RESET}\n")
			sys.exit(1)

		try:
			Process().title()
			Process().process()
			SubSeeker().crtsh()
			SubSeeker().certspotter()
			SubSeeker().certdb()
			SubSeeker().threatcrowd()
			SubSeeker().censys()
			SubSeeker().virustotal()
			SubSeeker().securitytrails()
			SubSeeker().print_domains()
			sys.exit(0)

		except KeyboardInterrupt:
			sys.exit(0)


if __name__ == "__main__":
	main()
