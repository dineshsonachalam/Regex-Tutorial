"""
re.findall()
The expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings. 

re.finditer()
The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string. 
"""
import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags = re.I)
print('\n'.join(m or ['-1']))