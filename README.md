<p align="center">
  <img width="250" height="250" src="https://github.com/DFC302/subseeker/blob/master/images/logo.jpg">
</p>

[![Build Status](https://travis-ci.org/DFC302/subseeker.svg?branch=master)](https://travis-ci.org/DFC302/subseeker)

# Subseeker
A sub-domain enumeration tool. \
Written in python3.

**Special thanks to tools like certspotter, sublist3r, subfinder, knock, and crt.sh. Without tools like these, subseeker.py would not be what it is.** \
**Special thanks to NahamSec's recon videos. This tool was built around his recon videos. Check him out on twitch, youtube, github, etc.**

**You can find these below:** \
Sublist3r:    <https://github.com/aboul3la/Sublist3r> \
Crtsh:        <https://crt.sh/> \
Certspotter:  https://sslmate.com/certspotter/ \
Certspotter command: "curl -s https://certspotter.com/api/v0/certs\?domain\=$1 | jq '.[].dns_names[]' | sed 's/\"//g' | sed 's/\*\.//g' | sort -u | grep $1" (put in bashrc or bash_aliases) \
Subfinder:    https://github.com/subfinder/subfinder \
Knock:        https://github.com/guelfoweb/knock


# Description:
Subseeker is a sub-domain enumeration tool. The tool simply iterates the recon process for finding subdomains from a target domain. Using tools like certspotter and sublister, subseeker can parse the output of these files for subdomain keywords. From there, those subdomain keywords can be used to individually parse https://crt.sh for subdomains. Using concurrency, (as shown in the examples) this can iterate a huge number of subdomain keywords in minutes, returning thousands of results. The results are then parsed through a python set, so duplicates are removed.

Subseeker can also parse crt.sh individually, as if one were using the actual website.

However, subseeker flourishes with the help of other tools. Using tools like certspotter, sublist3r, subfinder, and knock (too name a few), running these tools first into output files and then combining them all into one file, creates a file full of ton of subdomains. Using the subseeker (option -S), you can parse each subdomain into a file of sub keywords. From there, you can use subseeker to parse crt.sh for each of these sub keywords, using wildcards to return all variants. Doing this manually is time consuiming and requires a ton of effort and time. Subseeker can do this for you in minutes and in the end removes all duplicate URLs, calling a count on the output file returning your number of unique subdomains.

# Requirements
Python 3.x

**Python Modules** \
sys \
re \
platform \
requests \
argparse \
concurrent.futures \
subprocess \
termcolor

# Installation 
git clone https://github.com/DFC302/subseeker.git \
chmod 755 subseeker/main.py

# Usage
![usage](https://github.com/DFC302/subseeker/blob/master/images/usage.png)

    usage: subseeker.py [-h] [-d DOMAIN] [-f FILE] [-o OUT] [-H HEADER] [-v] [-S]
              [-t THREADS]

    optional arguments:
      -h, --help            show this help message and exit
      -d DOMAIN, --domain DOMAIN
                            Specify domain to search.
      -f FILE, --file FILE  Specify in file.
      -o OUT, --out OUT     Specify file to write results too.
      -H HEADER, --header HEADER
                            Specify header to use.
      -v, --verbose         Turn on verbose mode.
      -S, --searchsubs      Use regex to grab subdomains from domain.
      -t THREADS, --threads THREADS
                            Number of threads.


**subseeker.py single-search mode** \
Description: Search any variation of wildcard through crt.sh. \
usage: ./subseeker.py -d [search format][domain] \
EX: ./subseeker.py -d *.example.com 

OPTIONAL ARGUMENTS: \
-o Choose to send results to an output file. 

**subseeker.py multi-search mode** \
Description: Search subdomain keywords through crt.sh. \
Note: keywords are processed like so: \*[keyword]\*.[domain] \
Note: keywords should be written to file with each keyword on a new line, like so:

dev \
test \
ops \
mail
    
usage: ./subseeker.py -d [domain] -f [file containing subdomain keywords] \
EX: ./subseeker.py -d example.com -f domain_keywords.txt 

OPTIONAL ARGUMENTS: \
-H Choose a different header, default is Firefox. \
-t Choose number of threads. \
-v Verbose mode. \
-o Choose to send results to an output file. 

The keywords.txt file is a file that is provided, that can be used with multi-search mode.

**subseeker.py parse sub domain keywords** \
Description: Parse through sublister, certspotter, etc. text outputs for sub domain keywords. \
Note: If using sublist3r, use sublist3r's option [-o] to send results to outfile. Subseeker.py is designed to parse from a text file. Using standard redirection ">",">>", copies ANSI color codes, which will conflict with parsing. \
subseeker.py -S -d [domain] -f [file contaning output from certspotter, sublister, etc. results] \
EX: ./subseeker.py -S -d example.com -f certspotter_results.txt

OPTIONAL ARGUMENTS: \
-o Choose to send results to an output file.

# Examples:
**Single-Search Mode** \
![single-search mode](https://github.com/DFC302/subseeker/blob/master/images/singlemode.png)

**Multi-Search Mode (Default threads)** \
![multi-default](https://github.com/DFC302/subseeker/blob/master/images/results2.png)

**Multi-Search Mode (50 threads)** \
![multi-search mode](https://github.com/DFC302/subseeker/blob/master/images/mult-search.png)

# Author:
Coded by Matthew Greer \
Twitter: <https://twitter.com/Vail__> \
Email: DFC302@protonmail.com \
**Tested on Linux only**
