import mysql.connector

def create_personagem(p, db):
    c = db.cursor(buffered=True)
    c.execute("INSERT INTO personagem (nome_personagem, pontos) VALUES (%s, %s)", (p.nome, p.pontos))
    c.execute(f"SELECT idpersonagem FROM personagem WHERE UPPER(nome_personagem) = '{p.nome.upper()}'")
    id = c.fetchone()[0] # TODO, create um if para que caso não tiver nada devolver nulo
    
    # INSERT personagem_atributo
    for i in range(1, 5):
        c.execute("INSERT INTO personagem_atributo (idpersonagem, idatributos, pontos_gastos) VALUES (%s, %s, 0)", (id, i))
    # INSERT personagem_vantagens
    c.execute("SELECT * FROM vantagens")
    # try:
    #     r_van = c.fetchone()
    #     while r_van[0] is not None:
    #         c.execute("INSERT INTO personagem_vantagens (idpersonagem, idvantagem, comprado) VALUES (%s, %s, 0)", (id, r_van[0]))
    #         r_van = c.fetchone()
    # except mysql.connector.Error as e:
    #     print(e)
    for i in range(1, 11): # Ajustar Depois!
        c.execute("INSERT INTO personagem_vantagens (idpersonagem, idvantagem, comprado) VALUES (%s, %s, 0)", (id, i))
    # INSERT personagem_desvantagens
    c.execute("SELECT * FROM desvantagens")
    for i in range(1, 14):
        c.execute("INSERT INTO personagem_desvantagens (idpersonagem, iddesvantagens, comprado) VALUES (%s, %s, 0)", (id, i))
    # INSERT personagem_pericias
    c.execute("SELECT * FROM pericias")
    for i in range(1, 6):
        c.execute("INSERT INTO personagem_pericias (idpersonagem, idpericias, pontos_gastos) VALUES (%s, %s, 0)", (id, i))

    c.close()
    db.commit()

def get_id_personagens(db):
    c = db.cursor()
    c.execute("SELECT idpersonagem FROM personagem ORDER BY idpersonagem DESC LIMIT 1")
    if c.fetchall() == []:
        id = 1
    else:
        id = c.fetchone()
    return id

def get_pontos(p, db):
    c = db.cursor()
    c.execute(f"SELECT pontos FROM personagem WHERE UPPER(nome_personagem) = '{p.nome.upper()}'")
    return c.fetchone()[0]

def remover_personagem(p, db):
    c = db.cursor()
    c.execute(f"DELETE FROM personagem_atributo WHERE idpersonagem = {p.id}")
    c.execute(f"DELETE FROM personagem_desvantagens WHERE idpersonagem = {p.id}")
    c.execute(f"DELETE FROM personagem_pericias WHERE idpersonagem = {p.id}")
    c.execute(f"DELETE FROM personagem_vantagens WHERE idpersonagem = {p.id}")
    c.execute(f"DELETE FROM personagem WHERE idpersonagem = {p.id}")
    c.close()