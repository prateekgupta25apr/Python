# n = int(input("Enter a number"))
#
#
# def decimalToBinary(n):
#     return "{0:b}".format(int(n))
#
#
# i = decimalToBinary(n)
# print(i)
#
#
# def editNum(n):
#     l = list(n)
#     for i in range(len(l)):
#         if (i+1) % 2 == 0:
#             if l[i] == "0":
#                 l[i] = "1"
#             else:
#                 l[i] = "0"
#         else:
#             if l[i] == "1":
#                 l[i] = "0"
#     return "".join(l)
#
#
# print(editNum(str(i)))

# abcdffff
# ffffabcd


n=input("Enter a hex number")

l=list(n)
p=list()
p.extend(l[len(l)/2])
