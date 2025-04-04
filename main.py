from pathlib import Path
import os

def get_folder():
    origin_folder = input("\nDigite o caminho completo da pasta que vai ter os arquivos renomeados:\n")
    path_folder = Path(origin_folder)
    if not path_folder.exists() or not path_folder.is_dir():
        print("Caminho inválido. Verifique se a pasta existe.")
        return None
    elif not any(path_folder.iterdir()):
        print("A pasta está vazia!")
        return None
    return path_folder

def naming_options():
    
    count = False
    prefix = ""
    suffix = ""
    
    while True:
        print("\nO que você deseja adicionar ao nome dos arquivos?")
        print("1 - Contagem")
        print("2 - Prefixo")
        print("3 - Sufixo")
        print("4 - Enviar.")
        
        try:
            choice = int(input("> "))
        except ValueError:
            print("\nEntrada deve ser um número.")
            continue
        
        if choice == 1:
            count = True
            print("\nContagem será adicionada!")
        elif choice == 2:
            prefix = input("\nQual prefixo você deseja adicionar?\n")
        elif choice == 3:
            suffix = input("\nQual o sufixo você deseja adicionar?\n")
        elif choice == 4:
            break
        else:
            print("Opção inválida.")
        
    return count, prefix, suffix

def renaming_files():
    origin_folder = get_folder()
    if not origin_folder:
        return
    count, prefix, suffix = naming_options()
    counter = 1
    
    files = [file for file in origin_folder.iterdir() if file.is_file()]
    
    for file in files:
        old_name = file.parent / file.name
        extension = file.suffix
        if count == True:
            new_name = file.parent / f"{counter} - {prefix}_{file.stem}_{suffix}{extension}"
            counter += 1
        else:
            new_name = file.parent / f"{prefix}_{file.stem}_{suffix}{extension}"    
        os.rename(old_name, new_name)
                
    print("Arquivos renomeados com sucesso!")