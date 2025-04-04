from main import get_folder, naming_options, renaming_files

while True:
    print("1 - Renomear arquivos.")
    print("2 - Sair.")
    
    try:
        choice = int(input("> "))
    except ValueError:
        print("Entrada deve ser um número.")
        continue
    
    match choice:
        case 1:
            renaming_files()
        case 2:
            print("Saindo!")
            break
        case _:
            print("Opção inválida.")
            continue