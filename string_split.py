import re
arn = "arn:aws:iam::123456789012:user/JohnDoe"
m = arn.split("/")[1]
print(m)
""" for i in range(len(m)):
    print(m[i]) """
fname = "vandhana"
lname = "ic"
print(fname.upper())
str1 = fname + lname
print(str1)
print(len(arn))

# regex 
textt = "the fox is as cunning as a miser"
pattern = r"miser"
match = re.match(pattern, textt)
if match:
    print("match found:", match.group())
else:
    print("no match")

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")