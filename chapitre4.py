
# =============================================================================
# les dictionnaires
# ce sont des listes comme les séquences, mais dans les qels il ny pas d ordre
# les sont les clefs associés à des valeurs
# =============================================================================

traduction = {
    'Chien' : 'dog',
    'Chat' : 'cat',
    'souris' : 'mouse',
    'oiseau' : 'bird'
    }

inventaire = {
    'bananes' : 5000,
    'pommes' : 2410,
    'poires' : 15840
    }
dictionnaire_3 = {
    'dic1' : traduction,
    'dic2' : inventaire
    }

# =============================================================================
# print(inventaire.values())
# print(inventaire.keys())
# print(len(inventaire))
# =============================================================================

# =============================================================================
# liste1 = ('Paris', 'Bamako', 'Berlin')
# 
# inventaire['abricots'] = 25000
# 
# print(inventaire.get('pommes'))
# print(inventaire.fromkeys(liste1, 'default'))
# print(inventaire)
# result = inventaire.pop('poires')
# print(result)
# =============================================================================
for i, k in inventaire.items():
    print(i, k)