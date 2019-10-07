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
Subseeker is a sub-domain enumeration tool. The tool simply iterates the recon process for finding subdomains from a target domain. Using tools like sublister, knock, etc., subseeker can parse the output of these files for subdomain keywords. From there, those subdomain keywords can be used to individually parse crt.sh for subdomains. Using concurrency, (as shown in the examples) this can iterate a huge number of subdomain keywords in minutes, returning thousands of results.

Subseeker can also parse crt.sh, certdb, censys, and certspotter individually, as if one were using the actual websites.

However, subseeker flourishes with the help of other tools (see example below). Using tools like certspotter, sublist3r, subfinder, and knock (too name a few), running these tools first into output files and then combining them all into one file, creates a file full of
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
usage: python3 subseeker -d [search format][domain] \
EX: python3 subseeker -d *.example.com 

OPTIONAL ARGUMENTS: \
-o Choose to send results to an output file. 
-a Use an API to search certspotter, certdb, and censys.io (needed for censys)
-p Specify page number for certdb and censys
-v Verbose mode

**subseeker certspotter search mode** \
Description: Search for subdomains using just certspotter. \
usage: python3 subseeker --certspotter -d [domain] \
EX: python3 subseeker --certspotter -d example.com

OPTIONAL ARGUMENTS: \
-o Choose to send results to an output file. 
-v Verbose mode

**subseeker certdb search mode** \
Description: Search for subdomains using just certdb. \
usage: python3 subseeker --certdb -d [domain] \
EX: python3 subseeker --certdb -d example.com

OPTIONAL ARGUMENTS: \
-o Choose to send results to an output file. \
-p Specify page number. \
-v Verbose mode

**subseeker censys search mode** \
Description: Search for subdomains using just censys. \
usage: python3 subseeker --censys -d [domain] \
EX: python3 subseeker --censys -d example.com

OPTIONAL ARGUMENTS: \
-o Choose to send results to an output file. \ 
-p Specify page number. \
-v Verbose mode.

**subseeker.py subwordsearch mode** \
Description: Search subdomain keywords through crt.sh. \
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

![example](https://github.com/DFC302/subseeker/blob/master/images/example.png)

# Author:
Coded by Matthew Greer \
Twitter: <https://twitter.com/Vail__> \
Email: DFC302@protonmail.com \
**Tested mainly on Linux**
**Partially tested on Windows**
