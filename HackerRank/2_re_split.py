"""
re.split() -> Split string by occurrence of a pattern.
"""
regex_pattern = r"[,.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))