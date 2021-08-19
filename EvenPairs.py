"""
Even Pairs

Question :
Have the function EvenPairs(str) take the str parameter being passed and determine if a
pair of adjacent even numbers exists anywhere in the string. If a pair exists, return the
string true, otherwise return false. For example: if str is "f178svg3k19k46" then there
are two even numbers at the end of the string, "46" so your program should return the
string true. Another example: if str is "7r5gg812" then the pair is "812" (8 and 12)
so your program should return the string true.

Examples

Input: "3gy41d216"
Output: true

Input: "f09r27i8e67"
Output: false
"""


def EvenPairs(strParam):
    # Converting String to List
    l = list(strParam)

    # Adding a dummy to make the processing easier
    l.append("a")

    # List to store the first number of the Even Pair
    num1 = list()

    # List to store the second number of the Even Pair
    num2 = list()

    # Boolean to specify whether we are creating first number of the Even Pair or not
    isNum1 = True

    # Boolean to specify whether a sequence of even number started or not
    evenSequence = False

    # Traversing through the String passed as argument to this method
    for i in l:

        # Checking whether the element is a number or not
        if i.isdigit():

            # Checking whether we have to create first number of the Even Pair or not
            if isNum1:

                # Converting element from "str" to "int"
                i = int(i)

                # Checking whether element is even or not, so we can start a even sequence
                if (i % 2 == 0):
                    # Updating value of the variable "even sequence"
                    evenSequence = True

                # If current element is an odd number and an even sequence has already
                # started then we have stop creating first number of Even pair and start
                # creating second number of EVen Pair
                if (i % 2 == 1) and evenSequence:

                    # Started preparing second number of the Even Pair
                    num2.append(str(i))

                    # Updating value of the "isNum1" variable to "False" as we have
                    # started creating second number of the Even Pair
                    isNum1 = False

                # When either current element is not an odd number or even sequence
                # hasn't started yet
                else:

                    # Adding the current element to list "num1"
                    num1.append(str(i))

            # When we have to create second number of the Even Pair
            else:

                # Adding the current element to list "num2"
                num2.append(str(i))

        # When current element is not a number
        else:

            # When "num1" and "num2" contains both even and odd numbers
            if (len(num1) != 0) and (len(num2) != 0):

                # Converting lists "num1" and "num2" to strings
                s1 = "".join(num1)
                s2 = "".join(num2)

                # Converting "s1" and "s2" to int and checking whether "s1" and "s2"
                # both are even numbers or not
                if int(s1) % 2 == 0 and int(s2) % 2 == 0:

                    # Returning "true" if both "s1" and "s2" are even numbers
                    strParam = "true"
                    return strParam

                # When either of "s1" or "s2" is not even we are resetting all the
                # important variables to initial value
                else:
                    num1 = []
                    num2 = []
                    isNum1 = True
                    evenSequence = False

            # When "num1" contains only even numbers and "num2" is empty
            elif (len(num1) != 0) and (len(num1) % 2 == 0) and (len(num2) == 0):

                # Creating a boolean to specify whether all the elements in num1 are
                # even or not
                allEven = True

                # Traversing through "num1"
                for i in num1:

                    # If an element of the "num1" is odd then we are breaking the loop
                    if int(i) % 2 == 1:
                        # Updating value of variable "allEven"
                        allEven = False

                        # Getting out of this loop
                        break

                # If variable "allEven" is still "True" then the length of list "num1"
                # is at least 2 and contains all even numbers which cane considered as a
                # Even Pair while the list "num2" is empty
                if allEven:

                    # Returning "true" if all the elements of list "num1" are even and
                    # length of list "num1" is not 0 and list "num2" is empty
                    strParam = "true"
                    return strParam

                # If all the elements of list "num1" are not even numbers, we are
                # resetting all the important variables to initial value
                else:
                    num1 = []
                    num2 = []
                    isNum1 = True
                    evenSequence = False

            # When either both the lists "num1" and "num2" are empty or "num2" is empty
            # and "num1" contains both even and odd numbers, we are resetting all the
            # important variables to initial value
            else:
                num1 = []
                num2 = []
                isNum1 = True
                evenSequence = False

    # Returning "false" when not even a single pair of Even numbers is found
    strParam = "false"
    return strParam


# keep this function call here
print(EvenPairs(input()))
