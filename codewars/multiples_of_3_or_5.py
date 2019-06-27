#https://www.codewars.com/kata/514b92a657cdc65150000006/

def solution(number):
    if number == 0:
        return 0
    if (number - 1) % 3 == 0 or (number - 1) % 5 == 0:
        return (number - 1) + solution(number - 1)
    return solution(number - 1)
