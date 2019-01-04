"""
Match:
This function attempts to match RE pattern to string with optional flags.

re.match(pattern, string, flags=0)
pattern -> This is the regular exprssion to be matched.
string -> String to be match pattern at beginning of a string.

flags:
re.I -> Performs case-insensitive matching.
re.M -> Makes $ match end of a line.

"""
import re
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
	print "matchObj.group() : ", matchObj.group()
	print "matchObj.group(1) : ", matchObj.group(1)
	print "matchObj.group(2) : ", matchObj.group(2)
else:
	print("No match")