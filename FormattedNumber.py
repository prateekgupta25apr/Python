"""
Formatted Number

Question :
Have the function FormattedNumber(strArr) take the strArr parameter being passed, which
will only contain a single element, and return the string true if it is a valid number
that contains only digits with properly placed decimals and commas, otherwise return the
string false. For example: if strArr is ["1,093,222.04"] then your program should return
the string true, but if the input were ["1,093,22.04"] then your program should return
the string false. The input may contain characters other than digits.

Examples

Input: ["0.232567"]
Output: true

Input: ["2,567.00.2"]
Output: false
"""


def FormattedNumber(strArr):
    # Splitting string by commas
    l = strArr[0].split(",")

    # Traversing through list l
    for i in range(len(l)):

        # Checking for 2 adjacent commas and more than 3 numbers between 2 commas
        if len(l[i]) == 0:
            return "false"

        # Splitting element by decimal
        f = l[i].split(".")

        # Making sure decimal is not placed at the start or end of the element
        if len(f[0]) == 0 or len(f[-1]) == 0:
            return "false"

        # Checking first element
        if i == 0:

            # Making sure not more than 1 decimal is placed
            if len(f) > 2:
                return "false"

            # Making sure there are only 3 digits before decimal
            if len(f[0]) > 3:
                return "false"

        # Checking for last element
        elif i == (len(l) - 1) and len(l) > 1:

            # Making sure not more than 1 decimal is placed
            if len(f) > 2:
                return "false"

            # Making sure decimal is placed after 3 digits
            if len(f[0]) != 3:
                return "false"

        # Checking middle elements
        else:

            # Making sure no decimal is placed
            if len(f) > 1:
                return "false"

            # Making sure element length is 3 only
            if len(l[i]) != 3:
                return "false"

    # Returning "true" if all the commas and decimals are placed correctly
    return "true"


# keep this function call here
print(FormattedNumber(input()))
