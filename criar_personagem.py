import re

class VantagemDesvantagem:
    def __init__(self, id, nome, custo, descricao):
        self.id = id
        self.nome = nome
        self.custo = custo
        self.descricao = descricao
    
    def get_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome
    
    def get_custo(self):
        return self.custo

    def get_descricao(self):
        return self.descricao

def menu_criacao():
    print(chr(27) + "[2J")
    nome = input("Qual o nome do seu personagem?\n$ ")
    pontos = int(input("\nQuantos pontos terá o personagem?\n$ "))
    atributos = [10, 10, 10, 10] #Força, Destreza, Inteligencia e Vitalidade
    vantagens = []
    desvantagens = []
    pericias = []
    opt = -1
    while opt != 0:
        print(chr(27) + "[2J")
        print(f"""
        Personagem: {nome}
    Pontos para utilizar: {pontos}
Força:    {atributos[0]} | Inteligencia: {atributos[2]}
Destreza: {atributos[1]} | Vitalidade:   {atributos[3]}
        """)
        #Criar for loops para listar Vantagens, Desvantagens e Perícias
        if len(vantagens) > 0:
            print("Vantagens:")
            for v in vantagens:
                print(f"* {v.get_nome()}")
        if len(desvantagens) > 0:
            print("Desvantagens:")
            for d in desvantagens:
                print(f"* {d.get_nome()}")
        print("""
1 - Modificar Atributos
2 - Adicionar/Remover Vantagens
3 - Adicionar/Remover Desvantagens
4 - Adicionar/Remover Pericia

0 - Finalizar
        """)
        opt = int(input("$ "))
        if opt == 1:
            pontos = menu_atributos(pontos, atributos)
        elif opt == 2:
            pontos = menu_vantagens(pontos, vantagens)
        elif opt == 3:
            pontos = menu_desvantagens(pontos, desvantagens)
        elif opt == 0:
            pass
        else:
            print("Opção inválido!")
    

def menu_atributos(pontos, atributos):
    forca_preco = vitalidade_preco = 10
    destreza_preco = inteligencia_preco = 20
    opt = -1
    while opt != 0:
        print(chr(27) + "[2J")
        print(f"""
        Pontos para utilizar: {pontos}
    +[1] {forca_preco} | Força: {atributos[0]}        | -[2] -{forca_preco}
    +[3] {destreza_preco} | Destreza: {atributos[1]}     | -[4] -{destreza_preco}
    +[5] {inteligencia_preco} | Inteligencia: {atributos[2]} | -[6] -{inteligencia_preco}
    +[7] {vitalidade_preco} | Vitalidade: {atributos[3]}   | -[8] -{vitalidade_preco}
            
            0 - Finalizar
        """)
        opt = int(input("       $ "))
        if opt == 1:
            pontos -= forca_preco
            atributos[0] += 1
        elif opt == 2:
            pontos += forca_preco
            atributos[0] -= 1
        elif opt == 3:
            pontos -= destreza_preco
            atributos[1] += 1
        elif opt == 4:
            pontos += destreza_preco
            atributos[1] -= 1
        elif opt == 5:
            pontos -= inteligencia_preco
            atributos[2] += 1
        elif opt == 6:
            pontos += inteligencia_preco
            atributos[2] -= 1
        elif opt == 7:
            pontos -= vitalidade_preco
            atributos[3] += 1
        elif opt == 8:
            pontos += vitalidade_preco
            atributos[3] -= 1
        elif opt == 0:
            pass
        else:
            print("Opção inválido!")
    
    return pontos

