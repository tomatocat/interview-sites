# https://www.codewars.com/kata/5526fc09a1bbd946250002dc

def find_outlier(integers):
    numeven = 0
    for x in integers:
        if x % 2 == 0:
            numeven = numeven + 1
    if numeven == 1:
        for x in integers:
            if x % 2 == 0:
                return x
    else:
        for x in integers:
            if x % 2 == 1:
                return x
