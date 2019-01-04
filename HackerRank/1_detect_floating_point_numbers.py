"""
^ says start of the expression.

[-+]? says it can start with either - or +.

[0-9] says any number from 0-9 can be followed after it.

* says that whichever thing it follows[in this case it is[0-9]], it can repeat arbitrarily times, even 0 times.

'.' is placeholder for any character.(for the answer it should be '\.' instead of '.' ; '\' is escape character. Because of this you can literally mean a dot in expression).

again[0-9] as explained earlier.

'+' says that whichever thing it follows[in this case it is[0-9]], it can repeat arbitrarily times, but atleast one time.

$ follows whichever thing it should come in the end.
"""

import re
n = int(input())
for _ in range(0,n):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))

