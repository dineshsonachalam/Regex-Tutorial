import re
line = "Cats are smarter than dogs"
matchObj = re.match( r'dogs', line, re.M|re.I)
searchObj = re.search(r'dogs',line, re.M|re.I)
if matchObj:
	print "matchObj.group() : ", matchObj.group()
	print "matchObj.group(1) : ", matchObj.group(1)
	print "matchObj.group(2) : ", matchObj.group(2)
else:
	print("No match")

if searchObj:
	print "searchObj.group(): ",searchObj.group()
	
num = re.sub(r'\D', "", "112-3341-22")
print(num)
