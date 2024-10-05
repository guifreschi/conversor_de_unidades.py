from colorama import init, Fore, Style
import os
import time
import conversores.temperature_converter as tc

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

def temperature_converter():
    while True:
            clear_terminal()
            manner()
            print(Fore.GREEN + "[1] - Celsius para Fahrenheit\n[2] - Fahrenheit para Celsius\n[3] - Kelvin para Fahrenheit\n[4] - Fahrenheit para Kelvin\n[5] - Celsius para Kelvin\n[6] - Kelvin para Celsius")
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
                
            # Opções para conversão de temperatura
            if choice == 1:
                clear_terminal()
                manner()
                msg_manner("CONVERSOR CELSIUS PARA FAHRENHEIT")
                celsius = float(input("Digite a temperatura em Celsius que deseja converter para Fahrenheit: "))
                resultado = tc.celsius_to_fahrenheit(celsius)
                print(f"{celsius} graus Celsius é {resultado:.2f} graus Fahrenheit!")
                input("Dê Enter para continuar...")
            
            elif choice == 2:
                clear_terminal()
                manner()
                msg_manner("CONVERSOR FAHRENHEIT PARA CELSIUS")
                fahrenheit = float(input("Digite a temperatura em Fahrenheit que deseja converter para Celsius: "))
                resultado = tc.fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit} graus Fahrenheit é {resultado:.2f} graus Celsius!")
                input("Dê Enter para continuar...")
            
            elif choice == 3:
                clear_terminal()
                manner()
                msg_manner("CONVERSOR KELVIN PARA FAHRENHEIT")
                kelvin = float(input("Digite a temperatura em Kelvin que deseja converter para Fahrenheit: "))
                resultado = tc.kelvin_to_fahrenheit(kelvin)
                print(f"{kelvin} graus Kelvin é {resultado:.2f} graus Fahrenheit!")
                input("Dê Enter para continuar...")
                
            elif choice == 4:
                clear_terminal()
                manner()
                msg_manner("CONVERSOR FAHRENHEIT PARA KELVIN")
                fahrenheit = float(input("Digite a temperatura em Fahrenheit que deseja converter para Kelvin: "))
                resultado = tc.fahrenheit_to_kelvin(fahrenheit)
                print(f"{fahrenheit} graus Fahrenheit é {resultado:.2f} graus Kelvin!")
                input("Dê Enter para continuar...")
            
            elif choice == 5:
                clear_terminal()
                manner()
                msg_manner("CONVERSOR CELSIUS PARA KELVIN")
                celsius = float(input("Digite a temperatura em Celsius que deseja converter para Kelvin: "))
                resultado = tc.celsius_to_kelvin(celsius)
                print(f"{celsius} graus Celsius é {resultado:.2f} graus Kelvin!")
                input("Dê Enter para continuar...")
            
            elif choice == 6:
                clear_terminal()
                manner()
                msg_manner("CONVERSOR KELVIN PARA CELSIUS")
                kelvin = float(input("Digite a temperatura em Kelvin que deseja converter para Celsius: "))
                resultado = tc.kelvin_to_celsius(kelvin)
                print(f"{kelvin} graus Kelvin é {resultado:.2f} graus Celsius!")
                input("Dê Enter para continuar...")
            
            elif choice == 7:
                break
                
            else:
                if not incorrect_choice:
                    print(Fore.RED + "Número Inválido!" + Style.RESET_ALL)
                    time.sleep(0.5)
