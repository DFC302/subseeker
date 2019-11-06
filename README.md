<p align="center">
  <img width="250" height="250" src="https://github.com/DFC302/subseeker/blob/master/images/logo.jpg">
</p>

[![Build Status](https://travis-ci.org/DFC302/subseeker.svg?branch=master)](https://travis-ci.org/DFC302/subseeker) \
![version](https://img.shields.io/badge/version-2.0.1-dark_green) \
[![Follow on Twitter](https://img.shields.io/twitter/follow/Vail__.svg?logo=twitter)](https://twitter.com/Vail__)

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-dark_green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) \
**Check changelog.md for latest updates**

# Subseeker
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


# Description:
Subseeker is a sub-domain enumeration tool, which simply iterates the recon process for finding subdomains from a target domain. 

# What makes it different?
(**see example below**)
Subseeker flourishes with the use of keywords. These keywords can be found in the wordlists folder. However, keywords can also be made up on the fly using the [--keywords] option. Subseeker can also use the output from other tools like sublister, subfinder, knock, etc. Using the [--generate] option on the output files from these tools, subseeker will create a list of keywords that can then be used to find deep level subdomains. This in turn, creates a huge list of subdomains returned for the user.

Subseeker also parses all domains and keywords into a set, so dupliate domains are removed. No need to uniquely sort the output files.

Subseeker can also parse data from certificate sites individually, if the user does not want to search all certificate sites at once using the [--singlesearch (option)] option.

Subseeker parses data from crtsh, certdb, censys, certspotter, threatcrowd, virustotal, securitytrails.


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
usage: subseeker [-h] [--domain DOMAIN] [--singlesearch SINGLESEARCH]
                 [--keywords KEYWORDS [KEYWORDS ...]] [--generate]
                 [--file FILE] [--out OUT] [--threads THREADS]
                 [--useragent USERAGENT] [--api] [--page PAGE] [--version]

optional arguments:
  -h, --help            show this help message and exit
  --domain DOMAIN       Specify domain to search.
  --singlesearch SINGLESEARCH
                        Search using a specific certificate site.
  --keywords KEYWORDS [KEYWORDS ...]
                        Add a list of keywords.
  --generate            Create a list of sub domain keywords from a file
                        containing subdomains.
  --file FILE           Specify a file containing keywords to parse crt.sh OR
                        to create sub keywords from.
  --out OUT             Specify a file to write results too.
  --threads THREADS     Specify number of threads to be used when performing
                        keyword search.
  --useragent USERAGENT
                        Specify a user-agent to use. Default is a firefox UA.
  --api                 Turn on api.
  --page PAGE           Used with certdb and/or censys searchmodes. Specify
                        page number to display.
  --version             Display version information
```

# Usage
**Note: API credentials needed for censys, virustotal, securitytrails.**

**subseeker default search** \
Description: Search for subdomains from a top level domain. Wildcard notation excepted.
usage: subseeker --domain [domain] \
EX: subseeker --domain *.example.com 

OPTIONAL ARGUMENTS: \
--useragent Choose a different useragent, default is Firefox. \
--out Choose to send results to an output file. \
--api Use an API to search certspotter, certdb, and censys.io (needed for censys, virustotal, securitytrails) \
--page Specify page number for certdb and censys \

**subseeker keyword search** \
Description: Search for subdomains from a top level domain using keywords to find deep level subdomains.(will also search domain through certspotter, censys, Virustotal, and ThreatCrowd)

**WARNING: For searchmodes other than crtsh, some sites do not accept wildcard notation. So subseeker will fix the domain for you. For example, if you do something like: \*.example.com, subseeker will fix it to: example.com. Since crtsh accepts wildcard notation it will not be fixed! Whatever domain you type in is the domain that gets parsed, for example: \*.yahoo.com, when using keywords from [--keywords] option or from a file, will come out like so \*[keyword]\*\*.example.com with an extra star. This will most likely cause crtsh to not return results.**

Note: keywords are processed like so: \*[keyword]\*.[domain] \
Note: If keywords are written to a file, each keyword should be on a new line, like so:

dev \
test \
ops \
mail

usage: subseeker --domain [domain] --file [file containing subdomain keywords] \
usage: subseeker --domain [domain] --keywords [keywords (separated by spaces, NOT COMMAS!!!)] \
EX: subseeker --domain example.com --file domain_keywords.txt
EX: subseeker --domain example.com --keywords test dev product

OPTIONAL ARGUMENTS: \
--useragent Choose a different useragent, default is Firefox. \
--threads Choose number of threads. \
--out Choose to send results to an output file. \
--keywords Choose keywords to parse domains with. \
--api Enable search with API credentials. \
--page Specify page mode for censys and certdb.

The keywords.txt file is a file that is provided for you, that can be used with keyword searches.

**subseeker parse generate keywords** \
Description: Parse through sublister, certspotter, etc. text outputs and create sub domain keywords. \

**Special Note: If using sublist3r, use sublist3r's option [-o] to send results to outfile. (Subseeker is designed to parse from a text file. Using standard redirection ">",">>", copies ANSI color codes, which will conflict with parsing.)**

usage: subseeker --generate --domain [domain] --file [file contaning output from certspotter, sublister, etc. results] \
**Domain should be without wildcard notation, www, https, etc. Just the name of the domain and level (com, org, etc)** \
EX: subseeker --generate --domain example.com --file results.txt

OPTIONAL ARGUMENTS: \
--out Choose to send results to an output file.

**subseeker singlesearch** \
Description: Search crtsh, certspotter, certdb, censys, virustotal, threatcrowd, individually. \
usage: subseeker --singlesearch [site option]

Options: \
  crtsh \
  certspotter \
  certdb \
  censys \
  virustotal \
  threatcrowd

EX: subseeker --singlesearch certspotter

OPTIONAL ARGUMENTS: \
--useragent Choose a different useragent, default is Firefox. \
--out Choose to send results to an output file. \
--api Use an API to search certspotter, certdb, and censys.io (needed for censys, virustotal, securitytrails) \
--page Specify page number for certdb and censys \

**Configure API credentials in core/subseeker_config.json file.**

# Example usage:
**Here is an example usage on how you can fully take advantage of subseeker.**

Yes, subseeker can locate subdomains on its own. However, it was built around the idea of using sub domain keywords to parse crtsh for even greater results. You can aquire these sub domain keywords by using subeeker to parse crtsh, censys, certspotter, and certdb into an output file or files and/or by using other subdomain tools. From there, using the [--generate] option, subseeker will parse the second layer of each domain to create keywords.

For example, say I generate subdomains like so: \
test.example.com \
test.dev.example.com \
products.example.com 

Using the [--generate] option will then create a list of keywords like so: \
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