def menu_vantagens(pontos, vantagens):
    
    # Patters
    header_pattern = "(.*)(\d\d\d)(\d\d\d)"
    vantagem_pattern = "(.*)(\d\d\d)(\d\d\d)(.*)"
    # File
    arquivo_vantagens = open("read_files/vantagens.txt", "r")
    # Lista com vantagens lidas do arquivo
    lista_vantagens = []
    # Variáveis de loop
    opt = -1
    arquivo_nome = ""
    linha = arquivo_vantagens.readline()
    arquivo_leitura = arquivo_vantagens.read()
    header = re.search(header_pattern, linha)
    vantagens_encontrados = re.findall(vantagem_pattern, arquivo_leitura)
    
    for vantagem in vantagens_encontrados:
        lista_vantagens.append(VantagemDesvantagem(int(vantagem[2]), vantagem[0], int(vantagem[1]), vantagem[3]))
    
    s = 0 # Inicio parte da lista
    e = 4 # Final parte da lista
    while True:
        print(chr(27) + "[2J")
        print(f"Arquivo: {header.group(1)}")
        print(f"Pontos: {pontos}")
        if e > len(lista_vantagens):
            s -= e - len(lista_vantagens)
            e = len(lista_vantagens)
        for v in range(s, e):
            if lista_vantagens[v] in vantagens:
                print(f"[{lista_vantagens[v].get_id()}] {lista_vantagens[v].get_nome()} - {lista_vantagens[v].get_custo()} Pontos - Ja adquirido!")
            else:
                print(f"[{lista_vantagens[v].get_id()}] {lista_vantagens[v].get_nome()} - {lista_vantagens[v].get_custo()} Pontos")
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
                print(f"Vantagem: {vantagem_selecionado.get_nome()}\nDescrição: {vantagem_selecionado.get_descricao()}")
                vantagem_opt = input("\nDeseja selecionar essa vantagem? s/n: ")
                if vantagem_opt.lower() == "s":
                    pontos -= vantagem_selecionado.get_custo()
                    vantagens.append(vantagem_selecionado)
                else:
                    pass

    arquivo_vantagens.close()
    return pontos


def menu_desvantagens(pontos, desvantagens):
    # Patters
    header_pattern = "(.*)(\d\d\d)(\d\d\d)"
    desvantagem_pattern = "(.*)(\d\d\d)(\d\d\d)(.*)"
    # File
    arquivo_desvantagens = open("read_files/desvantagens.txt", "r")
    # Lista com desvantagens lidos do arquivo
    lista_desvantagens = []
    # Variáveis de loop
    opt = -1
    arquivo_nome = ""
    linha = arquivo_desvantagens.readline()
    arquivo_leitura = arquivo_desvantagens.read()
    header = re.search(header_pattern, linha)
    desvantagens_encontrados = re.findall(desvantagem_pattern, arquivo_leitura)
    
    for desvantagem in desvantagens_encontrados:
        lista_desvantagens.append(VantagemDesvantagem(int(desvantagem[2]), desvantagem[0], int(desvantagem[1]), desvantagem[3]))
    
    s = 0 # Inicio parte da lista
    e = 4 # Final parte da lista
    while True:
        print(chr(27) + "[2J")
        print(f"Arquivo: {header.group(1)}")
        print(f"Pontos: {pontos}")
        if e > len(lista_desvantagens):
            s -= e - len(lista_desvantagens)
            e -=  e - len(lista_desvantagens)
        if s < 0:
            s = 0
        for v in range(s, e):
            if lista_desvantagens[v] in desvantagens:
                print(f"[{lista_desvantagens[v].get_id()}] {lista_desvantagens[v].get_nome()} - +{lista_desvantagens[v].get_custo()} Pontos - Ja adquirido!")
            else:
                print(f"[{lista_desvantagens[v].get_id()}] {lista_desvantagens[v].get_nome()} - +{lista_desvantagens[v].get_custo()} Pontos")
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
                print(f"Vantagem: {desvantagem_selecionado.get_nome()}\nDescrição: {desvantagem_selecionado.get_descricao()}")
                desvantagem_opt = input("\nDeseja selecionar essa vantagem? s/n: ")
                if desvantagem_opt.lower() == "s":
                    pontos += desvantagem_selecionado.get_custo()
                    desvantagens.append(desvantagem_selecionado)
                else:
                    pass

    arquivo_desvantagens.close()
    return pontos