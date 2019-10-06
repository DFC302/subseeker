<p align="center">
  <img width="250" height="250" src="https://github.com/DFC302/subseeker/blob/master/images/logo.jpg">
</p>

[![Build Status](https://travis-ci.org/DFC302/subseeker.svg?branch=master)](https://travis-ci.org/DFC302/subseeker)

# Version 2.0

# Subseeker
A sub-domain enumeration tool. \
Written in python3.

**Special thanks to tools like certspotter, sublist3r, subfinder, knock, and crt.sh. Without tools like these, subseeker.py would not be what it is.** \
**Special thanks to NahamSec's recon videos. This tool was built around his recon videos. Check him out on twitch, youtube, github, etc.**

**You can find these below:** \
Sublist3r:    <https://github.com/aboul3la/Sublist3r> \
Crtsh:        <https://crt.sh/> \
Certdb:       https://certdb.com/ \
Certspotter:  https://sslmate.com/certspotter/ \
Subfinder:    https://github.com/subfinder/subfinder \
Knock:        https://github.com/guelfoweb/knock


# Description:
Subseeker is a sub-domain enumeration tool. The tool simply iterates the recon process for finding subdomains from a target domain. Using tools like sublister, knock, etc., subseeker can parse the output of these files for subdomain keywords. From there, those subdomain keywords can be used to individually parse crt.sh for subdomains. Using concurrency, (as shown in the examples) this can iterate a huge number of subdomain keywords in minutes, returning thousands of results. The results are then parsed through a python set, so duplicates are removed.

Subseeker can also parse crt.sh, certdb, censys, and certspotter individually, as if one were using the actual websites.

However, subseeker flourishes with the help of other tools. Using tools like certspotter, sublist3r, subfinder, and knock (too name a few), running these tools first into output files and then combining them all into one file, creates a file full of
subdomains. Using the subseeker (option -S), you can parse each subdomain into a file of sub keywords. From there, you can use subseeker to parse crt.sh for each of these sub keywords, using wildcards to return all variants. You can also now use the keyword option (-k) to create a keyword list on the fly, and use that to parse crt.sh. Doing either of these manually is time consuiming and requires a ton of effort and time. Subseeker however, can do this for you in minutes.

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
termcolor \
json

# Installation
git clone https://github.com/DFC302/subseeker.git \
chmod 755 subseeker/subseeker

# Usage
![usage](https://github.com/DFC302/subseeker/blob/master/images/usage.png)

**subseeker.py default search mode** \
Description: Search any variation of wildcard through crt.sh, certspotter, certdb, and censys.io \
usage: ./subseeker.py -d [search format][domain] \
EX: ./subseeker.py -d *.example.com 

OPTIONAL ARGUMENTS: \
-o Choose to send results to an output file. 
-a Use an API to search certspotter, certdb, and censys.io (needed for censys)

**subseeker.py subwordsearch mode** \
Description: Search subdomain keywords through crt.sh. \
Note: keywords are processed like so: \*[keyword]\*.[domain] \
Note: keywords should be written to file with each keyword on a new line, like so:

dev \
test \
ops \
mail
    
usage: ./subseeker -d [domain] -f [file containing subdomain keywords] \
usage: ./subseeker -d [domain] -k [keywords (separated by spaces)]
EX: ./subseeker.py -d example.com -f domain_keywords.txt 

OPTIONAL ARGUMENTS: \
-H Choose a different header, default is Firefox. \
-t Choose number of threads. \
-v Verbose mode. \
-o Choose to send results to an output file. \
-k Choose keywords to parse domains with. \
-a Enable search with API credentials.

The keywords.txt file is a file that is provided, that can be used with multi-search mode.

**subseeker.py parse createsubs mode** \
Description: Parse through sublister, certspotter, etc. text outputs for sub domain keywords. \
Note: If using sublist3r, use sublist3r's option [-o] to send results to outfile. Subseeker.py is designed to parse from a text file. Using standard redirection ">",">>", copies ANSI color codes, which will conflict with parsing. \
subseeker.py -S -d [domain] -f [file contaning output from certspotter, sublister, etc. results] \
EX: ./subseeker.py -S -d example.com -f certspotter_results.txt

OPTIONAL ARGUMENTS: \
-o Choose to send results to an output file.

**Configure API credentials in config.json file.**

# Author:
Coded by Matthew Greer \
Twitter: <https://twitter.com/Vail__> \
Email: DFC302@protonmail.com \
**Tested mainly on Linux**
**Partially tested on Windows**
