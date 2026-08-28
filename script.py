from InquirerPy import inquirer
import os
import random
from pathlib import Path
import shutil


escolha= inquirer.select(
    message="escolha sua ação",
    choices=["organizador de arquivos", "pedra, papel e tesoura","revisar o clima"]
).execute()



if escolha== "organizador de arquivos":
    print("org. de arqui.")

if escolha=="pedra, papel e tesoura":
    #comando limpar terminal do linux
    os.system("clear")
    jogo= inquirer.select(
    #definindo a seleção dos valores
    message= "escolha",
    choices=["pedra", "papel", "tesoura"],
    pointer= "*"
    ).execute()
    ebot= ["pedra", "papel", "tesoura"]
    bot= random.choice(ebot)

    if jogo in bot:
        print("empate")
        #se o jogo empatar ele irá escrever empate
    else:
        if jogo=="pedra" and bot == "tesoura" or jogo=="papel" and bot == "pedra" or jogo=="tesoura" and bot == "papel":
            print(f"voce ganhou. voce jogou {jogo} e o bot jogou {bot}")
            #se o jogador ganhar ele imprime essa frase
        else:
            print(f"voce perdeu. voce jogou {jogo} e o bot jogou {bot}") 
            # se ele perder ele printa o voce perdeu 
 

if escolha=="revisar o clima":
    print("r. clima")
