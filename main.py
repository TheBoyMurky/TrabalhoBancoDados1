#! /usr/bin/env python3

from pyfiglet import Figlet
from time import sleep
# import criar_personagem # Caso dê merda no BD
import criar_personagem_db
import listar_personagem_db
import import_files
import mysql.connector

f = Figlet(font='slant')
opt = -1
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123",
        database="mydb"
    )

while opt != 0:
    print(chr(27) + "[2J")
    print(f.renderText('PyGURPS'))

    arquivos_restantes = import_files.verify_import()

    print("""
        1. Criar Personagem novo
        2. Personagens Criados
        3. Importar Personagem --TODO
        4. Exportar Personagem --TODO
        5. Remover Personagem
        6. Gerar NPC --TODO
        7. Importar Arquivos em "read_files"
        0. Sair""")
    try:
        opt = int(input("\n\t$ "))
    except ValueError:
        pass
    #Pq python não tem um switch :(
    if opt == 1:
        criar_personagem_db.criacao_inicial(mydb)
    elif opt == 2:
        listar_personagem_db.listar_editar(mydb)
    # elif opt == 3:
    #     print("\tAinda não implementado")
    # elif opt == 4:
    #     print("\tAinda não implementado")
    elif opt == 5:
        listar_personagem_db.lista_remover(mydb)
    elif opt == 6:
        print("\tAinda não implementado")
    elif opt == 7:
        import_files.import_all()
    elif opt == 0:
        print(chr(27) + "[2J")
        pass
    else:
        print("\tOpção inválido, tente novamente")
    sleep(2)