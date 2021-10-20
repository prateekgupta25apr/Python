i = int(input("Enter a number\n"))

if i <= 1:
    print(i, "is not a prime number")
else:
    t = True
    for j in range(2, int(i / 2) + 1):
        if i % j == 0:
            t = False
            break
    if t:
        print(i, "is prime number")
    else:
        print(i, "is not prime number")
