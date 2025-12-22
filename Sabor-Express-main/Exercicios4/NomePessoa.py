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



