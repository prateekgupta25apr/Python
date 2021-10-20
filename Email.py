"""
EmailSort

Question:
First get all the alphabets of the email then sort the alphabets then without changing the
position of the special characters and numbers just replace alphabets

Examples

Input: pencil@gmail.com
Output : accegi@illmm.nop

Input : hi.hello@gmail.com
Output : ac.eghhi@illlm.moo
"""

import re

s = input("Enter an email\n")

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

print("".join(result))
