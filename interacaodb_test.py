import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123",
  database="mydb"
)

if mydb.is_connected():
  cursor = mydb.cursor()
  # Inserindo Valores dentro do DB
  cursor.execute("INSERT INTO atributos (nome_atributo) VALUES ('Força')")
  cursor.execute("INSERT INTO atributos (nome_atributo) VALUES ('Destreza')")
  cursor.execute("INSERT INTO atributos (nome_atributo) VALUES ('Inteligência')")
  cursor.execute("INSERT INTO atributos (nome_atributo) VALUES ('Vitalidade')")
  mydb.commit()

  # Puxando Valores
  cursor.execute("SELECT * FROM atributos")
  myresult = cursor.fetchall()
  for i in myresult:
    print(i)

if mydb.is_connected():
  cursor.close()
  mydb.close()