# Exercice : programmer une fonction(n) 
#            qui retourne les termes de la suite de fibonacci jusqu'Ã  la valeur de n



def fibonacci (n):
            
            print('Les nombres de Fibonacci inférieurs ou égaux à ', n, 'sont :')
            w = 0
            v = 1
            
            while w <= n:        
             print(w)
             w, v = v, v+w
            
           
fibonacci(5)
