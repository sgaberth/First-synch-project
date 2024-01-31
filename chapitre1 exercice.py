
def e_potentielles (masse, hauteur, e_limit, g=9.81) :
    E = masse*hauteur*g
    C = E <= e_limit
    return C

resultat = e_potentielles(200, 5, 1000)
if resultat :
    print("L'énergie est inférieure ou égale à l'energie limite"); 
else: print("L'énergie est superieure à l'energie limite")
    
    

"L'énergie est inférieure à l'energie limite"