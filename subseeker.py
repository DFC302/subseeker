#!/usr/bin/env python3

import sys
import re
import requests
import argparse
import platform
import concurrent.futures
import subprocess
from termcolor import colored
from datetime import datetime

# User options
def options():
	parser = argparse.ArgumentParser()

	# specify domain
	parser.add_argument(
		"-d", "--domain",
		help="Specify domain to search.",
		action="store",
	)

	# search domain using subdomain keywords from file
	parser.add_argument(
		"-f", "--file",
		help="Specify in file.",
		action="store",
	)

	# Write to output file
	parser.add_argument(
		"-o", "--out",
		help="Specify file to write results too.",
		action="store",
	)

	# Try with different headers, firefox, chrome, opera
	parser.add_argument(
		"-H", "--header",
		help="Specify header to use.",
		action="store"
	)

	# Turn on verbose mode.
	parser.add_argument(
		"-v", "--verbose",
		help="Turn on verbose mode.",
		action="store_true",
	)

	# Parse subdomain keywords from other tools output files
	parser.add_argument(
		"-S", "--searchsubs",
		help="Use regex to grab subdomains from domain.",
		action="store_true",
	)

	# User specify number of threads
	parser.add_argument(
		"-t", "--threads",
		help="Number of threads.",
		action="store",
		type=int,
	)

	# if not arguments are given, print usage message
	if len(sys.argv[1:]) == 0:
		parser.print_help()
		parser.exit()

	args = parser.parse_args()

	return args

def header():
	# Chrome header
	if options().header == "chrome".lower():
		ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
	
	# Firefox header, default
	elif options().header == "firefox".lower():
		ua = "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1"

	# Opera header
	elif options().header == "opera".lower():
		ua = "Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18"

	# If no header specifed, use set firefox
	elif not options().header:
		ua = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"

	return ua

# Display a title at each run
def title():
	print(colored(f"\n\t\t\tCollecting Information Now...", "cyan"))
	print(colored("\t\t    ============", "red"), end="")
	print(colored("=" * 12, "white"), end="") 
	print(colored("=" * 13, "blue"), end="\n")

	print(colored(f"\t\t\t     Domain: {options().domain}", "white"))

# Multi-search mode
# Open file to read sub keywords, start threads
def grabSubs():
	if options().threads:
		print(colored(f"\t\t\t     Threads: {options().threads}", "white"))

	else:
		print(colored(f"\t\t\t     Threads: 10 (default)", "white"))

	domains = []

	with open(options().file, "r") as f:
		for sub in f:

			if sub == "":
				pass
			else:
				sub = str(sub.strip("\n"))
				domains.append(sub)

	print(colored(f"\t\t\t     File: {options().file}", "white"))
	num_lines = sum(1 for line in open(options().file))
	print(colored(f"\t\t\t     Subdomains being tested: {num_lines}\n", "white"))

	if not options().threads:
		threads = 10

	elif options().threads:
		threads = options().threads

	with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
		executor.map(crtpy, domains)

# Parse crt.sh for each sub domain keyword
def crtpy(sub):
	# Make sure each subdomain returned, is unique
	subset=set()
	# Log how many successful searches and record successful subs
	ssubs = []
	# Log how many searches returned zero results and subs with no results
	nosubs = []
	# Log failed searches and failed subs
	fsubs = []

	if options().domain.startswith("*."):
		domain = options().domain[2:]

	else:
		domain = options().domain

	try:	
		url = f"https://crt.sh/?q=%25{sub}%25.{domain}&output=json"
		request = requests.get(url, headers={'User-Agent':header()})
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

# Single search mode
def crtpySingle():
	subset = set()

	domain = options().domain.replace("*","%25")

	# Wildcards and dot notation needed
	url = f"https://crt.sh/?q={domain}&output=json"

	try:
		request = requests.get(url, headers={'User-Agent':header()})
		regex = r'[^%*].*'
		data = request.json()

		if data:
			for row in data:
				row = re.findall(regex, row["name_value"])[0]
				subset.add(row)

	# JSON Decode Error
	except ValueError:
		# Verbose override to help user understand zero results
		print(colored(f"JSON value error!", "yellow"))
		print(colored(f"This could mean no data was found or crt.sh failed to return data.", "yellow"))
		print(colored(f"Parsing domains with a large number of subdomains can sometimes crash results.", "yellow")) 
		print(colored(f"Try again for possibly a different result.\n", "yellow"))
		sys.exit(1)

	# User cancels program
	except KeyboardInterrupt:
		print(colored(f"User cancelled search.", "yellow"))
		sys.exit(0)

	if options().out:
		with open(options().out, "w") as f:
			f.write("\n".join(subset))
		print(colored(f"\nYour search results have been written to: {options().out}", "yellow"))
		grabCount()

	else:
		print("\n")
		print(colored("\n".join(subset), "blue"))
		print("\n")

# Parse keywords mode
def searchSubs():
	if not options().domain:
		print(colored("\nDomain needed to parse subs against!", "red"))
		print(colored("Usage: ./subseeker.py -d [domain] -f [file to grab subs from] optional: -o [file to send results too.]\n", "red"))
		sys.exit(1)

	elif not options().file:
		print(colored("\nA file is needed to parse subs against!", "red"))
		print(colored("Usage: ./subseeker.py -d [domain] -f [file to grab subs from] optional: -o [file to send results too.]\n", "red"))
		sys.exit(1)

	if options().domain.startswith("."):
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
		print(colored(f"\nYour output has been written too {options().out}", "yellow"))
			
		stdoutdata = subprocess.getoutput(f"wc -l {options().out}")
		print(colored(f"Your results have returned {stdoutdata} unique subdomains\n", "yellow"))


	elif not options().out:
		print("\n".join(subset))

# Remove duplicates, if any, return unique number from file count
def grabCount():
	stdoutdata = subprocess.getoutput(f"cat {options().out} | sort -u | wc -l")
	print(colored(f"Your results have returned {stdoutdata} unique subdomains\n", "yellow"))

	subprocess.run(["sort", "-u", f"{options().out}", "-o", f"{options().out}"])

# Clean the screen of the terminal 
def cleanScreen():
	if platform.system() == "Windows":
		subprocess.run(["cls"])
	elif platform.system() == "Linux" or "Darwin":
		subprocess.run(["clear"])

if __name__ == "__main__":
	# uncomment next line, if you want screen cleared disabled
	cleanScreen()

	# parse subs from file with list of domains
	if options().searchsubs:
		searchSubs()
	# regualr search does not use file option, so call crtpy single mode
	elif not options().file:
		title()
		crtpySingle()
	# call crtpy file search mode
	else:
		title()
		grabSubs()

		if options().out:
			print(colored(f"\nYour results have been written too {options().out}", "yellow"))
			grabCount()
