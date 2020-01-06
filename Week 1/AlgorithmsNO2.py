def GCD(a, b):
    if a < b:
        smaller = a
    else:
        smaller = b

    for i in range(1, smaller+1):
        if (a % i == 0) & (b % i == 0):
            gcd = i

    return gcd


print(GCD(80, 36))
print(GCD(2019, 1869))
