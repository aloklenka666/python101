#wap to find largest number of three numbers (a,b,c),ask input from users.
a =float(input("enter the first number:" ))
b =float(input("enter the second number:" ))
c =float(input("enter the third number:" ))
if(a>=b) and (a>=c):
 largest = a
elif(b>=a) and (b>=c):
 largest = b
else:
 largest = c
print("the largest number between",a,",",b,"and",c,"is",largest)
#wap to implement all string functionalities and comment on each and everry function after looking at the result.
str ="ALOK KUMAR LENKA"
str.capitalize()
#capitalize() - Returns the string with first letter capitalized and the rest lowercased.
str.casefold()
#casefold() - Returns a lowercase string, generally used for caseless matching. This is more aggressive than the lower() method.
str.count('l')
#count() - Count the non-overlapping occurrence of supplied substring in the string.
str.encode()
#encode() - Return the encoded version of the string as a bytes object.
str.endswith('o')
#endswith() - Returns ture if the string ends with the supplied substring.
str.expandtabs()
#expandtabs() - Return a string where all the tab characters are replaced by the supplied number of spaces.
str.find('l')
#find() - Return the index of the first occurrence of supplied substring in the string. Return -1 if not found.
str.format()
#format() - Format the given string.
str.format_map('k')
#format_map() - Format the given string.
str.index('U')
#index() - Return the index of the first occurrence of supplied substring in the string. Raise ValueError if not found.
str.isalnum()
#isalnum() - Return true if the string is non-empty and all characters are alphanumeric.
str.isalpha()
#isalpha() - Return true if the string is non-empty and all characters are alphabetic.
str.isdecimal()
#isdecimal() - Return true if the string is non-empty and all characters are decimal characters.
str.isdigit()
#isdigit() - Return true if the string is non-empty and all characters are digits.
str.isidentifier()
#isidentifier() - Return true if the string is a valid identifier.
str.islower()
#islower() - Return true if the string has all lowercased characters and at least one is cased character.
str.isnumeric()
#isnumeric() - Return true if the string is non-empty and all characters are numeric.
str.isprintable()
#isprintable() - Return true if the string is empty or all characters are printable.
str.isspace()
#isspace() - Return true if the string is non-empty and all characters are whitespaces.
str.istitle()
#istitle() - Return true if the string is non-empty and titlecased.
str.isupper()
#isupper() - Return true if the string has all uppercased characters and at least one is cased character.
str.join('k')
#join() - Concatenate strings in the provided iterable with separator between them being the string providing this method.
str.ljust(3)
#ljust() - Left justify the string in the provided width with optional fill characters.
str.lower()
#lower() - Return a copy of all lowercased string.
str.lstrip()
#lstrip() - Return a string with provided leading characters removed.
#str.maketrans()
#maketrans() - Return a translation table.
str.partition('k')
#partition() - Partition the string at first occurrence of substring (separator) and return a 3-tuple with part before separator, the separator and part after separator.
#str.replace()
#replace() - Replace all old substrings with new substrings.
str.rfind('U')
#rfind() - Return the index of the last occurrence of supplied substring in the string. Return -1 if not found.
str.rindex('U')
#rindex() - Return the index of the last occurrence of supplied substring in the string. Raise ValueError if not found.
str.rjust(3)
#rjust() - Right justify the string in the provided width with optional fill characters.
str.rpartition('K')
#rpartition() - Partition the string at last occurrence of substring (separator) and return a 3-tuple with part before separator, the separator and part after separator.
str.rsplit()
#rsplit() - Return a list of words delimited by the provided subtring. If maximum number of split is specified, it is done from the right.
str.rstrip()
#rstrip() - Return a string with provided trailing characters removed.
str.split()
#split() - Return a list of words delimited by the provided subtring. If maximum number of split is specified, it is done from the left.
str.splitlines()
#splitlines() - Return a list of lines in the string.
str.startswith('K')
#startswith() - Return true if the string starts with the provided substring.
str.strip()
#strip() - Return a string with provided leading and trailing characters removed.
str.swapcase()
#swapcase() - Return a string with lowercase characters converted to uppercase and vice versa.
str.title()
#title() - Return a title (first character of each word capitalized, others lowercased) cased string.
str.translate('L')
#translate() - Return a copy of string that has been mapped according to the provided map.
str.upper()
#upper() - Return a copy of all uppercased string.
str.zfill(3)
#zfill() - Return a numeric string left filled with zeros in the provided width.