import mysql.connector
# from time import sleep # DEBUG
import dao_atributos
import dao_personagem
import dao_vantagens
import dao_desvantagens
import dao_pericias

class Personagem:
    def __init__(self, id, nome, pontos):
        self.id = id
        self.nome = nome
        self.pontos = pontos

class VantagemDesvantagem:
    def __init__(self, id, nome, valor, descricao):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.descricao = descricao
    
class Pericia:
    def __init__(self, id, nome, dificuldade, atributo, descricao):
        self.id = id
        self.nome = nome
        self.dificuldade = dificuldade
        self.atributo = atributo
        self.descricao = descricao

def criacao_inicial(mydb):
    print(chr(27) + "[2J")
    nome = input("Qual o nome do seu personagem?\n$ ")
    pontos = int(input("\nQuantos pontos terá o personagem?\n$ "))
    id = dao_personagem.get_id_personagens(mydb)
    personagem = Personagem(id, nome, pontos)
    dao_personagem.create_personagem(personagem, mydb)
    menu_editacao(personagem, mydb)

def menu_editacao(personagem, mydb):
    c = mydb.cursor()
    opt = -1
    # Create lista_vantagens
    c.execute("SELECT * FROM vantagens")
    lista_vantagens = []
    for vantagem in c:
        lista_vantagens.append(VantagemDesvantagem(vantagem[0], vantagem[1], int(vantagem[3]), vantagem[2]))
    # Create lista_desvantagens
    c.execute("SELECT * FROM desvantagens")
    lista_desvantagens = []
    for desvantagem in c:
        lista_desvantagens.append(VantagemDesvantagem(desvantagem[0], desvantagem[1], int(desvantagem[3]), desvantagem[2]))
    # Create lista_pericias
    c.execute("SELECT * FROM pericias")
    lista_pericias = []
    for pericia in c:
        lista_pericias.append(Pericia(pericia[0], pericia[1], pericia[2], pericia[3], pericia[4]))
    while opt != 0:
        print(chr(27) + "[2J")
        print(f"""
        Personagem: {personagem.nome}
    Pontos para utilizar: {dao_personagem.get_pontos(personagem, mydb)}
 Força:    {dao_atributos.get_for(personagem, mydb)} | Inteligencia: {dao_atributos.get_int(personagem, mydb)}
 Destreza: {dao_atributos.get_des(personagem, mydb)} | Vitalidade:   {dao_atributos.get_vit(personagem, mydb)}
        """)
        #Criar for loops para listar Vantagens, Desvantagens e Perícias
        # if len(lista_vantagens) > 0:
        #     print("Vantagens:")
        #     for v in lista_vantagens:
        #         print(f"* {v.nome()}")
        # if len(lista_desvantagens) > 0:
        #     print("Desvantagens:")
        #     for d in lista_desvantagens:
        #         print(f"* {d.nome()}")
        print("""
1 - Modificar Atributos
2 - Adicionar/Remover Vantagens
3 - Adicionar/Remover Desvantagens
4 - Adicionar/Remover Pericia

0 - Finalizar
        """)
        opt = int(input("$ "))
        if opt == 1:
            menu_atributos(personagem, mydb)
            pass
        elif opt == 2:
            menu_vantagens(lista_vantagens, personagem, mydb)
        elif opt == 3:
            menu_desvantagens(lista_desvantagens, personagem, mydb)
        elif opt == 4:
            menu_pericias(lista_pericias, personagem, mydb)
        elif opt == 0:
            pass
        else:
            print("Opção inválido!")
    

def menu_atributos(per, bd):
    forca_preco = dao_atributos.get_for_val(bd)
    vitalidade_preco = dao_atributos.get_vit_val(bd)
    destreza_preco = dao_atributos.get_des_val(bd)
    inteligencia_preco = dao_atributos.get_int_val(bd)
    opt = -1
    while opt != 0:
        print(chr(27) + "[2J")
        print(f"""
        Pontos para utilizar: {dao_personagem.get_pontos(per, bd)}
    +[1] {forca_preco} | Força:        {dao_atributos.get_for(per, bd)} | -[2] -{forca_preco}
    +[3] {destreza_preco} | Destreza:     {dao_atributos.get_des(per, bd)} | -[4] -{destreza_preco}
    +[5] {inteligencia_preco} | Inteligencia: {dao_atributos.get_int(per, bd)} | -[6] -{inteligencia_preco}
    +[7] {vitalidade_preco} | Vitalidade:   {dao_atributos.get_vit(per, bd)} | -[8] -{vitalidade_preco}
            
            0 - Finalizar
        """)
        opt = int(input("       $ "))
        if opt == 1:
            dao_atributos.update_melhoria_pontos_for(per, bd)
        elif opt == 2:
            dao_atributos.update_diminuicao_pontos_for(per, bd)
        elif opt == 3:
            dao_atributos.update_melhoria_pontos_des(per, bd)
        elif opt == 4:
            dao_atributos.update_diminuicao_pontos_des(per, bd)
        elif opt == 5:
            dao_atributos.update_melhoria_pontos_int(per, bd)
        elif opt == 6:
            dao_atributos.update_diminuicao_pontos_int(per, bd)
        elif opt == 7:
            dao_atributos.update_melhoria_pontos_vit(per, bd)
        elif opt == 8:
            dao_atributos.update_diminuicao_pontos_vit(per, bd)
        elif opt == 0:
            pass
        else:
            print("Opção inválido!")

