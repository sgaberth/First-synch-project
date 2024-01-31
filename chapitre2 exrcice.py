# Exercice : programmer une fonction(n) 
#            qui retourne les termes de la suite de fibonacci jusqu'Ã  la valeur de n



def fibonacci (n):
            
            print('Les nombres de Fibonacci inférieurs ou égaux à ', n, 'sont :')
            w = 0
            v = 1
            u = 0
            print(u)
            u = 1
            
            x = 1
            while (x <= n):        
                if u <= n:
                    print(u)
                u = v + w
                w = v
                v = u
                x += 1
            
            print('//') 
            print('Fibonacci de',n, ':', w)
            
fibonacci(7)
