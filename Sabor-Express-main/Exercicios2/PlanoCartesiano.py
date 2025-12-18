def cartesiano():
        
            x = float(input('Escolha a posiçao X: '))
            y = float(input('Escolha a posição Y: '))

            if x >= 1 and y >= 1:
                print('Você está no Primeiro quadrante')
                print("""

                    |
                    |      
                    |    aqui
                    |
        -------------------------
                    |
                    |
                    |
                    |
    """)
            elif x <= -1 and y >= 1:
                print('Você está no segundo quadrante')
                print("""

                    |
              aqui  |      
                    |    
                    |
        -------------------------
                    |
                    |    
                    |
                    |
    """)
            elif x <= -1 and y <= -1:
                print ('Você esá no Terceiro quadrante') 

                print("""

                    |
                    |      
                    |    
                    |
        -------------------------
                    |
             aqui   |  
                    |
                    |
    """)
            elif x >= 1 and y <= -1:
                print ('Você esá no Quarto quadrante') 

                print("""

                    |
                    |      
                    |    
                    |
        -------------------------
                    |
                    |  aqui
                    |
                    |
    """)
            else: 
                print('Você está no eixo')



def main():
    cartesiano()
        

if __name__ == '__main__':
    while True:
        main()                             


# Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem. 