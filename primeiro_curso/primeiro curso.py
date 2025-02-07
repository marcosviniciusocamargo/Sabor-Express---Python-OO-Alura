import os
from selectors import SelectSelector

restaurantes = [{'nome':"Café", 'categoria': 'Padaria', 'ativo': False},
                {'nome':"Cebola", 'categoria': 'Supermercado', 'ativo': True},
                {'nome':"Kibarato", 'categoria': 'Supermercado', 'ativo': True}]

def main():
    os.system('cls')
    pega_opcao()

def exibe_menu():
    menu = '''
    ****** SABOR EXPRESS ******
    1. Cadastrar restaurante
    2. Listar restaurantes
    3. Aternar estado do restaurante
    4. Sair
    
    '''
    return menu

def exibe_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(f'{texto}')
    print(linha)

def saida_menu():
    input('\nDigite uma tecla para continuar')
    main()

def cadastrar_restaurente():
    exibe_subtitulo('Cadastro de Restaurantes')
    nome = input('Nome: ')
    categoria = input('Categoria: ')
    restaurante = {'nome':nome, 'categoria':categoria, 'ativo':False}
    restaurantes.append(restaurante)
    print(f'\n{nome} cadastrado com sucesso')
    saida_menu()

def listar_restaurantes():
    exibe_subtitulo('Restaurantes Cadastrados')
    print(f'{'*NOME*'.ljust(20)}  {'*CATEGORIA*'.ljust(20)}   {'*STATUS*'}')
    for restaurante in restaurantes:
        ativado = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'{restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {ativado}')
    saida_menu()

def alternar_estado_restaurante():
    exibe_subtitulo("Alterando Status do Restaurante")

    nome = input("Nome do restaurante: ")
    encontrado = False
    for restaurante in restaurantes:
        if restaurante['nome'].lower() == nome.lower():
            encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            print(f'O restaurante {restaurante['nome']} foi ativado com sucesso' if restaurante['ativo'] else
                  f'O restaurante {restaurante['nome']} foi desativado com sucesso')
    if not encontrado:
        print('Restaurante não encontrado')

    saida_menu()


def pega_opcao():
    try:
        opcao = int(input(exibe_menu()))
        match opcao:
            case 1:
                cadastrar_restaurente()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
    except:
        opcao_invalida()

def finalizar_app():
    os.system('cls')
    print("Finalizando App!")

def opcao_invalida():
    print("Opção inválida")
    main()


if __name__ == '__main__':
    main()

