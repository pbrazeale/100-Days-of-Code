def is_prime(num):
    for n in range(2, num, 1):
        if n == num:
            pass
        elif num % n == 0:
            return False

    return True

print(is_prime(73))