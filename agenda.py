contatos = []

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    contatos.append(contato)

    print("\nContato adicionado com sucesso!\n")


def listar_contatos():
    if len(contatos) == 0:
        print("\nNenhum contato cadastrado.\n")
        return

    print("\nLISTA DE CONTATOS\n")

    for i, contato in enumerate(contatos, start=1):
        print(f"{i}. Nome: {contato['nome']}")
        print(f"   Telefone: {contato['telefone']}")
        print(f"   Email: {contato['email']}")
        print("-" * 30)


def remover_contato():
    listar_contatos()

    if len(contatos) == 0:
        return

    indice = int(input("Digite o número do contato para remover: "))

    if 1 <= indice <= len(contatos):
        removido = contatos.pop(indice - 1)
        print(f"\nContato '{removido['nome']}' removido.\n")
    else:
        print("\nNúmero inválido.\n")


while True:
    print("===== AGENDA =====")
    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Remover")
    print("4 - Sair")

    opcao = input("\nEscolha: ")

    if opcao == "1":
        adicionar_contato()

    elif opcao == "2":
        listar_contatos()

    elif opcao == "3":
        remover_contato()

    elif opcao == "4":
        print("\nPrograma encerrado.")
        break

    else:
        print("\nOpção inválida.\n")