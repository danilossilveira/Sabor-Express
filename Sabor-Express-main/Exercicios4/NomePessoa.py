<<<<<<< HEAD
import os

lista = [{'nome':'Danilo', 'Idade':'19', 'Cidade':'Porto Alebre'},
         {'nome':'Pedro', 'Idade':'18', 'Cidade':'Alvorada'},
         {'nome':'Nicolas', 'Idade':'18', 'Cidade':'Viamão'},
         {'nome':'Sarah', 'Idade':'18', 'Cidade':'Gravataí'}]

def voltar_menu():
    input('"ENTER" para voltar ao menu')
    os.system('cls')
    escolhas()

def cabecario(titulo):
    os.system('cls')
    print(titulo)
    print('\n')

def menu_inicial():
    print("""
    O que quer fazer?
    1- Cadastrar pessoa
    2- Listar pessoa
    3- Buscar alguem expecífico    
    4- Alterar algum dado
    5- Excluir alguma pessoa
    6- Sair                                                                                
""")
    
def menu_alteracao():
    cabecario('Alterar algum dado')
    escolha = int(input("""
    Qual dado quer alterar?
    1-Nome
    2-Idade
    3-Cidade                                                
"""))
    if escolha == 1:
        modificar_nome()
    elif escolha == 2:
        modificar_idade()
    elif escolha == 3:
        modificar_cidade()
    else:
        print('Essa opção não existe')
        menu_alteracao()       

def modificar_nome():
    cabecario('Modificar nome')
    buscar_pessoa = input('Quer modificar o nome de quem?')
    for pessoa in lista:
       if buscar_pessoa == pessoa['nome']:
        novo_nome = input('Quer alterar para qual nome?')
        pessoa.update({'nome': novo_nome})
        print('Modificado com sucesso')
        voltar_menu()
    else:
        print('Pessoa não encontrada')
        modificar_nome()

def modificar_cidade():
    buscar_pessoa = input('Qual nome da pessoa que você quer alterar a idade?')
    cabecario('Modificar cidade')
    for pessoa in lista:
       if buscar_pessoa == pessoa['nome']:       
        nova_cidade = input('Digite a nova cidade:')
        pessoa.update({'Cidade': nova_cidade})
        print('Modificado com sucesso')    
        voltar_menu()
    else:
        print('Pessoa não encontrada')
        modificar_cidade()

def modificar_idade():
    cabecario('Modificar idade')
    buscar_pessoa = input('Quer modificar a idade de quem?')
    for pessoa in lista:    
     if buscar_pessoa == pessoa['nome']:
        nova_idade = input('Qual a nova idade dessa pessoa?')
        pessoa.update({'Idade': nova_idade})   
        print('Modificado com sucesso')     
        voltar_menu()
    else:
        print('Pessoa não encontrada')            
        modificar_idade()

def listar():
    cabecario('Listar cadastrados')
    for pessoa in lista:
        nome = pessoa['nome']
        idade = pessoa['Idade']
        cidade = pessoa['Cidade']
        print(f'Nome: {nome}\nIdade: {idade}\nCidade: {cidade}\n')
        
    voltar_menu()    

def adicionar_pessoa():
    cabecario('Menu inicial')
    cabecario('Cadastrar pessoa')
    nome = input('Escolha o nome de quem você quer adicionar')
    idade = input('Idade:')
    cidade = input('Cidade:')
    pessoa_dado = {'nome' : nome, 'Idade' : idade, 'Cidade' : cidade}
    lista.append(pessoa_dado)
    print('Pessoa cadastrada')
    voltar_menu()

def procurar_alguem():
    cabecario('Buscar alguém expecífico')
    procurar_pessoa = input('Quem você procura?')
    for pessoa in lista:
        if procurar_pessoa == pessoa['nome']:
            print(pessoa)
            voltar_menu()    

    else:
        print('Pessoa não encontrada')

    procurar_alguem()

def deletar_pessoa():
    cabecario('Excluir pessoa')
    buscar_pessoa = input('Quem você quer excluir?\n')  
    for pessoa in lista:
        if buscar_pessoa == pessoa['nome']:           
            print('Pessoa removida')
            lista.remove(pessoa)
            voltar_menu()
    else:
        print('Pessoa não encontrada')

    deletar_pessoa()        

def escolhas():
    try:    
        menu_inicial()
        escolha = int(input())
        if escolha == 1:
            adicionar_pessoa()
        elif escolha == 2:
            listar()
        elif escolha == 3:
            procurar_alguem()
        elif escolha == 4:
            menu_alteracao()
        elif escolha == 5:
            deletar_pessoa()
        elif escolha == 6:
            print('Até mais')
        else:
            print('Opção inválida')
            voltar_menu()
    except ValueError:
        print('Você não pode inserir uma vogal')
        voltar_menu()                                 


def main():
    escolhas()

if __name__ == '__main__':
    main()            

 

=======
lista = [{'nome':'Danilo', 'Idade':'19', 'Cidade':'Porto Alebre'},
         {'nome':'Pedro', 'Idade':'18', 'Cidade':'Alvorada'},
         {'nome':'Nicolas', 'Idade':'18', 'Cidade':'Viamão'},
         {'nome':'Sarah', 'Idade':'18', 'Cidade':'Gravataí'}]

def menu_inicial():
    escolha = input("""
    O que quer fazer?
    1- Cadastrar pessoa
    2- Listar pessoa
    3- Alterar algum dado
    4- Excluir alguma pessoa
    5- Sair                                                                                
""")
    
def menu_alteracao():
    escolha = input("""
    Qual dado quer alterar?
    1-Nome
    2-Idade
    3-Cidade                                                
""")
    if escolha == 1:
        modificar_nome()
    elif escolha == 2:
        modificar_idade()
    elif escolha == 3:
        modificar_cidade()
    else:
        print('Essa opção não existe')
        menu_alteracao()       

def modificar_nome():
    for pessoa in lista:
        buscar_pessoa = input('Quer modificar o nome de quem?')
        if buscar_pessoa == pessoa['nome']:
            novo_nome = input('Quer alterar para qual nome?')
            pessoa.update({'nome': novo_nome})
            print('Modificado com sucesso')
        else:
            print('Pessoa não encontrada')

def modificar_cidade():
    for pessoa in lista:
        buscar_pessoa = input('Qual nome da pessoa que você quer alterar a idade?')
        if buscar_pessoa == pessoa['nome']:
            nova_cidade = input('Digite a nova cidade:')
            pessoa.update({'Cidade': nova_cidade})
            print('Modificado com sucesso')
        else:
            print('Pessoa não encontrada')

def modificar_idade():
    for pessoa in lista:    
        buscar_pessoa = input('Quer modificar a idade de quem?')
        if buscar_pessoa == pessoa['nome']:
            nova_idade = input('Qual a nova idade dessa pessoa?')
            pessoa.update({'Idade': nova_idade})   
            print('Modificado com sucesso')     
            
        else:
            print('Pessoa não encontrada')            



def informacoes():
    for pessoa in lista:
        nome = pessoa['nome']
        idade = pessoa['Idade']
        cidade = pessoa['Cidade']
        print(f'Nome: {nome}\nIdade: {idade}\nCidade: {cidade}\n')

def main():
    informacoes()
    modificar_idade()

if __name__ == '__main__':
    main()            



>>>>>>> 77fea289b63c052bcfff2ca2b04fcdc38082a965
