# Use recursion to do factorial calculation


def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1


if __name__ == "__main__":
    print (factorial(5))
    print (factorial(10))
    print (factorial(100))
