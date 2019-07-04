def getdigit(x):
    """

    :type x: int or float
    """
    returnDigit = 0
    while x > 0:
        x /= 10
        returnDigit += 1
    return returnDigit


print getdigit(2 ** 512)
print 2 ** 512
