def isEven(number):
    return number % 2 == 0

def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True