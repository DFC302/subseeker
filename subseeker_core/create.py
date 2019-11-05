from subseeker_core.options import options
import re

class GenerateKeywords():
	# Create sub domain keywords to search from
	def create(self):
		if options().domain:
			domain_regex = r"[a-zA-Z0-9].*"
			domain = re.findall(domain_regex, options().domain)[0]

		print(domain)
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

		print("\n".join(subset))

		# If write to outfile is specified
		if options().out:
			with open(options().out, "a") as wf:
				wf.write("\n".join(subset))
				wf.write("\n")
			print(f"\nYour results have been written too {options().out}")
