def  recherche_indices_classement(elt,tab):
    tabR = [[],[],[]]

    for key,value in enumerate(tab):
        print(value,elt)
        if value < elt:
            tabR[0].append(key)
        if value == elt:
            tabR[1].append(key)
        if value > elt:
            tabR[2].append(key)
    return (tabR[0],tabR[1],tabR[2])
print(
    recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0])
)


resultats = {'Dupont': {
                           'DS1': [15.5, 4],
                           'DM1': [14.5, 1],
                           'DS2': [13, 4],
                           'PROJET1': [16, 3],
                           'DS3': [14, 4]
                       },
             'Durand': {
                           'DS1': [6 , 4],
                           'DM1': [14.5, 1],
                           'DS2': [8, 4],
                           'PROJET1': [9, 3],
                           'IE1': [7, 2],
                           'DS3': [8, 4],
                           'DS4':[15, 4]
                       }
            }

def moyenne(nom, dico_result):
    if nom in dico_result:
        notes = dico_result[nom]
        total_points = 0
        total_coefficients = 0
        for valeurs in notes.values():
            note, coefficient = valeurs
            total_points = total_points + note * coefficient
            total_coefficients = total_coefficients + coefficient
        return round( total_points / total_coefficients, 1 )
    else:
        return -1
print(moyenne("Durand",resultats))
