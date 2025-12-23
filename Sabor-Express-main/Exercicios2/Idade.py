def idade():
    idade = int(input('Digite sua idade: '))
    if idade < 13 and idade > 0:
        print('Você é criança')
    elif idade > 12 and idade< 18:
        print('Você é adolescente')
    elif idade < 0:
        print('Você está morto')    
    else:
        print('Você é adulto')    
    
def main():
    idade()        

if __name__ == '__main__':
    main()