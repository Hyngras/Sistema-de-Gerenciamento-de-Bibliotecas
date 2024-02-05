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

    livro = Livro(titulo, isbn, editora, ano_publicacao, autores)
    # Adicione o livro à sua estrutura de dados (pode ser uma lista, dicionário, etc.)

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
            # Implemente a lógica para cadastrar uma revista
            pass
        elif opcao == '3':
            # Implemente a lógica para cadastrar uma tese
            pass
        elif opcao == '4':
            cadastrar_usuario()
        elif opcao == '5':
            realizar_emprestimo()
        elif opcao == '6':
            # Implemente a lógica para devolver um livro
            pass
        elif opcao == '7':
            # Implemente a lógica para pagar uma multa
            pass
        elif opcao == '8':
            # Implemente a lógica para adicionar à lista de espera
            pass
        elif opcao == '9':
            print("Saindo do sistema. Até a próxima!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
