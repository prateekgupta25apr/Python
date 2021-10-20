"""
First get all the alphabets of the email then sort the alphabets then without changing the
position of the special characters and numbers just replace alphabets
"""

import re

s = "prateek.gupta25apr@gmail.com"
print("Original String", s, "size =", len(s))

regex = r'[A-Za-z]+'
l = list(s)
r = list()
d = dict()
for i in range(len(l)):
    if re.fullmatch(regex, l[i]):
        r.append(l[i])
    else:
        d[i] = l[i]
r.sort()
# print(r)
# print(d)

result = list()
i = 0
j = 0
t = (len(r) + len(d))
while i < t:
    if d.get(i) is not None:
        result.append(d.get(i))
        d.pop(i)
        i += 1
    else:
        result.append(r[j])
        i += 1
        j += 1

print("Processed String", "".join(result), "size =", len(result))
