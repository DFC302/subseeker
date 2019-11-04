# ChangeLog

All notable changes to this project will be kept and updated here.

**Version 2.2.2**

**(Nov 2, 2019)**
# Bug Fixes
* Reduced code
* Fixed issue with setup.py not correctly installing alias
* Fixed issue with not finding config file for API when in another directory

# Changes
* Fixed CLI options. Reduced options, got rid of short options, and made options more simple.
* Added more colors
* Added icons for different status meanings;
	successful data will be printed in blue
	x No data found
	! Error/Warnings
* Created a basic regex to find domain easier
* Removed verbose mode

**Version 2.1.1**

**(Oct 15, 2019)**
# Bug Fixes
* Fixed issue with censys page mode. Censys may or may not of been displaying data due to wrong type mode for page. Issue is corrected now and is working. 

**(Oct 10, 2019)**
# Bug fixes
* Fixed an issue with certspotter function in searchmodes.py, not properly writing results to output file and displaying a "no data found" error.

# Changes
* Updated config.json to allow Virustotal API

# Features
* Added Virustotal
* Added ThreatCrowd

# Future features
* Working on implementing google

**Version 2.0**

**(Oct 7, 2019)**

# Bug fixes
* Corrected issue with JSON return error not printing on screen correctly.

# Changes
* Changed JSON error response for crtsh
* Added error response for censys, if API credentials are not configured.

# Features
* Added the ability to use just certspotter, censys, or certdb from searchmodes.py
* Added page option to specify page number for certdb and censys.
* Updated README.md

**(Oct 5, 2019)**

# Bug Fixes
* Corrected an issue with useragents not properly returning the correct value.
* Fixed json file and corrected values in searchmodes.py

# Features
* Certspotter support now added
* Certdb support now added
* Censys support now added.
* API option added to flag options.

# Future features
**In progress now**
* Ability to use just certspotter, censys, or certdb by itself.
* Adding page option to select different page results on certdb and censys.

