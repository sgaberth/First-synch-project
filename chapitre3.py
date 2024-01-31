# STRUCTURES DE DONNEES : SEQUENCES
# c'est un ensemble ordonné de données
# chaque element a un index, ce qui nous permet d'acceder aux elements de la sequence
# l'index du premier element est 0, celui du dernier est -1
# la différence du tuple de la liste est qu'on ne peux pas modifier son contenu


# Listes
Liste_1 = [1, 2, 5, 6, 11]
Liste_2 = ['Paris', 'Berlin', 'Londres', 'Bruxelles']
Liste_3 = []
Liste_4 =[[Liste_1], [Liste_2]]

# Tuples
tuple_1 = (1, 5, 8, 45)

# Strings
prenom = 'Berthe'

# Indexing
# c'est acceder aux éléments de la séquence via les indexs de ces éléments
print(Liste_2[0]) # le premier element
print(Liste_2[1]) # le deuxieme element
print(Liste_2[-1]) # le dernier element
print(Liste_2[-2]) # le avant deuxieme element

# Slicing
print(Liste_2[1:2])
print(Liste_2[:2])
print(Liste_2[2:])
print(Liste_2[1:3:1])
print(Liste_2[::1])
print(Liste_2[::-1])

print(prenom[:3])

Liste_2[2] = 'Dublin'
print(Liste_2)

Liste_2.append('Berlin')
print(Liste_2)
Liste_2.insert(2, 'Madrid')
print(Liste_2)
villes = ['Rome', 'Moscou', 'Athenes']
Liste_2.extend(villes)
print(Liste_2)
len(Liste_2)
Liste_1.sort(reverse=True)
print(Liste_1)
Liste_2.sort()
print(Liste_2)

print(Liste_2.count('Berlin'))
print(Liste_2.count('Bamako'))

if 'Paris' in Liste_2:
    print('Oui')
else:
    print('Non')
    
for i in Liste_2:
    print(i)
for index, valeur in enumerate(Liste_2):
    print(index, valeur)

for a, b in zip(Liste_1, Liste_2):
    print(a, b)
