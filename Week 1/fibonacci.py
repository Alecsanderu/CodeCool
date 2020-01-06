nterms = int(input("How many terms? "))
# first two terms
n1, n2 = 0, 1
count = 0
x = 1
for x in range(n1):
    x += 1

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        # print(x, '.',  n1, sep='')
        # print("%-15s %-15s" % (x, n1))
        print('{:>3}.{:>8}'.format(x, n1))
        # print(f'{x:5} {n1}')
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        x += 1
        count += 1
