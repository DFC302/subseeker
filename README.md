<p align="center">
  <img width="250" height="250" src="https://github.com/DFC302/subseeker/blob/master/images/logo.jpg">
</p>

[![Build Status](https://travis-ci.org/DFC302/subseeker.svg?branch=master)](https://travis-ci.org/DFC302/subseeker) \
![version](https://img.shields.io/badge/version-2.0.1-dark_green) \
[![Follow on Twitter](https://img.shields.io/twitter/follow/Vail__.svg?logo=twitter)](https://twitter.com/Vail__)

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-dark_green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) \
**Check changelog.md for latest updates**

# Subseeker
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) \
A sub-domain enumeration tool. \
Written in Python3

**Special thanks to tools like certspotter, sublist3r, subfinder, knock, and crt.sh. Without tools like these, subseeker.py would not be what it is.**

**You can find these below:** \
Sublist3r:    <https://github.com/aboul3la/Sublist3r> \
Crtsh:        <https://crt.sh/> \
Certdb:       https://certdb.com/ \
Certspotter:  https://sslmate.com/certspotter/ \
Subfinder:    https://github.com/subfinder/subfinder \
Knock:        https://github.com/guelfoweb/knock


# Description:
Subseeker is a sub-domain enumeration tool, which simply iterates the recon process for finding subdomains from a target domain. 

# What makes it different?
(**see example below**)
Subseeker flourishes with the use of keywords. These keywords can be found in the wordlists folder. However, keywords can also be made up on the fly using the [--keywords] option. Subseeker can also use the output from other tools like sublister, subfinder, knock, etc. Using the [--createsubs] option on the output files from these tools, subseeker will create a list of keywords that can then be used to find deep level subdomains. This in turn, creates a huge list of subdomains returned for the user.

Subseeker can also parse data from certificate sites individually, if the user does not want to search all certificate sites at once. 

Subseeker parses data from crtsh, certdb, censys, certspotter, threatcrowd, and virustotal.


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
colorama \
json \
os

# Installation
python3 setup.py install

# Manual installation
git clone https://github.com/DFC302/subseeker.git \
chmod 755 core/subseeker.py

# Usage
```
usage: subseeker [-h] [-d DOMAIN] [-k KEYWORDS [KEYWORDS ...]] [-C] [-f FILE]
                 [-o OUT] [-t THREADS] [-u USERAGENT] [-a] [--certspotter]
                 [--certdb] [--censys] [--virustotal] [--threatcrowd]
                 [-p PAGE] [-v] [-V]

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Specify domain to search.
  -k KEYWORDS [KEYWORDS ...], --keywords KEYWORDS [KEYWORDS ...]
                        Add a list of keywords.
  -C, --createsubs      Create a list of sub domain keywords from a file
                        containing subdomains.
  -f FILE, --file FILE  Specify a file containing keywords to parse crt.sh OR
                        to create sub keywords from.
  -o OUT, --out OUT     Specify a file to write results too.
  -t THREADS, --threads THREADS
                        Specify number of threads to be used when performing
                        keyword search.
  -u USERAGENT, --useragent USERAGENT
                        Specify a user-agent to use. Default is a firefox UA.
  -a, --api             Turn on api.
  --certspotter         Search just using certspotter.
  --certdb              Search just using certdb.
  --censys              Search just using censys.
  --virustotal          Seach just using virustotal.
  --threatcrowd         Search just using threatcrowd.
  -p PAGE, --page PAGE  Used with certdb and/or censys searchmodes. Specify
                        page number to display.
  -v, --verbose         Turn on verbose mode.
  -V, --version         Display version information
```

**subseeker.py default search mode** \
Description: Search any variation of wildcard through crt.sh, certspotter, certdb, censys.io, Virustotal, threatcrowd\
usage: python3 subseeker -d [search format][domain] \
EX: python3 subseeker -d *.example.com 

OPTIONAL ARGUMENTS: \
-o Choose to send results to an output file. \
-a Use an API to search certspotter, certdb, and censys.io (needed for censys) \
-p Specify page number for certdb and censys \
-v Verbose mode


**subseeker.py subwordsearch mode** \
Description: Search subdomain keywords through crt.sh. (will also search domain through certspotter, censys, Virustotal, and ThreatCrowd) \
**WARNING: For the other searchmodes (other than crtsh), subseeker fixes the domain for you. So if you do something like: \*.example.com, subseeker will fix it to: example.com. For crtsh and subwordsearch mode, it is not fixed! So whatever domain you type in is the domain that gets parsed, for example: \*.yahoo.com, when using keywords, would come out like so \*[keyword]\*\*.example.com with an extra star.**\
Note: keywords are processed like so: \*[keyword]\*.[domain] \
Note: keywords should be written to file with each keyword on a new line, like so:

dev \
test \
ops \
mail

**Special Note:** \
**Domain must be without "." or "\*" notation. For example: example.com NOT .example.com or \*.example.com**\
usage: python3 subseeker -d [domain] -f [file containing subdomain keywords] \
usage: python3 subseeker -d [domain] -k [keywords (separated by spaces)] \
EX: python3 subseeker -d example.com -f domain_keywords.txt 

OPTIONAL ARGUMENTS: \
-H Choose a different header, default is Firefox. \
-t Choose number of threads. \
-v Verbose mode. \
-o Choose to send results to an output file. \
-k Choose keywords to parse domains with. \
-a Enable search with API credentials. \
-p Specify page mode.

The keywords.txt file is a file that is provided, that can be used with multi-search mode.

**subseeker.py parse createsubs mode** \
Description: Parse through sublister, certspotter, etc. text outputs for sub domain keywords. \
Note: If using sublist3r, use sublist3r's option [-o] to send results to outfile. (Subseeker is designed to parse from a text file. Using standard redirection ">",">>", copies ANSI color codes, which will conflict with parsing.) \
usage: python3 subseeker -C -d [domain] -f [file contaning output from certspotter, sublister, etc. results] \
EX: python3 subseeker -C -d example.com -f certspotter_results.txt

OPTIONAL ARGUMENTS: \
-o Choose to send results to an output file.

**Configure API credentials in config.json file.**

# Example usage:
**Here is an example usage on how you can fully take advantage of subseeker.**

Yes, subseeker can locate subdomains on its own. However, it was built around the idea of using sub domain keywords to parse crtsh. You can aquire these sub domain keywords by using subeeker to parse crtsh, censys, certspotter, and certdb into an output file or files and/or by using other subdomain tools. From there, using the createsubs option (-C), it will parse the second layer of each domain to create keywords.

For example, say I generate subdomains like so: \
test.example.com \
test.dev.example.com \
products.example.com 

Using the -C option will then create a list of keywords like so: \
test \
dev \
products

From there this list can be used to generate even more subdomains from crt.sh. Subseeker will automatically search with the syntax like so: \
\*test\*.example.com \
\*dev\*.example.com \
\*products\*.example.com

This is why using other subdomain tools and parsing the results into output files can then be used to generate a huge list of keywords to parse crt.sh with.

| TOOL | TIME | NUMBER OF KEYWORDS USED | SUBDOMAINS FOUND | THREAD COUNT |
| --- | --- | --- | --- | --- |
| subseeker | 8m9.243s | 1348 | 56793 | 10 (Default)

**Using Concurrency**

| TOOL | TIME | NUMBER OF KEYWORDS USED | SUBDOMAINS FOUND | THREAD COUNT |
| --- | --- | --- | --- | --- |
| subseeker | 4m49.491s | 1348 | 57335 | 200 (Max tested) |

# Author:
Coded by Matthew Greer \
Twitter: <https://twitter.com/Vail__> \
Email: DFC302@protonmail.com \
**Tested mainly on Linux**
**Partially tested on Windows**
