# 8.1

def combos(n):
  if n == 1:
    return 1
  tmp, i, a, b, c = 0, 2, 1, 1, 2
  while i <= n:
    tmp = a + b + c
    c, b, a = tmp, c, b
   return c
