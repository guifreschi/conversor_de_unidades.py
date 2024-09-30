from colorama import init, Fore, Back, Style
import os
import time
import temperature_converter as tc
import weight_converter as wc
import distance_converter as dc

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
                    
        
        # Conversor de Peso
        elif choice == 2:
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
        
        # Conversor de distância
        elif choice == 3:
            while True:
                clear_terminal()
                manner()
                print(Fore.GREEN + "[1] - Metro para Quilômetro\n[2] - Metro para Milha\n[3] - Metro para Pé\n[4] - Quilômetro para Metro\n[5] - Quilômetro para Milha\n[6] - Quilômetro para Pé\n[7] - Milha para Metro\n[8] - Milha para Quilômetro\n[9] - Milha para Pé\n[10] - Pé para Metro\n[11] - Pé para Quilômetro\n[12] - Pé para Milha")
                print(Fore.RED + "[13] - SAIR" + Style.RESET_ALL)
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
                    msg_manner("CONVERSOR METRO PARA QUILÔMETRO")
                    metro = float(input("Metros: "))
                    if metro > 0:
                        resultado = dc.meter_to_kilometer(metro)
                        print(f"{metro}m é {resultado:.2f}km.")
                        input("Dê Enter para continuar...")
                    else:
                        print(Fore.RED + "Número Inválido!" + Style.RESET_ALL)
                        time.sleep(0.5)
                    
                elif choice == 2:
                    clear_terminal()
                    manner()
                    msg_manner("CONVERSOR METRO PARA MILHA")
                    metro = float(input("Metros: "))
                    if metro > 0:
                        resultado = dc.meter_to_mile(metro)
                        print(f"{metro}m é {resultado:.2f}mi.")
                        input("Dê Enter para continuar...")
                    else:
                        print(Fore.RED + "Número Inválido!" + Style.RESET_ALL)
                        time.sleep(0.5)
                
                elif choice == 3:
                    clear_terminal()
                    manner()
                    msg_manner("CONVERSOR METRO PARA PÉ")
                    metro = float(input("Metro(s): "))
                    if metro > 0:
                        resultado = dc.meter_to_feet(metro)
                        print(f"{metro}m é {resultado:.2f}ft.")
                        input("Dê Enter para continuar...")
                    else:
                        print(Fore.RED + "Número Inválido!" + Style.RESET_ALL)
                        time.sleep(0.5)
                
                elif choice == 4:
                    clear_terminal()
                    manner()
                    msg_manner("CONVERSOR QUILÔMETRO PARA METRO")
                    quilometro = float(input("Quilômetro(s): "))
                    if quilometro > 0:
                        resultado = dc.kilometer_to_meter(quilometro)
                        print(f"{quilometro}km é {resultado:.2f}m.")
                        input("Dê Enter para continuar...")
                    else:
                        print(Fore.RED + "Número Inválido!" + Style.RESET_ALL)
                        time.sleep(0.5)
                
                elif choice == 5:
                    clear_terminal()
                    manner()
                    msg_manner("CONVERSOR QUILÔMETRO PARA MILHA")
                    quilometro = float(input("Quilômetro(s): "))
                    if quilometro > 0:
                        resultado = dc.kilometer_to_mile(quilometro)
                        print(f"{quilometro}km é {resultado:.2f}mi.")
                        input("Dê Enter para continuar...")
                    else:
                        print(Fore.RED + "Número Inválido!" + Style.RESET_ALL)
                        time.sleep(0.5)
                
                elif choice == 6:
                    clear_terminal()
                    manner()
                    msg_manner("CONVERSOR QUILÔMETRO PARA PÉ")
                    quilometro = float(input("Quilômetro(s): "))
                    if quilometro > 0:
                        resultado = dc.kilometer_to_feet(quilometro)
                        print(f"{quilometro}km é {resultado:.2f}ft.")
                        input("Dê Enter para continuar...")
                    else:
                        print(Fore.RED + "Número Inválido!" + Style.RESET_ALL)
                        time.sleep(0.5)
                
                elif choice == 7:
                    clear_terminal()
                    manner()
                    msg_manner("CONVERSOR MILHA PARA METRO")
                    milha = float(input("Milha(s): "))
                    if milha > 0:
                        resultado = dc.mile_to_meter(milha)
                        print(f"{milha}mi é {resultado:.2f}m.")
                        input("Dê Enter para continuar...")
                    else:
                        print(Fore.RED + "Número Inválido!" + Style.RESET_ALL)
                        time.sleep(0.5)
                
                elif choice == 8:
                    clear_terminal()
                    manner()
                    msg_manner("CONVERSOR MILHA PARA QUILÔMETRO")
                    milha = float(input("Milha(s): "))
                    if milha > 0:
                        resultado = dc.mile_to_kilometer(milha)
                        print(f"{milha}mi é {resultado:.2f}km.")
                        input("Dê Enter para continuar...")
                    else:
                        print(Fore.RED + "Número Inválido!" + Style.RESET_ALL)
                        time.sleep(0.5)
                
                elif choice == 9:
                    clear_terminal()
                    manner()
                    msg_manner("CONVERSOR MILHA PARA PÉ")
                    milha = float(input("Milha(s): "))
                    if milha > 0:
                        resultado = dc.mile_to_feet(milha)
                        print(f"{milha}mi é {resultado:.2f}ft.")
                        input("Dê Enter para continuar...")
                    else:
                        print(Fore.RED + "Número Inválido!" + Style.RESET_ALL)
                        time.sleep(0.5)
                
                elif choice == 10:
                    clear_terminal()
                    manner()
                    msg_manner("CONVERSOR PÉ PARA METRO")
                    pe = float(input("Pé(s): "))
                    if pe > 0:
                        resultado = dc.feet_to_meter(pe)
                        print(f"{pe}ft é {resultado:.2f}m.")
                        input("Dê Enter para continuar...")
                    else:
                        print(Fore.RED + "Número Inválido!" + Style.RESET_ALL)
                        time.sleep(0.5)
                
                elif choice == 11:
                    clear_terminal()
                    manner()
                    msg_manner("CONVERSOR PÉ PARA QUILÔMETRO")
                    pe = float(input("Pé(s): "))
                    if pe > 0:
                        resultado = dc.feet_to_kilometer(pe)
                        print(f"{pe}ft é {resultado:.2f}km.")
                        input("Dê Enter para continuar...")
                    else:
                        print(Fore.RED + "Número Inválido!" + Style.RESET_ALL)
                        time.sleep(0.5)
                
                elif choice == 12:
                    clear_terminal()
                    manner()
                    msg_manner("CONVERSOR PÉ PARA MILHA")
                    pe = float(input("Pé(s): "))
                    if pe > 0:
                        resultado = dc.feet_to_mile(pe)
                        print(f"{pe}ft é {resultado:.2f}mi.")
                        input("Dê Enter para continuar...")
                    else:
                        print(Fore.RED + "Número Inválido!" + Style.RESET_ALL)
                        time.sleep(0.5)
                
                elif choice == 13:
                    break
                
                else: 
                    if not incorrect_choice:
                        print(Fore.RED + "Número Inválido!" + Style.RESET_ALL)
                        time.sleep(0.5)
                    
            
        elif choice == 4:
            break
        
        else:
            if not incorrect_choice:
                print(Fore.RED + "Número Inválido!" + Style.RESET_ALL)
                time.sleep(0.5)
menu()
msg_manner("FIM!")