def is_prime(n):
    if n == 1:
        return False

    if n == 2:
        return True

    for i in range(2, n, 1):
        if n % i == 0:
            return False

    return True


s = int(input("Number: "))

if is_prime(s):
    print("The " + str(s) + " is prime!")
else:
    print("The " + str(s) + " is not prime!")