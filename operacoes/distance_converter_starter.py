from colorama import init, Fore, Style
import os
import time
import conversores.distance_converter as dc

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


def distance_converter():
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

