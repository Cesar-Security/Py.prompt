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
    print("")
    #pasta que queremos organizar
    pasta= Path.home()/ "Downloads"
    #especificação dos arquivos
    categorias={
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documentos": [".pdf", ".doc",".docx", ".txt"],
    "Musicas": [".mp3", ".wav", ".flac"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Compactados": [".zip", ".rar",".7z"]
    }
    #percorre os arquivos da pasta dowloads
    for arquivo in pasta.iterdir():
        #verificar se não é um arquivo
        if not arquivo.is_file():
            continue
        #pega a extensao do arquivo e transforma em letras minusculas
        extensao= arquivo.suffix.lower()
        #se não tiver nenhuma categoria ele vai ficar em outros
        categoria= "outros"
        #percorre cada categoria e suas extensoes especificas
        for nome, extensoes in categorias.items():
            #verifica se as extensoes pertencem aquela categoria
            if extensao in extensoes:
                categoria = nome #guarda o nome da categoria
                break
        #cria o caminho para a pasta de destino
        destino= pasta / categoria
        #cria uma pasta caso nao exista
        destino.mkdir(exist_ok=True)
        #move o arquivo pra pasta
        shutil.move(str(arquivo), str(destino/arquivo.name))
        #informações finais
        print(f"{arquivo.name}--> {categoria}")
    print("organização completa")


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