def menu_vantagens(lista_vantagens, per, bd):
    opt = -1
    s = 0 # Inicio parte da lista
    e = 4 # Final parte da lista
    while True:
        print(chr(27) + "[2J")
        # print(f"Arquivo: {header.group(1)}") # Verificar como pegar o nome de arquivo (NÃO É NECESSÁRIO PARA O TRABALHO, SÓ FICARIA LEGAL)
        print(f"Pontos: {dao_personagem.get_pontos(per, bd)}")
        if e > len(lista_vantagens):
            s -= e - len(lista_vantagens)
            e = len(lista_vantagens)
        for v in range(s, e):
            if dao_vantagens.get_comprado(per, lista_vantagens[v], bd) == 1:
                print(f"[{lista_vantagens[v].id}] {lista_vantagens[v].nome} - {lista_vantagens[v].valor} Pontos - Ja adquirido!")
            else:
                print(f"[{lista_vantagens[v].id}] {lista_vantagens[v].nome} - {lista_vantagens[v].valor} Pontos")
        if s == 0:
            print("\nPróxima Página [>]")
        else:
            print("\n[<] Página Anterior | Próxima Página [>]")
        print("\n[0] Finalizar")
        opt = input("\n$ ")
        if opt == "<" and s != 0:
            s -= 4
            e -= 4
        elif opt == ">":
            s += 4
            e += 4
        else:
            opt = int(opt)
            if opt == 0:
                break
            else:
                vantagem_selecionado = lista_vantagens[opt-1]
                print(chr(27) + "[2J")
                print(f"Vantagem: {vantagem_selecionado.nome}\nDescrição: {vantagem_selecionado.descricao}")
                vantagem_opt = input(f"\nDeseja comprar essa vantagem por {vantagem_selecionado.valor}? s/n: ")
                if vantagem_opt.lower() == "s": # Verificar se ja tem a pericia
                    dao_vantagens.comprar(per, vantagem_selecionado, bd)
                    # pass
                else:
                    pass

def menu_desvantagens(lista_desvantagens, per, bd):
    opt = -1
    s = 0 # Inicio parte da lista
    e = 4 # Final parte da lista
    while True:
        print(chr(27) + "[2J")
        # print(f"Arquivo: {header.group(1)}") # Verificar como pegar o nome de arquivo (NÃO É NECESSÁRIO PARA O TRABALHO, SÓ FICARIA LEGAL)
        print(f"Pontos: {dao_personagem.get_pontos(per, bd)}")
        if e > len(lista_desvantagens):
            s -= e - len(lista_desvantagens)
            e = len(lista_desvantagens)
        for d in range(s, e):
            if dao_desvantagens.get_comprado(per, lista_desvantagens[d], bd) == 1:
                print(f"[{lista_desvantagens[d].id}] {lista_desvantagens[d].nome} - +{lista_desvantagens[d].valor} Pontos - Ja adquirido!")
            else:
                print(f"[{lista_desvantagens[d].id}] {lista_desvantagens[d].nome} - +{lista_desvantagens[d].valor} Pontos")
        if s == 0:
            print("\nPróxima Página [>]")
        else:
            print("\n[<] Página Anterior | Próxima Página [>]")
        print("\n[0] Finalizar")
        opt = input("\n$ ")
        if opt == "<" and s != 0:
            s -= 4
            e -= 4
        elif opt == ">":
            s += 4
            e += 4
        else:
            opt = int(opt)
            if opt == 0:
                break
            else: 
                desvantagem_selecionado = lista_desvantagens[opt-1]
                print(chr(27) + "[2J")
                print(f"Desvantagem: {desvantagem_selecionado.nome}\nDescrição: {desvantagem_selecionado.descricao}")
                desvantagem_opt = input(f"\nDeseja receber {desvantagem_selecionado.valor} por essa desvantagem? s/n: ")
                if desvantagem_opt.lower() == "s": # Verificar se ja tem a pericia
                    dao_desvantagens.comprar(per, desvantagem_selecionado, bd)
                else:
                    pass

