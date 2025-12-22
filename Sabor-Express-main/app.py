import os

restaurantes = [{'nome':'Dona Luíza', 'categoria':'Pizza','ativo':False},
                {'nome':'García', 'categoria':'Churrasco','ativo':True},
                {'nome':'Rafa Sushi', 'categoria':'Sushi','ativo':False}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def cadastrar_restaurantes():
    exibir_subtitulo('Cadastro de restaurante')
    nome = input('Digite o nome do restaurante que quer cadastrar: \n')
    categoria = input(f'Qual é a categoria do(a) {nome}?\n')
    restaurante_dados = {'nome' : nome, 'categoria' : categoria, 'ativo' : False}
    restaurantes.append(restaurante_dados)
    print(f'O restaurante {nome} foi cadastrado com sucesso!')
    retornar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    print('Nome:'.ljust(20), 'Categoria'.ljust(20), 'Estado')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = restaurante['ativo']
        ativo = 'Ativado' if restaurante['ativo']else 'Desativado'
        print(f'{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')
    retornar_ao_menu()

def finalizar_app():
    exibir_subtitulo('Finalizando app')

def opcao_invalida():
    exibir_subtitulo('Opção inválida')
    retornar_ao_menu() 

def retornar_ao_menu():
    input('Digite uma tecla para voltar ao menu')
    os.system('cls')
    main()        

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto)+5)
    print(linha)
    print(' ',texto)
    print(linha)
    print('')    

def ativar_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Escolha o restaurante para alterar o estado: \n')
    restaurante_encontrado = False  
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não encontrado')        
    retornar_ao_menu()
    
def escolher_opcao():
    try:       
            opcao_escolhida = int(input('Escolha uma opção: '))

            if opcao_escolhida == 1: 
                cadastrar_restaurantes()
            elif opcao_escolhida == 2: 
                listar_restaurantes()
            elif opcao_escolhida == 3: 
                ativar_restaurante()
            elif opcao_escolhida == 4: 
                finalizar_app()
            else:
                opcao_invalida()
    except:
        opcao_invalida()            
                
def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()