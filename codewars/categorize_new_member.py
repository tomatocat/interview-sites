# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa

def openOrSenior(data):
    return list(map(lambda l:"Senior" if l[0]>=55 and l[1]>7 else "Open", data))
