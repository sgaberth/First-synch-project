def signe(x):
    if x < 0:
         print(x, " negatif")
    elif x==0:
        print(x, 'nul')
    else:
        print(x, " positif")
        
for element in range(0, -10, -2):  signe(element)

x = 0
while x <= 20:
    signe(x)
    x += 1
