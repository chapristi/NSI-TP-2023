def moyenne(tab):
  moy = 0
  for i in tab:
    moy +=i
  return moy /len(tab)
print(moyenne([1.0])
)
print(moyenne([1.0, 2.0, 4.0]))

def binaire(a):
    bin_a = str(a % 2)
    
    a = a // 2
    while a > 0 :
        bin_a = str(a % 2)  + bin_a
        
        a = a//2
        
    return bin_a
print(binaire(83))
print( binaire(127))
print( binaire(0))
