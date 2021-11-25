from colorama.ansi import Cursor
import mysql.connector
import re
from colorama import Fore, Style

def verify_import():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="mydb"
  )
  if mydb.is_connected():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM atributos")
    resultado = cursor.fetchall()
    if not resultado:
      print(Fore.RED + "Não foram importados arquivos recentemente")
      print(Style.RESET_ALL)
      cursor.close()
      mydb.close()
      return False
    return True


def import_atributes(db):
  if db.is_connected():
    cursor = db.cursor()
    # Inserindo valores padrões dentro do DB
    cursor.execute("INSERT INTO atributos (nome_atributo, valor_atributo) VALUES ('Força', 10)")
    cursor.execute("INSERT INTO atributos (nome_atributo, valor_atributo) VALUES ('Destreza', 20)")
    cursor.execute("INSERT INTO atributos (nome_atributo, valor_atributo) VALUES ('Inteligência', 20)")
    cursor.execute("INSERT INTO atributos (nome_atributo, valor_atributo) VALUES ('Vitalidade', 10)")
    # cursor.execute("SELECT valor_atributo FROM atributos WHERE nome_atributo = 'Força'")
    # print(cursor.fetchone()[0])
    cursor.close()
    
def import_vantagens(db):
  # Patters
  vantagem_pattern = "(.*)(\d\d\d)(.*)"
  # File
  arquivo_vantagens = open("read_files/vantagens.txt", "r")
  arquivo_leitura = arquivo_vantagens.read()
  arquivo_vantagens.close()
  vantagens_encontrados = re.findall(vantagem_pattern, arquivo_leitura)
  cursor = db.cursor()  
  for vantagem in vantagens_encontrados:
    nome_vantagem = vantagem[0].strip()
    descricao = vantagem[2].strip()
    valor_vantagem = int(vantagem[1])
    # print(descricao, len(descricao))
    cursor.execute("INSERT INTO vantagens (nome_vantagem, descricao, valor_vantagem) VALUES (%s, %s, %s)", (nome_vantagem, descricao, valor_vantagem))
  cursor.close()

def import_desvantagens(db):
  # Patters
  desvantagem_pattern = "(.*)(\d\d\d)(.*)"
  # File
  arquivo_desvantagens = open("read_files/desvantagens.txt", "r")
  arquivo_leitura = arquivo_desvantagens.read()
  arquivo_desvantagens.close()
  desvantagens_encontrados = re.findall(desvantagem_pattern, arquivo_leitura)
  cursor = db.cursor()  
  for desvantagem in desvantagens_encontrados:
    nome_vantagem = desvantagem[0].strip()
    descricao = desvantagem[2].strip()
    valor_vantagem = int(desvantagem[1])
    cursor.execute("INSERT INTO desvantagens (nome_desvantagem, descricao, valor_desvantagem) VALUES (%s, %s, %s)", (nome_vantagem, descricao, valor_vantagem))
  cursor.close()

def import_pericias(db):
  # Patterns
  pericia_pattern = "(.*)(\d)(\d)(.*)"
  # File
  arquivo_pericias = open("read_files/pericias.txt", "r")
  arquivo_leitura = arquivo_pericias.read()
  arquivo_pericias.close()
  pericias_encontradas = re.findall(pericia_pattern, arquivo_leitura)
  cursor = db.cursor()
  for pericia in pericias_encontradas:
    nome_pericia = pericia[0].strip()
    dificuldade_pericia = pericia[2]
    atributo_pericia = pericia[1]
    descricao_pericia = pericia[3].strip()
    cursor.execute("INSERT INTO pericias (nome_pericia, dificuldade, atributo, descricao) VALUES (%s, %s, %s, %s)", (nome_pericia, dificuldade_pericia, atributo_pericia, descricao_pericia))
  cursor.close()

def import_all():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="mydb"
  )
  if mydb.is_connected():
    import_atributes(mydb)
    import_vantagens(mydb)
    import_desvantagens(mydb)
    import_pericias(mydb)
    mydb.commit()
    mydb.close()
    mydb.close()