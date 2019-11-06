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
	RED = Fore.RED
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

		elif options().file and options().domain:
			GenerateKeywords().create()

	elif options().file or options().keywords:
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

		except KeyboardInterrupt:
			sys.exit(0)

	elif options().singlesearch:
		if not options().domain:
			print(f"\n{RED}Error: Missing domain.{RESET}\n")
			sys.exit(1)

		if options().singlesearch.lower() == "crtsh":
			Process().title()
			Process().process()
			SubSeeker().crtsh()
			SubSeeker().print_domains()

		elif options().singlesearch.lower() == "certspotter":
			Process().title()
			Process().process()
			SubSeeker().certspotter()
			SubSeeker().print_domains()

		elif options().singlesearch.lower() == "certdb":
			Process().title()
			Process().process()
			SubSeeker().certdb()
			SubSeeker().print_domains()

		elif options().singlesearch.lower() == "threatcrowd":
			Process().title()
			Process().process()
			SubSeeker().threatcrowd()
			SubSeeker().print_domains()

		elif options().singlesearch.lower() == "censys":
			Process().title()
			Process().process()
			SubSeeker().censys()
			SubSeeker().print_domains()

		elif options().singlesearch.lower() == "virustotal":
			Process().title()
			Process().process()
			SubSeeker().virustotal()
			SubSeeker().print_domains()

		elif options().singlesearch.lower() == "securitytrails":
			Process().title()
			Process().process()
			SubSeeker().securitytrails()
			SubSeeker().print_domains()

		# elif options().singlesearch == None or options().singlesearch == " " or options().singlesearch == "":
		# 	print("\nsinglesearch usage: subseeker --domain [domain] --singlesearch [option]")
		# 	print("Options:\n\tcrtsh\n\tcertspotter\n\tcertdb\n\tthreatcrowd\n\tcensys\n\tvirustotal\n\tsecuritytrails\n")

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

		except KeyboardInterrupt:
			sys.exit(0)


if __name__ == "__main__":
	main()
