<<<<<<< HEAD
def login():
    print('Cadastre:')
    usuario = input('Crie o usuario')
    senha = input('Crie a senha')
    print('Faça login agora')
    new_usuario = input('Usuario:')
    new_senha = input('Senha:')
    if usuario == new_usuario and senha == new_senha :
        print('Login realizado com sucesso')
    else: 
        print('Usuario ou senha estão incorretos')    

def main():
    login()

if __name__ == '__main__':
=======
def login():
    print('Cadastre:')
    usuario = input('Crie o usuario')
    senha = input('Crie a senha')
    print('Faça login agora')
    new_usuario = input('Usuario:')
    new_senha = input('Senha:')
    if usuario == new_usuario and senha == new_senha :
        print('Login realizado com sucesso')
    else: 
        print('Usuario ou senha estão incorretos')    

def main():
    login()

if __name__ == '__main__':
>>>>>>> 77fea289b63c052bcfff2ca2b04fcdc38082a965
    main()        