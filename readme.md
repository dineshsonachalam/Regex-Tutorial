# Regex Tutorial

### Regex Syntax:
```
abc…	Letters
123…	Digits
\d	Any Digit
\D	Any Non-digit character
.	Any Character
\.	Period
[abc]	Only a, b, or c
[^abc]	Not a, b, nor c
[a-z]	Characters a to z
[0-9]	Numbers 0 to 9
\w	Any Alphanumeric character
\W	Any Non-alphanumeric character
{m}	m Repetitions
{m,n}	m to n Repetitions
*	Zero or more repetitions
+	One or more repetitions
?	Optional character
\s	Any Whitespace
\S	Any Non-whitespace character
^…$	Starts and ends
(…)	Capture Group
(a(bc))	Capture Sub-group
(.*)	Capture all
(abc|def)	Matches abc or def
```

1. Match specific characters

Match only specific characters using regular expressions by defining them inside the square brackets.
Here [abc] match only single a,b or c.

```
Task	Text	 
Match	can	
Match	man	
Match	fan	
Skip	dan	
Skip	ran	
Skip	pan
```
Soultion:
```
[cmf]an -> Matches the task
```

2. Excluding specific characters

Exclude specific characters using the square brackets and the ^ (hat).
For Example: patter[^abc] will match any single character except for the letters a, b or c.

```

Task	Text	 
Match	hog	Success
Match	dog	Success
Skip	bog 

```
Solution:
```
[^b]og -> Will match any character that doesnt have b followed by og
[hd]og -> Will match hog and dog
```

3. Character Ranges

- There is a shorthand for matching a character in list of sequential characters by using the dash to indicate a character range. For example, the pattern [0-6] will only match any single digit character from zero to six, and nothing else. And likewise, [^n-p] will only match any single character except for letters n to p.

- Multiple character ranges can also be used in the same set of brackets, along with individual characters. An example of this is the alphanumeric \w metacharacter which is equivalent to the character range [A-Za-z0-9_] and often used to match characters in English text.

```
Exercise 5: Matching Character Ranges
Task	Text	 
Match	Ana	Success
Match	Bob	Success
Match	Cpc	Success
Skip	aax	To be completed
Skip	bby	To be completed
Skip	ccz	To be completed

```
Solution:

```
[A-C][n-p][a-c]
```

4. Matching repeated characters

a{3} -> will match a character exactly 3 times (aaa).
a{3,5} -> will match aaa,aaaa,aaaaa


```
Exercise 6: Matching Repeated Characters
Task	Text	 
Match	wazzzzzup	Success
Match	wazzzup	Success
Skip	wazup
```
Solution:
```
waz{3,5}up
```

Things to know:

```
\d* -> Will match any number of digits.
a+  -> 1 or more a's
[abc]+ -> 1 or more of any a, b, or c character
.* -> 0 or more of any characters
```

```
Exercise 7: Matching Repeated Characters
Task	Text	 
Match	aaaabcc	Success
Match	aabbbbc	Success
Match	aacc	Success
Skip	a	To be completed
```
Solution:
```
aa+b*c*
```

5. Matching optional character

Here ? denotes the optionality.
ab?c -> will match string 'abc' (or) 'ac'

The question mark is a special character and you will have to escape it using a slash \? to match a plain question mark character in a string.

```
Exercise 8: Matching Optional Characters
Task	Text	 
Match	1 file found?	Success
Match	2 files found?	Success
Match	24 files found?	Success
Skip	No files found.
```

Solution:
```
\d+ files? found\?
```

6. Matching Whitespaces

Whitespace character \s will match any of specific whitespaces.

```
Exercise 9: Matching Whitespaces
Task	Text	 
Match	1.   abc	Success
Match	2.	abc	Success
Match	3.           abc	Success
Skip	4.abc
```

Solution:

```
\d.\s+abc
```

7. Starting and ending

- ^…$	Starts and ends
- The start and the end of the line using the special ^ (hat) and $ (dollar sign) metacharacters. 

Note that this is different than the hat used inside a set of bracket [^...] for excluding characters, which can be confusing when reading regular expressions.

```
Exercise 10: Matching Lines
Task	Text	 
Match	Mission: successful	Success
Skip	Last Mission: unsuccessful	To be completed
Skip	Next Mission: successful upon capture of target
```
Solution:
```
^Mission: successful$
```

8. Matching groups
- (....) Capture group
-  ^(IMG\d+\.png)$ to capture and extract the full filename, but if you only wanted to capture the filename without the extension, you could use the pattern ^(IMG\d+)\.png$ which only captures the part before the period.
- Here \. is Period

```
Exercise 11: Matching Groups
Task	Text	Capture Groups	 
Capture	file_record_transcript.pdf	file_record_transcript	Success
Capture	file_07241999.pdf	file_07241999	Success
Skip	testfile_fake.pdf.tmp
```
Solution:
```
^(file.+)\.pdf
```

9. Matching the nested subgroup
- (a(bc))	Capture Sub-group

```
Exercise 12: Matching Nested Groups
Task	Text	Capture Groups	 
Capture	Jan 1987	Jan 1987 1987	Success
Capture	May 1969	May 1969 1969	Success
Capture	Aug 2011	Aug 2011 2011	Success
```
Solution:
```
(\w+ (\d+))
```

10. Matching nested groups
```
Exercise 13: Matching Nested Groups
Task	Text	Capture Groups	 
Capture	1280x720	1280 720	Success
Capture	1920x1600	1920 1600	Success
Capture	1024x768	1024 768	Success

```
Solution:
```
(\d+)x(\d+)
```

11. Match conditional text

```
Exercise 14: Matching Conditional Text
Task	Text	 
Match	I love cats	Success
Match	I love dogs	Success
Skip	I love logs	To be completed
Skip	I love cogs	
```

Solution:
```
((\w +\w+)+ (cats|dogs))
```
