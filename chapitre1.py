x=1
y=2.5
a=True

u, v = 2, 1.9


# Arithmétique
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)
print(x//y)
print(x%y)

# Comparaison
print(x==y)
print(x!=y)
print(x<=y)
print(x>=y)

# Logique
print(False & True) # And
print(False or True) # Or
print(False ^ True) # XOr
print(False and True) # And
print(False or True)

# String
prenom = 'Alou'
print(prenom)

# Les fonctions
f = lambda x : x**2
g = lambda x, y : 2*x+5*y-10
print(f(3))
print(g(5, 8))
print("Les fonctions")

def e_potentielles (masse, hauteur, g) :
    E = masse*hauteur*g
    return E

resultat = e_potentielles(20, 5, 9.81)
print('le sesultat est ', resultat)

