import criar_personagem_db
import dao_personagem
from time import sleep

def listar_editar(db):
    c = db.cursor()
    c.execute("SELECT * FROM mydb.personagem")
    lista_personagens = []
    for personagem in c:
        lista_personagens.append(criar_personagem_db.Personagem(personagem[0], personagem[1], personagem[3]))
    
    print("Personagens:")
    for i in range(len(lista_personagens)):
        print(f"[{i+1}] Nome:{lista_personagens[i].nome} | Pontos:{lista_personagens[i].pontos}")
    print("\nEscolha um personagem para editar | Sair [0]")
    opt = int(input("$ "))
    if opt > 0:
        if opt > len(lista_personagens):
            print("Opção Inválida, Tente Novamente")
            sleep(3)
        else:
            criar_personagem_db.menu_editacao(lista_personagens[opt-1], db)
    sleep(2)

def lista_remover(db):
    c = db.cursor()
    c.execute("SELECT * FROM mydb.personagem")
    lista_personagens = []
    for personagem in c:
        lista_personagens.append(criar_personagem_db.Personagem(personagem[0], personagem[1], personagem[3]))
    
    print("Personagens:")
    for i in range(len(lista_personagens)):
        print(f"[{i+1}] Nome:{lista_personagens[i].nome} | Pontos:{lista_personagens[i].pontos}")
    print("\nEscolha um personagem para remover | Sair [0]")
    opt = int(input("$ "))
    if opt > 0:
        dao_personagem.remover_personagem(lista_personagens[opt-1], db)
    sleep(2)