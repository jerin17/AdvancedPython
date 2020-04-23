import re

string = "search inside of this this this text, please!"

print('search' in string)
a = re.search('this', string)
print(a)
print(a.group())
print()

pattern = re.compile('this')
pattern2 = re.compile('search inside of this this this text, please ?')
a = pattern.search(string)
b = pattern.findall(string)
c = pattern2.fullmatch(string)
d = pattern2.match(string)

print(a)
print(b)
print(c)
print(d)

