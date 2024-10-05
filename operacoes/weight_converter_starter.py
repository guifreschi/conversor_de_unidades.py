from colorama import init, Fore, Style
import os
import time
import conversores.weight_converter as wc

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
init()

def manner():
    print("-=" * 25)
    
def end_manner():
    print("-=" * 25)
    print()
    
def msg_manner(msg):
    print(msg.center(50, '-'))


def weight_converter():
    while True:
        clear_terminal()
        manner()
        print(Fore.GREEN + "[1] - Grama para Quilograma\n[2] - Quilograma para Grama\n[3] - Quilograma para Libra\n[4] - Libra para Quilograma\n[5] - Grama para Libra\n[6] - Libra para Grama")
        print(Fore.RED + "[7] - SAIR" + Style.RESET_ALL)
        choice = str(input(">."))
        
        # Verifica se o usuário informou um número
        if choice.isnumeric():
            choice = int(choice)
            incorrect_choice = False
        else:
            print(Fore.RED + "Opção Inválida!" + Style.RESET_ALL)
            choice = 0
            incorrect_choice = True
            time.sleep(0.5)

    
        if choice == 1:
            clear_terminal()
            manner()
            msg_manner("CONVERSOR GRAMA PARA QUILOGRAMA")
            grama = float(input("Informe o peso em Grama para converter em Quilograma: "))
            resultado = wc.gram_to_kilogram(grama)
            print(f"{grama}g é {resultado:.2f}kg.")
            input("Dê Enter para continuar...")
            
            
        elif choice == 2:
            clear_terminal()
            manner()
            msg_manner("CONVERSOR QUILOGRAMA PARA GRAMA")
            quilograma = float(input("Informe o peso em Quilograma para converter em Grama: "))
            resultado = wc.kilogram_to_gram(quilograma)
            print(f"{quilograma}kg é {resultado:.2f}g.")
            input("Dê Enter para continuar...")
            
        elif choice == 3:
            clear_terminal()
            manner()
            msg_manner("CONVERSOR QUILOGRAMA PARA LIBRA")
            quilograma = float(input("Informe o peso em Quilograma para converter em Libra: "))
            resultado = wc.kilogram_to_pound(quilograma)
            print(f"{quilograma}kg é {resultado:.2f}lb.")
            input("Dê Enter para continuar...")
            
        elif choice == 4:
            clear_terminal()
            manner()
            msg_manner("CONVERSOR LIBRA PARA QUILOGRAMA")
            libra = float(input("Informe o peso em Libra para converter em Quilograma: "))
            resultado = wc.pound_to_kilogram(libra)
            print(f"{libra}lb é {resultado:.2f}kg.")
            input("Dê Enter para continuar...")
            
        elif choice == 5:
            clear_terminal()
            manner()
            msg_manner("CONVERSOR GRAMA PARA LIBRA")
            grama = float(input("Informe o peso em Grama para converter em Libra: "))
            resultado = wc.gram_to_pound(grama)
            print(f"{grama}g é {resultado:.2f}lb.")
            input("Dê Enter para continuar...")
            
        elif choice == 6:
            clear_terminal()
            manner()
            msg_manner("CONVERSOR LIBRA PARA GRAMA")
            libra = float(input("Informe o peso em Libra para converter em Grama: "))
            resultado = wc.pound_to_gram(libra)
            print(f"{libra}lb é {resultado:.2f}g.")
            input("Dê Enter para continuar...")
            
        elif choice == 7:
            break
        
        else:
            if not incorrect_choice:
                print(Fore.RED + "Número Inválido!" + Style.RESET_ALL)
                time.sleep(0.5)