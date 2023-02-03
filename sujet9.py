def multiplication(n1,n2):
  if n2 == 0 or n1 == 0:
    return 0
  elif n1 < 0 and n2 < 0:
    #surement mieux à faire ;)
    n1 -= n1 + n1
    n2 -= n2 + n2
    return n1  + multiplication(n1,n2-1)
  else:
    return n1  + multiplication(n1,n2-1)
    
print(multiplication(-4, -8))
print(multiplication(3, 5))
print(multiplication(-2, 0))
print(multiplication(-2, 6))
