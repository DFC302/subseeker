#!/usr/bin/env python

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
		"-d", "--domain",
		help="Specify domain to search.",
		action="store",
	)

	# User can specify keywords instead of a file full of sub keywords
	parser.add_argument(
		"-k", "--keywords",
		nargs="+",
		help="Add a list of keywords.",
		type=str,
	)

	# Parse subdomain keywords from other tools output files
	parser.add_argument(
		"-C", "--createsubs",
		help="Create a list of sub domain keywords from a file containing \
		subdomains.",
		action="store_true",
	)

	# search domain using subdomain keywords from file
	parser.add_argument(
		"-f", "--file",
		help="Specify a file containing keywords to parse crt.sh OR to create \
		sub keywords from.",
		action="store",
	)

	# Write to output file
	parser.add_argument(
		"-o", "--out",
		help="Specify a file to write results too.",
		action="store",
	)

	# User specify number of threads
	parser.add_argument(
		"-t", "--threads",
		help="Specify number of threads to be used when performing keyword \
		search.",
		action="store",
		type=int,
	)

	# Try with different headers, firefox, chrome, opera
	parser.add_argument(
		"-u", "--useragent",
		help="Specify a user-agent to use. Default is a firefox UA.",
		action="store",
		type=str
	)

	# If API information has been configured, allow use of API credentials
	parser.add_argument(
		"-a", "--api",
		help="Turn on api.",
		action="store_true",
	)

	# Call just certspotter
	parser.add_argument(
		"--certspotter",
		help="Search just using certspotter.",
		action="store_true",
	)

	# Call just certdb
	parser.add_argument(
		"--certdb",
		help="Search just using certdb.",
		action="store_true",
	)

	# Call just censys
	parser.add_argument(
		"--censys",
		help="Search just using censys.",
		action="store_true",
	)

	# Call just virustotal
	parser.add_argument(
		"--virustotal",
		help="Seach just using virustotal.",
		action="store_true",
	)

	# Call just threatcrowd
	parser.add_argument(
		"--threatcrowd",
		help="Search just using threatcrowd.",
		action="store_true",
	)

	# Specify page number for certdb and/or censys
	parser.add_argument(
		"-p", "--page",
		help="Used with certdb and/or censys searchmodes. Specify page number to display.",
		action="store",
		type=int,
	)

	# Turn on verbose mode.
	parser.add_argument(
		"-v", "--verbose",
		help="Turn on verbose mode.",
		action="store_true",
	)

	parser.add_argument(
		"-V", "--version",
		help="Display version information",
		action="store_true",
	)

	# if not arguments are given, print usage message
	if len(sys.argv[1:]) == 0:
		parser.print_help()
		parser.exit()

	args = parser.parse_args()

	return args

def title():
  # Print default title info
  print(colored("\n\t\t\t\t\t  SUBSEEKER", "red"))
  print(colored("\t\t\t\t===============================", "red"))
  print(colored(f"\t\t\t\tDOMAIN:\t\t{options().domain}", "red"))

  # if verbose mode is on, tell user, if not tell user
  if options().verbose:
  	print(colored(f"\t\t\t\tVERBOSE:\tON", "red"))
  else:
  	print(colored(f"\t\t\t\tVERBOSE:\tOFF", "red"))

  # Display choosen header, if not chosen, display default
  if options().useragent:
  	print(colored(f"\t\t\t\tUser-Agent:\t{options().useragent.lower()}","red"))
  elif not options().useragent:
    print(colored(f"\t\t\t\tUser-Agent:\tFirefox (Default)", "red"))
    
  # If file option is used, show how many sub keywords are in file
  if options().file:
    print(colored(f"\t\t\t\tFILE:\t\t{options().file}", "red"))
    count_lines = sum(1 for line in open(options().file))
    print(colored(f"\t\t\t\tKEYWORDS:\t{count_lines}", "red"))

  # If keywords option is used, show how many keywords are being parsed against 
  # crtsh
  if options().keywords:
    print(colored(f"\t\t\t\tKEYWORDS:\t{len(options().keywords)}", "red"))

  # Since threading is only used with the file or keyword options, display 
  # threads. Else if user still uses these options, but does not use threads, 
  # display default threads
  if options().threads and options().file or options().keywords:
    print(colored(f"\t\t\t\tTHREADS:\t{options().threads}", "red"))
  elif not options().threads:
  	if options().file:
  		print(colored(f"\t\t\t\tTHREADS:\t10", "red"))
  	elif options().keywords:
  		print(colored(f"\t\t\t\tTHREADS:\t10", "red"))
  	elif not options().threads and not options().file and not options().keywords:
  		pass

# Version information
def version():
	print(colored("\n\t\t\t\t\t\t\tSUBSEEKER", "yellow"))
	print(colored("\t\t\t\t===================================================="\
		, "yellow"))
	print(colored("\t\t\t\t VERSION:\t\t2.0", "yellow"))
	print(colored("\t\t\t\t Author:\t\tMatthew Greer", "yellow"))
	print(colored("\t\t\t\t Twitter:\t\thttps://twitter.com/Vail___", "yellow"))
	print(colored("\t\t\t\t Github:\t\thttps://github.com/DFC302\n", "yellow"))

if __name__ == "__main__":
	main()
