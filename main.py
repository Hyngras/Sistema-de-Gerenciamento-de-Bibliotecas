from livro import Livro
from revista import Revista
from tese import Tese
from usuario import Usuario
from emprestimo import Emprestimo
from multa import Multa
from lista_espera import ListaEspera


def cadastrar_livro():
    # Implemente a lógica para cadastrar um livro
    titulo = input("Digite o título do livro: ")
    isbn = input("Digite o ISBN do livro: ")
    editora = input("Digite a editora do livro: ")
    ano_publicacao = input("Digite o ano de publicação do livro: ")
    autores = input("Digite os autores do livro (separados por vírgula): ").split(',')
    id_exemplar = input("Digite o identificador único do exemplar: ")

    livro = Livro(titulo, isbn, editora, ano_publicacao, autores, id_exemplar)
    # Adicione o livro à sua estrutura de dados (pode ser uma lista, dicionário, etc.)

def cadastrar_revista():
    # Implemente a lógica para cadastrar uma revista
    titulo = input("Digite o título da revista: ")
    issn = input("Digite o ISSN da revista: ")
    autor = input("Digite o autor da revista: ")
    editoras = input("Digite as editoras da revista (separadas por vírgula): ").split(',')
    ano = input("Digite o ano da revista: ")
    volume = input("Digite o volume da revista: ")
    id_exemplar = input("Digite o identificador único do exemplar: ")

    revista = Revista(titulo, issn, autor, editoras, ano, volume, id_exemplar)
    # Adicione a revista à sua estrutura de dados (pode ser uma lista, dicionário, etc.)

def cadastrar_tese():
    # Implemente a lógica para cadastrar uma tese
    titulo = input("Digite o título da tese: ")
    autor = input("Digite o autor da tese: ")
    programa_pos = input("Digite o programa de pós-graduação da tese: ")
    orientador = input("Digite o orientador da tese: ")
    co_orientador = input("Digite o co-orientador da tese: ")
    ano_publicacao = input("Digite o ano de publicação da tese: ")

    tese = Tese(titulo, autor, programa_pos, orientador, co_orientador, ano_publicacao)
    # Adicione a tese à sua estrutura de dados

def cadastrar_usuario():
    # Implemente a lógica para cadastrar um usuário
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o e-mail do usuário: ")
    telefone = input("Digite o telefone do usuário: ")
    # Adicione outros campos conforme necessário

    usuario = Usuario(nome, email, telefone)
    # Adicione o usuário à sua estrutura de dados

def realizar_emprestimo():
    # Implemente a lógica para realizar um empréstimo
    # Você precisará verificar a disponibilidade do item e atualizar as estruturas de dados
    usuario_nome = input("Digite o nome do usuário: ")
    livro_id_exemplar = input("Digite o id_exemplar do livro: ")

    usuario = encontrar_usuario_por_nome(usuario_nome)
    livro = encontrar_livro_por_id_exemplar(livro_id_exemplar)

    if usuario and livro and livro.disponivel:
        emprestimo = usuario.emprestar_livro(livro)
        if emprestimo:
            print(f"Empréstimo realizado com sucesso! Devolução até {emprestimo.data_devolucao}.")
        else:
            print("Usuário atingiu o limite de empréstimos.")
    else:
        print("Usuário não encontrado ou livro indisponível.")

def devolver_livro():
    usuario_nome = input("Digite o nome do usuário: ")
    livro_id_exemplar = input("Digite o id_exemplar do livro: ")

    usuario = encontrar_usuario_por_nome(usuario_nome)
    livro = encontrar_livro_por_id_exemplar(livro_id_exemplar)

    if usuario and livro:
        sucesso_devolucao = usuario.devolver_livro(livro_id_exemplar)
        if sucesso_devolucao:
            print("Devolução realizada com sucesso.")
        else:
            print("Empréstimo não encontrado na lista.")
    else:
        print("Usuário ou livro não encontrado.")

def pagar_multa():
    usuario_nome = input("Digite o nome do usuário: ")
    usuario = encontrar_usuario_por_nome(usuario_nome)

    if usuario:
        if usuario.multas:
            print("Multas do usuário:")
            for i, multa in enumerate(usuario.multas, start=1):
                print(f"{i}. Valor: R${multa.valor:.2f}, Data de Vencimento: {multa.data_pagamento}")
            
            multa_index = int(input("Digite o número da multa que deseja pagar (0 para sair): "))
            if multa_index > 0 and multa_index <= len(usuario.multas):
                sucesso_pagamento = usuario.pagar_multa(multa_index - 1)
                if sucesso_pagamento:
                    print("Multa paga com sucesso.")
                else:
                    print("Multa não encontrada ou já foi paga.")
            else:
                print("Opção inválida.")
        else:
            print("Usuário não possui multas.")
    else:
        print("Usuário não encontrado.")

def adicionar_a_lista_de_espera():
    usuario_nome = input("Digite o nome do usuário: ")
    livro_titulo = input("Digite o título do livro: ")

    usuario = encontrar_usuario_por_nome(usuario_nome)
    livro = encontrar_livro_por_titulo(livro_titulo)

    if usuario and livro and not livro.disponivel:
        lista_espera.adicionar_usuario_espera(livro_titulo, usuario_nome) #lista do banco de dados, importada no comeco
        print(f"{usuario_nome} adicionado à lista de espera para o livro {livro_titulo}.")
    else:
        print("Usuário não encontrado, livro não disponível ou ambos.")

# Funções auxiliares para encontrar usuário e livro (precisamos ter o banco de dados)
def encontrar_usuario_por_nome(nome):
    # Implemente a lógica para encontrar o usuário pelo nome
    #Algo como:
    '''for usuario in lista_de_usuarios:  # a lista de usuários sendo a base de dados
        if usuario.nome == nome:
            return usuario
    return None  # Retorna None se o usuário não for encontrado'''
    pass

def encontrar_livro_por_id_exemplar(id_exemplar):
    # Implemente a lógica para encontrar o livro pelo id_exemplar
    pass

def encontrar_livro_por_titulo(titulo):
    # Implemente a lógica para encontrar o livro pelo título
    pass

# Adicione as demais funções conforme necessário

def exibir_menu():
    print("==== Sistema de Gerenciamento de Bibliotecas ====")
    print("1. Cadastrar Livro")
    print("2. Cadastrar Revista")
    print("3. Cadastrar Tese")
    print("4. Cadastrar Usuário")
    print("5. Realizar Empréstimo")
    print("6. Devolver Livro")
    print("7. Pagar Multa")
    print("8. Adicionar à Lista de Espera")
    print("9. Sair")

def main():
    lista_espera = ListaEspera()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-9): ")

        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            cadastrar_revista()
            pass
        elif opcao == '3':
            cadastrar_tese()
            pass
        elif opcao == '4':
            cadastrar_usuario()
        elif opcao == '5':
            realizar_emprestimo()
        elif opcao == '6':
            devolver_livro()
            # Implemente a lógica para devolver uma revista e tese

            pass
        elif opcao == '7':
            pagar_multa()
            pass
        elif opcao == '8':
            adicionar_a_lista_de_espera()
            pass
        elif opcao == '9':
            print("Saindo do sistema. Até a próxima!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
