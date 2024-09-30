from colorama import init, Fore, Back, Style
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
        manner()
        print(Fore.GREEN + "[1] - Conversores de Temperatura\n[2] - Conversores de Peso\n[3] - Conversores de Distancia")
        print(Fore.RED + "[4] - SAIR" + Style.RESET_ALL)
        choice = str(input(">."))
        
        if choice.isnumeric():
            choice = int(choice)
        else:
            manner()
            print(Fore.RED + "Opção Inválida!" + Style.RESET_ALL)
            choice = 0
        
    
menu()