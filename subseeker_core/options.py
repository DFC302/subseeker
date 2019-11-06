# This file contains information regarding command line arguments, title
# information and version information.

import argparse
import sys
from termcolor import colored

# User options
def options():
	parser = argparse.ArgumentParser()

	# specify domain
	parser.add_argument(
		"--domain",
		help="Specify domain to search.",
		action="store",
	)

	# single search mode
	parser.add_argument(
		"--singlesearch",
		help="Search using a specific certificate site.",
		action="store",
		type=str,
	)

	# User can specify keywords instead of a file full of sub keywords
	parser.add_argument(
		"--keywords",
		nargs="+",
		help="Add a list of keywords.",
		type=str,
	)

	# Parse subdomain keywords from other tools output files
	parser.add_argument(
		"--generate",
		help="Create a list of sub domain keywords from a file containing \
		subdomains.",
		action="store_true",
	)

	# search domain using subdomain keywords from file
	parser.add_argument(
		"--file",
		help="Specify a file containing keywords to parse crt.sh OR to create \
		sub keywords from.",
		action="store",
	)

	# Write to output file
	parser.add_argument(
		"--out",
		help="Specify a file to write results too.",
		action="store",
	)

	# User specify number of threads
	parser.add_argument(
		"--threads",
		help="Specify number of threads to be used when performing keyword \
		search.",
		action="store",
		type=int,
	)

	# Try with different headers, firefox, chrome, opera
	parser.add_argument(
		"--useragent",
		help="Specify a user-agent to use. Default is a firefox UA.",
		action="store",
		type=str
	)

	# If API information has been configured, allow use of API credentials
	parser.add_argument(
		"--api",
		help="Turn on api.",
		action="store_true",
	)

	# Specify page number for certdb and/or censys
	parser.add_argument(
		"--page",
		help="Used with certdb and/or censys searchmodes. Specify page number to display.",
		action="store",
		type=int,
	)

	parser.add_argument(
		"--version",
		help="Display version information",
		action="store_true",
	)

	parser.add_argument(
		"--verbose",
		help="Display extra verbose information, such as errors.",
		action="store_true",
	)

	# if not arguments are given, print usage message
	if len(sys.argv[1:]) == 0:
		parser.print_help()
		parser.exit()

	args = parser.parse_args()

	return args