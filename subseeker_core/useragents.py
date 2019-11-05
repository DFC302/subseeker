from subseeker_core.options import options

def useragent():
	# Chrome header
	if options().useragent == "chrome".lower():
		ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
		(KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
		return ua
	# Firefox header, default
	elif options().useragent == "firefox".lower():
		ua = "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 \
		Firefox/7.0.1"
		return ua
	# Opera header
	elif options().useragent == "opera".lower():
		ua = "Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18"
		return ua
	# If no header specifed, use set firefox
	elif not options().useragent:
		ua = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 \
		Firefox/40.1"
		return ua
