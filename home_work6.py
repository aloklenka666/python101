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
print('str.capitalize()=',str.capitalize())
#capitalize() - Returns the string with first letter capitalized and the rest lowercased.
print('str.casefold()=',str.casefold())
#casefold() - Returns a lowercase string, generally used for caseless matching. This is more aggressive than the lower() method.
print('str.count()=',str.count('l'))
#count() - Count the non-overlapping occurrence of supplied substring in the string.
print('str.encode()=',str.encode())
#encode() - Return the encoded version of the string as a bytes object.
print('str.endswith()=',str.endswith('K'))
#endswith() - Returns ture if the string ends with the supplied substring.
print('str.expandtabs()=',str.expandtabs())
#expandtabs() - Return a string where all the tab characters are replaced by the supplied number of spaces.
print('str.find()=',str.find('l'))
#find() - Return the index of the first occurrence of supplied substring in the string. Return -1 if not found.
print('str.format()=',str.format())
#format() - Format the given string.
print('str.format_map()=',str.format_map('k'))
#format_map() - Format the given string.
print('str.index()=',str.index('U'))
#index() - Return the index of the first occurrence of supplied substring in the string. Raise ValueError if not found.
print('str.isalnum()=',str.isalnum())
#isalnum() - Return true if the string is non-empty and all characters are alphanumeric.
print('str.isalpha()=',str.isalpha())
#isalpha() - Return true if the string is non-empty and all characters are alphabetic.
print('str.isdecimal()=',str.isdecimal())
#isdecimal() - Return true if the string is non-empty and all characters are decimal characters.
print('str.isdigit()=',str.isdigit())
#isdigit() - Return true if the string is non-empty and all characters are digits.
print('str.isidentifier()=',str.isidentifier())
#isidentifier() - Return true if the string is a valid identifier.
print('str.islower()=',str.islower())
#islower() - Return true if the string has all lowercased characters and at least one is cased character.
print('str.isnumeric()=',str.isnumeric())
#isnumeric() - Return true if the string is non-empty and all characters are numeric.
print('str.isprintable()=',str.isprintable())
#isprintable() - Return true if the string is empty or all characters are printable.
print('str.isspace()=',str.isspace())
#isspace() - Return true if the string is non-empty and all characters are whitespaces.
print('str.istitle()=',str.istitle())
#istitle() - Return true if the string is non-empty and titlecased.
print('str.isupper()=',str.isupper())
#isupper() - Return true if the string has all uppercased characters and at least one is cased character.
print('str.join()=',str.join('k'))
#join() - Concatenate strings in the provided iterable with separator between them being the string providing this method.
print('str.ljust()=',str.ljust(3))
#ljust() - Left justify the string in the provided width with optional fill characters.
print('str.lower()=',str.lower())
#lower() - Return a copy of all lowercased string.
print('str.lstrip()=',str.lstrip())
#lstrip() - Return a string with provided leading characters removed.
#str.maketrans()
#maketrans() - Return a translation table.
print('str.partition()=',str.partition('k'))
#partition() - Partition the string at first occurrence of substring (separator) and return a 3-tuple with part before separator, the separator and part after separator.
#str.replace()
#replace() - Replace all old substrings with new substrings.
print('str.rfind()=',str.rfind('U'))
#rfind() - Return the index of the last occurrence of supplied substring in the string. Return -1 if not found.
print('str.rindex()=',str.rindex('U'))
#rindex() - Return the index of the last occurrence of supplied substring in the string. Raise ValueError if not found.
print('str.rjust()=',str.rjust(3))
#rjust() - Right justify the string in the provided width with optional fill characters.
print('str.rpartition()=',str.rpartition('K'))
#rpartition() - Partition the string at last occurrence of substring (separator) and return a 3-tuple with part before separator, the separator and part after separator.
print('str.rsplit()=',str.rsplit())
#rsplit() - Return a list of words delimited by the provided subtring. If maximum number of split is specified, it is done from the right.
print('str.rstrip()=',str.rstrip())
#rstrip() - Return a string with provided trailing characters removed.
print('str.split()=',str.split())
#split() - Return a list of words delimited by the provided subtring. If maximum number of split is specified, it is done from the left.
print('str.splitlines()=',str.splitlines())
#splitlines() - Return a list of lines in the string.
print('str.startswith()=',str.startswith('K'))
#startswith() - Return true if the string starts with the provided substring.
print('str.strip()=',str.strip())
#strip() - Return a string with provided leading and trailing characters removed.
print('str.swapcase()=',str.swapcase())
#swapcase() - Return a string with lowercase characters converted to uppercase and vice versa.
print('str.title()=',str.title())
#title() - Return a title (first character of each word capitalized, others lowercased) cased string.
print('str.translate()=',str.translate('L'))
#translate() - Return a copy of string that has been mapped according to the provided map.
print('str.upper()=',str.upper())
#upper() - Return a copy of all uppercased string.
print('str.zfill()=',str.zfill(3))
#zfill() - Return a numeric string left filled with zeros in the provided width.
#wap to find square root of a number using input form users
import math
number = int(input("Enter the number to find the square root:"))
if number<0:
 print("enter avalid number.")
else:
 print("square root of {} is {}".format(number,math.sqrt(number))) 