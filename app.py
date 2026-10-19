from colorama import Fore, Style #importa bibliotecas para cor e sorteio
from random import randint

#guarda variaveis importantes em ordem de criticalidade

cores = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE] 
estados = ["Muito baixo (crítico)!", "baixo", "médio", "alto", "Muito alto (alerta)"]

#retorna o nivel dependendo da porcentagem
def checar_situacao(porcentagem):
    if porcentagem <= 10:
        nivel = 1
    elif porcentagem <= 30:
        nivel = 2
    elif porcentagem <= 50:
        nivel = 3
    elif porcentagem <= 90:
        nivel = 4
    else:
        nivel = 5

    return nivel



#função que inicia o programa
def iniciar():
    
    quant_reservatiorios = randint(4, 15) #sorteia a quantidade de reservatorios para a simulação
    porc_dos_reservatorios = []

    for i in range(quant_reservatiorios):
        porc_dos_reservatorios.append(randint(0, 130)) #sorteia a quantidade de cada reservatorio


    for indice, porc in enumerate(porc_dos_reservatorios):  #em cada loop retorna a dupla ordenada com indice e o valor da lista
        nivel = checar_situacao(porc)
        print(f"{cores[nivel-1]}O estado do reservatório {indice+1} é {estados[nivel-1]}: {porc}%{Style.RESET_ALL}")
        

iniciar() #inicia o programa

