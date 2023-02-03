t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

def  mini(t_moy, annees):
    mini  = t_moy[0]
    index = 0
    for key,value in enumerate(t_moy):
        if t_moy[key] < mini:
            index = key
            mini = value
    return( mini,annees[index])
print(
    mini(t_moy, annees)
)


   
def inverse_chaine(chaine):
    result = ""
    for caractere in chaine:
       result = caractere +result 
    return result
print(inverse_chaine("lopm"))
def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return inverse == chaine
print(est_palindrome('NSI'))
print(est_palindrome('ISN-NSI'))
def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)
print(est_nbre_palindrome(214312))
print(est_nbre_palindrome(213312))
