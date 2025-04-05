from main import renaming_files

while True:
    print("\n1 - Renomear arquivos.")
    print("2 - Sair.")
    
    try:
        choice = int(input("> "))
    except ValueError:
        print("Entrada deve ser um número.")
        pass
    
    match choice:
        case 1:
            try:
                renaming_files()
            except OSError as e:
                print(f"Erro ao renomear arquivos: {e.strerror}")
        case 2:
            print("Saindo!")
            break
        case _:
            print("Opção inválida.")
            continue