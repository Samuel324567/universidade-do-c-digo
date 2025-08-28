def mostrar_menu():
    print()
    print("==== MENU ====")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Sair")
    print("==============")

while True:
    mostrar_menu()
    op = input("Opção: ")

    if op == "1":
        print("Cadastrar escolhido\n")
        # chama função cadastro
    elif op == "2":
        print("Listar escolhido\n")
        # chama função listar
    elif op == "3":
        print("Atualizar escolhido\n")
        # chama função atualizar
    elif op == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida\n")
