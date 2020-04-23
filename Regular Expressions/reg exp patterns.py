import re

string = "search inside of this this this text, please!"
# pattern = re.compile(r"([a-zA-Z]).([a])")
# a = pattern.search(string)
# print(a.group())
# print(a.group(1))
# print(a.group(2))

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
email = "jerinthomas17@gmail.com"
email2 = 'jerin'

a = pattern.search(email)
print(a)
b = pattern.search(email2)
print(b)


pattern2 = re.compile(r"[(a-zA-Z0-9$%@#)]{8,}")
password = "Jerinthomas@123"

c = pattern2.fullmatch(password)
print(c)