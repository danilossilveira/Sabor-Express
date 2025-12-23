<<<<<<< HEAD
lista = [4,6,8]
soma = int(0)
try:
    for i in lista:
        
        soma += i
    soma/=len(lista)
    print(soma)
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")



#Construa um código que calcule a média dos valores em uma lista. 
=======
lista = [4,6,8]
soma = int(0)
try:
    for i in lista:
        
        soma += i
    soma/=len(lista)
    print(soma)
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")



#Construa um código que calcule a média dos valores em uma lista. 
>>>>>>> 77fea289b63c052bcfff2ca2b04fcdc38082a965
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.