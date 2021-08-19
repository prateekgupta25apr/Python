"""
Python Age Counting

Question :
In the Python file, write a program to perform a GET request on the route
https://coderbyte.com/api/challenges/json/age-counting which contains a data key and the
value is a string which contains items in the format: key=STRING, age=INTEGER. Your goal
is to count how many items exist that have an age equal to or greater than 50, and print
this final value.

Example Input
{"data":"key=IAfpK, age=58, key=WNVdi, age=64, key=jp9zt, age=47"}

Example Output
2
"""

import requests

# Retrieving data
r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
dataString = r.json()['data']

# Creating list from retrieved data
dataList = dataString.split(",")

# Retrieving all the ages in dataList
ages = list()
for i in range(1, len(dataList), 2):
    age = dataList[i][5:]
    ages.append(int(age))

# Calculating number of ages which are equal to or greater than 50
count = 0
for i in ages:
    if i >= 50:
        count += 1

# Printing the result
print(count)
