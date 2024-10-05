from colorama import init, Fore, Style
import os
import time
import operacoes.weight_converter_starter as wcs
import operacoes.distance_converter_starter as dcs
import operacoes.temperatute_converter_starter as tcs

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

def menu():
    while True:
        clear_terminal()
        manner()
        incorrect_choice = False
        print(Fore.GREEN + "[1] - Conversores de Temperatura\n[2] - Conversores de Peso\n[3] - Conversores de Distancia")
        print(Fore.RED + "[4] - SAIR" + Style.RESET_ALL)
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
        
        # Opções
        # Conversor de temperatura
        if choice == 1:
            tcs.temperature_converter()
                    
        
        # Conversor de Peso
        elif choice == 2:
            wcs.weight_converter()
            
        
        # Conversor de distância
        elif choice == 3:
            dcs.distance_converter()
                    
            
        elif choice == 4:
            break
        
        else:
            if not incorrect_choice:
                print(Fore.RED + "Número Inválido!" + Style.RESET_ALL)
                time.sleep(0.5)
menu()
msg_manner("FIM!")