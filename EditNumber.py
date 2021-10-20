"""
EditNumber

Question:
Take a number as input in decimal convert it to binary and then toggle the values at odd
positions and set the values at even positions if they are unset.

Examples

Input: 4
Output: 010

Input: 8
Output: 0101

"""


def decimal_to_binary(num):
    return "{0:b}".format(int(num))


def edit_num(num):
    num = list(num)
    for i in range(len(num)):
        if (i + 1) % 2 == 0:
            if num[i] == "0":
                num[i] = "1"
            else:
                num[i] = "0"
        else:
            if num[i] == "1":
                num[i] = "0"
    return "".join(num)


n = int(input("Enter a number\n"))
print(edit_num(str(decimal_to_binary(n))))
