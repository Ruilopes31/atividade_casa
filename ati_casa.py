import os
os.system("cls || clear")
import time

biblioteca = []

def cadastrar_livro(titulo, autor):
    livro = {
        'titulo': titulo,
        'autor': autor,
        'status': 'disponível'
    }
    biblioteca.append(livro)
    print("Livro cadastrado com sucesso!")

def listar_livros():
    if len(biblioteca) == 0:
        print("Nenhum livro cadastrado ainda.")
    else:
        print("📚 Lista de livros cadastrados:\n")
        for i, livro in enumerate(biblioteca):
            print(f"Livro {i + 1}")
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Status: {livro['status']}")
            print("-----------------------------")

def buscar_livro(titulo_procurado):
    encontrado = False
    for livro in biblioteca:
        if livro['titulo'].lower() == titulo_procurado.lower():
            print("📖 Livro encontrado!")
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Status: {livro['status']}")
            encontrado = True
            break
    if not encontrado:
        print("Livro não encontrado.")

def alterar_status(titulo_procurado):
    encontrado = False
    for livro in biblioteca:
        if livro['titulo'].lower() == titulo_procurado.lower():
            encontrado = True
            if livro['status'] == 'disponível':
                livro['status'] = 'emprestado'
                print(f"O livro \"{livro['titulo']}\" foi emprestado com sucesso.")
            else:
                livro['status'] = 'disponível'
                print(f"O livro \"{livro['titulo']}\" foi devolvido e está disponível.")
            break
    if not encontrado:
        print("Livro não encontrado.\n")

while True:
    print("\n====== Sistema de Biblioteca ======")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Buscar livro")
    print("4. Emprestar/Devolver livro")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        cadastrar_livro(titulo, autor)

    elif opcao == "2":
        listar_livros()

    elif opcao == "3":
        titulo = input("Digite o título do livro para buscar: ")
        buscar_livro(titulo)

    elif opcao == "4":
        titulo = input("Digite o título do livro para alterar o status: ")
        alterar_status(titulo)

    elif opcao == "5":
        print("Saindo do sistema...")
        time.sleep(5)
        break

    else:
        print("Opção inválida! Tente novamente.")