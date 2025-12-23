<<<<<<< HEAD
import os

numero = []
pares = []
impares = []
escolha = -1

def numero_par_impar():
    for _ in range(100):
        escolha = input('Digite um número: \n')
        if escolha == '':
            print('Números digitados: ', numero)
            for n in numero:
                if n %2 == 0:
                    pares.append(n)
                else:
                    impares.append(n)

            print('Números pares: ',pares,' Números ímpares: ',impares)
            break

        else:
            numero.append(escolha)

def main():
    numero_par_impar()

if __name__ == '__main__':
    main()


    





#Desafio 3 – Análise simples (difícil)
#O usuário digita números até decidir parar
#Todas as entradas válidas vão para uma lista
#Use try / except para evitar erro
#Ao final, mostre:
#Quantos números foram digitados
#Quantos são positivos
#Quantos são negativos
#Se quiser aumentar a dificuldade depois:
#tirar limite de tentativas
#exigir mais regras
=======
import os

numero = []
pares = []
impares = []
escolha = -1

def numero_par_impar():
    for _ in range(100):
        escolha = input('Digite um número: \n')
        if escolha == '':
            print('Números digitados: ', numero)
            for n in numero:
                if n %2 == 0:
                    pares.append(n)
                else:
                    impares.append(n)

            print('Números pares: ',pares,' Números ímpares: ',impares)
            break

        else:
            numero.append(escolha)

def main():
    numero_par_impar()

if __name__ == '__main__':
    main()


    





#Desafio 3 – Análise simples (difícil)
#O usuário digita números até decidir parar
#Todas as entradas válidas vão para uma lista
#Use try / except para evitar erro
#Ao final, mostre:
#Quantos números foram digitados
#Quantos são positivos
#Quantos são negativos
#Se quiser aumentar a dificuldade depois:
#tirar limite de tentativas
#exigir mais regras
>>>>>>> 77fea289b63c052bcfff2ca2b04fcdc38082a965
#misturar dois desafios em um