# Exercice : programmer une fonction(n) 
#            qui retourne les termes de la suite de fibonacci jusqu'à la valeur de n



def fibonacci (n):
            
            print('Les nombres de Fibonacci inf�rieurs ou �gaux �', n, 'sont :')
            w = 0
            v = 1
            
            while w <= n:        
             print(w)
             w, v = v, v+w
            
           
fibonacci(5)