def menu_pericias(lista_pericias, per, bd):
    # Dicionários para Dificuldade e Atributo
    atributo = {
        1:"Força",
        2:"Destreza",
        3:"Inteligência",
        4:"Vitalidade"
    }
    dificuldade = {
        1:"Fácil",
        2:"Médio",
        3:"Difícil"
    }
    pontos = 0
    opt = -1
    s = 0 # Inicio parte da lista
    e = 4 # Final parte da lista
    while True:
        print(chr(27) + "[2J")
        print(f"Pontos: {dao_personagem.get_pontos(per, bd)}")
        if e > len(lista_pericias):
            s -= e - len(lista_pericias)
            e = len(lista_pericias)
        for p in range(s, e):
            pontos = dao_pericias.get_pontos_gastos(per, lista_pericias[p], bd)
            if pontos > 0:
                print(f"[{lista_pericias[p].id}] {lista_pericias[p].nome} - {atributo[lista_pericias[p].atributo]}/{dificuldade[lista_pericias[p].dificuldade]} | {pericia_calc(lista_pericias[p], pontos)} ({pontos})")
            else:
                print(f"[{lista_pericias[p].id}] {lista_pericias[p].nome} - {atributo[lista_pericias[p].atributo]}/{dificuldade[lista_pericias[p].dificuldade]}")
        if s == 0:
            print("\nPróxima Página [>]")
        else:
            print("\n[<] Página Anterior | Próxima Página [>]")
        print("\n[0] Finalizar")
        opt = input("\n$ ")
        if opt == "<" and s != 0:
            s -= 4
            e -= 4
        elif opt == ">":
            s += 4
            e += 4
        else:
            opt = int(opt)
            if opt == 0:
                break
            else:
                while True:
                    pericia_selecionado = lista_pericias[opt-1]
                    pontos = dao_pericias.get_pontos_gastos(per, pericia_selecionado, bd)
                    print(chr(27) + "[2J")
                    print(f"Pontos Personagem: {dao_personagem.get_pontos(per, bd)}")
                    print(f"Pericia: {pericia_selecionado.nome}\nDescrição: {pericia_selecionado.descricao}")
                    print(f"Pontos Gastados: ({pontos}) {pericia_calc(pericia_selecionado, pontos)}" )
                    if pontos > 0:
                        print("\n[-] Diminuir | Melhorar [+]")
                    else:
                        print("\n Melhorar [+]")
                    print("\n[0] Finalizar")
                    pericia_opt = input(f"\n$ ")

                    if pericia_opt == "-" and pontos != 0:
                        pericia_diminuir(per, pericia_selecionado, pontos, bd)
                    elif pericia_opt == "+":
                        pericia_melhorar(per, pericia_selecionado, pontos, bd)
                    else:
                        break

def pericia_calc(peri, pontos):
    atributo = {
        1:"Força",
        2:"Destreza",
        3:"Inteligência",
        4:"Vitalidade"
    }
    # Tabela Fácil
    if peri.dificuldade == 1:
        if pontos == 0:
            return f"{atributo[peri.atributo]}-1"
        elif pontos == 1:
            return f"{atributo[peri.atributo]}+0"
        elif pontos == 2:
            return f"{atributo[peri.atributo]}+1"
        elif pontos == 4:
            return f"{atributo[peri.atributo]}+2"
        else:
            return f"{atributo[peri.atributo]}+{int(pontos / 4 + 1)}"
    # Tabela Médio
    elif peri.dificuldade == 2:
        if pontos == 0:
            return f"{atributo[peri.atributo]}-2"
        elif pontos == 1:
            return f"{atributo[peri.atributo]}-1"
        elif pontos == 2:
            return f"{atributo[peri.atributo]}+0"
        elif pontos == 4:
            return f"{atributo[peri.atributo]}+1"
        else:
            return f"{atributo[peri.atributo]}+{int(pontos / 4)}"
    # Tabela Difícil
    elif peri.dificuldade == 3:
        if pontos == 0:
            return f"{atributo[peri.atributo]}-3"
        elif pontos == 1:
            return f"{atributo[peri.atributo]}-2"
        elif pontos == 2:
            return f"{atributo[peri.atributo]}-1"
        elif pontos == 4:
            return f"{atributo[peri.atributo]}+0"
        else:
            return f"{atributo[peri.atributo]}+{int(pontos / 4 - 1)}"
    else:
        return "ERROR"

def pericia_melhorar(pers, peri, pontos, db):
    if pontos == 0:
        dao_pericias.alterar_pontos(pers, peri, pontos+1, 1, db)
    elif pontos == 1:
        dao_pericias.alterar_pontos(pers, peri, pontos+1, 1, db)
    elif pontos == 2:
        dao_pericias.alterar_pontos(pers, peri, pontos+2, 2, db)
    else:
        dao_pericias.alterar_pontos(pers, peri, pontos+4, 4, db)

def pericia_diminuir(pers, peri, pontos, db):
    if pontos == 1:
        dao_pericias.alterar_pontos(pers, peri, pontos-1, 1, db)
    elif pontos == 2:
        dao_pericias.alterar_pontos(pers, peri, pontos-1, 1, db)
    elif pontos == 4:
        dao_pericias.alterar_pontos(pers, peri, pontos-2, 2, db)
    else:
        dao_pericias.alterar_pontos(pers, peri, pontos-4, 4, db)