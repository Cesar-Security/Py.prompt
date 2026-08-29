from InquirerPy import inquirer
import os
import random
from pathlib import Path
import shutil
import json

ARQUIVOS_TAREFAS= "tarefas.json"
def ler_tarefas():
    if not os.path.exists(ARQUIVOS_TAREFAS):
        return []
    with open(ARQUIVOS_TAREFAS, "r") as arquivo:
        return json.load(arquivo)
def salvar_tarefas(tarefas):
    with open (ARQUIVOS_TAREFAS, "w") as arquivo:
        json.dump(tarefas, arquivo, indent= 4, ensure_ascii= False)
def inserir_tarefas(id_tarefa, nome_tarefa):
    tarefas= ler_tarefas()
    nova_tarefa={
        "id": id_tarefa,
        "tarefa": nome_tarefa,
        "concluida": False
    }
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print(f"Tarefa {nome_tarefa} inserido com sucesso")
def excluir_tarefa(id_tarefa):
    tarefas= ler_tarefas()
    tarefas_atualizadas= [t for t in tarefas if t["id"] != id_tarefa]
    if len(tarefas)== len(tarefas_atualizadas):
        print(f"Aviso: Nenhuma tarefa encontrada com o ID {id_tarefa}.")
    else:
        salvar_tarefas(tarefas_atualizadas)
        print(f"tarefa com ID {id_tarefa} excluida com sucesso!")







os.system("clear")

escolha= inquirer.select(
    message="escolha sua ação",
    choices=["organizador de arquivos", "pedra, papel e tesoura","lista de tarefas"]
).execute()

if escolha== "organizador de arquivos":
    
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
 

if escolha=="lista de tarefas":
    os.system("clear")

    es= inquirer.select(message="=== Menu de oções ===", choices= ["ler tarefa", "Criar uma tarefa", "Excluir/Concluir uma tarefa", "sair"]).execute()
    if es == "ler tarefa":
        tare= ler_tarefas()
        if not tare:
            print("nenhuma tarefa registrada")
            
        else: 
            for t in tare:
                status= "feito" if t["concluida"] else "nao feito"
                print(f"[{t['id']}] {t["tarefa"]}- status: {status}")


    if es == "Criar uma tarefa":
        a= input("diga sua tarefa: ")
        b= int(input("diga a posição dela: "))

        inserir_tarefas(b,a)
        print(f"tarefa {a} inserida com sucesso na posição {b}")

    if es == "Excluir/Concluir uma tarefa":
        c= int(input("escreva qual a posição dela: "))
        excluir_tarefa(c)
        print("exclusão feita")

    if es== "sair":
        print("projeto desenvolvido por: Antonio César")


