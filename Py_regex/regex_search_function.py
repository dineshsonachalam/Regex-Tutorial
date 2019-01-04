"""
This function searches for first occurrence of RE pattern within string with optional flags.
"""
import re
line = "Cats are smarter than dogs"
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
if searchObj:
	print "matchObj.group() : ", searchObj.group()
	print "matchObj.group(1) : ", searchObj.group(1)
	print "matchObj.group(2) : ", searchObj.group(2)
else:
	print("No match")