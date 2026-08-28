from InquirerPy import inquirer

escolha= inquirer.select(
    message="escolha sua ação",
    choices=["organizador de arquivos", "pedra, papel e tesoura","revisar o clima"]
).execute()

