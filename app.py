import os

restaurantes = []

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
    nome_do_restaurante = input('Digite o nome do restaurante que quer cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    retornar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    retornar_ao_menu()

def finalizar_app():
    exibir_subtitulo('Finalizando app')

def opcao_invalida():
    exibir_subtitulo('Opção inválida')
    retornar_ao_menu() 

def retornar_ao_menu():
    input('Digite uma tecla para voltar ao meno')
    os.system('cls')
    main()        

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print('')    

def escolher_opcao():
    try:       
            opcao_escolhida = int(input('Escolha uma opção: '))

            if opcao_escolhida == 1: 
                cadastrar_restaurantes()
            elif opcao_escolhida == 2: 
                listar_restaurantes()
            elif opcao_escolhida == 3: 
                print('Ativar restaurante')
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