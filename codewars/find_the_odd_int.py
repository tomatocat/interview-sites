# https://www.codewars.com/kata/54da5a58ea159efa38000836

def find_it(seq):
    res = 0
    for x in seq:
        res = res ^ x      
    return res
