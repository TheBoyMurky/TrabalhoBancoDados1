import mysql.connector

def get_comprado(per, desv, db):
    c = db.cursor()
    c.execute(f"""SELECT personagem_desvantagens.comprado
        FROM personagem_desvantagens
        INNER JOIN personagem ON (personagem.idpersonagem = personagem_desvantagens.idpersonagem)
        INNER JOIN desvantagens ON (desvantagens.iddesvantagens = personagem_desvantagens.iddesvantagens)
        WHERE personagem.idpersonagem = (
            SELECT personagem.idpersonagem 
            FROM personagem 
            WHERE UPPER(personagem.nome_personagem) = '{per.nome.upper()}'
        AND desvantagens.iddesvantagens = {desv.id}) 
    """)
    comprado = c.fetchone()[0]
    c.close()
    return comprado

def comprar(per, desv, db):
    c = db.cursor()
    c.execute(f"""UPDATE personagem_desvantagens
    SET comprado = 1
    WHERE personagem_desvantagens.iddesvantagens = {desv.id} 
    AND personagem_desvantagens.idpersonagem = (
        SELECT personagem.idpersonagem 
        FROM personagem 
        WHERE UPPER(personagem.nome_personagem) = 
            '{per.nome.upper()}'
    )""")
    c.execute(f"""UPDATE personagem
    SET pontos = personagem.pontos
    + (
        SELECT desvantagens.valor_desvantagem
        FROM desvantagens
        WHERE desvantagens.iddesvantagens = {desv.id}
    )
    WHERE UPPER(personagem.nome_personagem) = 
	    '{per.nome.upper()}'""")
    c.close()

def descomprar(per, desv, db):
    c = db.cursor()
    c.execute(f"""UPDATE personagem_desvantagens
    SET comprado = 0
    WHERE personagem_desvantagens.iddesvantagens = {desv.id} 
    AND personagem_desvantagens.idpersonagem = (
        SELECT personagem.idpersonagem 
        FROM personagem 
        WHERE UPPER(personagem.nome_personagem) = 
            '{per.nome.upper()}'
    )""")
    c.execute(f"""UPDATE personagem
    SET pontos = personagem.pontos
    - (
        SELECT desvantagens.valor_desvantagem
        FROM desvantagens
        WHERE desvantagens.iddesvantagens = {desv.id}
    )
    WHERE UPPER(personagem.nome_personagem) = 
	    '{per.nome.upper()}'""")
    c.close()