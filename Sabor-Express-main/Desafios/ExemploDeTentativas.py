import os

def teste():
    try:
        numero = -1
        for _ in range(3):
            numero = int(input('Digite um número positivo: \n'))  
            if numero > 0:
                os.system('cls')
                print(numero)
                print('Seu número é positívo')
                break
            else:
                print('Incorreto')                  
            if _ >= 2:
                os.system('cls')
                print('Limite de tentativas atingido')
            else:
                print(f'Você tentou {_+1} vezes')
    except:
        print('Tente novamnente')
                        
def main():
     teste()

if __name__ == '__main__':
     while True:
        main()     