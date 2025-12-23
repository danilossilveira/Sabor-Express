<<<<<<< HEAD
import os

numero = []

def cadastrar_numero():
    try:    
        escolha = -1
        for _ in range(5):
            escolha = int(input('Cadastre 5 valores: \n'))
            if escolha % 2 ==0:
                numero.append(escolha)
            else:
                print('Este número é impar')    
        
        print(f'Suas scolhas: {numero}')
    except:
        print('Escolha inválida')
        main()    

def main():
    cadastrar_numero()

if __name__ == '__main__':
    main()        
    







#Desafio 2 – Cadastro de valores (médio)
#O usuário deve cadastrar 5 números
#Apenas números positivos são aceitos
#Cada tentativa (válida ou não) entra em uma lista
#Se o usuário digitar algo inválido:
#Mostra erro
#Continua pedindo
#Ao final, mostre:
#A lista completa
=======
import os

numero = []

def cadastrar_numero():
    try:    
        escolha = -1
        for _ in range(5):
            escolha = int(input('Cadastre 5 valores: \n'))
            if escolha % 2 ==0:
                numero.append(escolha)
            else:
                print('Este número é impar')    
        
        print(f'Suas scolhas: {numero}')
    except:
        print('Escolha inválida')
        main()    

def main():
    cadastrar_numero()

if __name__ == '__main__':
    main()        
    







#Desafio 2 – Cadastro de valores (médio)
#O usuário deve cadastrar 5 números
#Apenas números positivos são aceitos
#Cada tentativa (válida ou não) entra em uma lista
#Se o usuário digitar algo inválido:
#Mostra erro
#Continua pedindo
#Ao final, mostre:
#A lista completa
>>>>>>> 77fea289b63c052bcfff2ca2b04fcdc38082a965
#Quantos valores válidos foram cadastrados