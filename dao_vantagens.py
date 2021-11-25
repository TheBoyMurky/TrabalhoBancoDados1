import mysql.connector

def get_comprado(per, van, db):
    c = db.cursor()
    c.execute(f"""SELECT personagem_vantagens.comprado
        FROM personagem_vantagens
        INNER JOIN personagem ON (personagem.idpersonagem = personagem_vantagens.idpersonagem)
        INNER JOIN vantagens ON (vantagens.idvantagem = personagem_vantagens.idvantagem)
        WHERE personagem.idpersonagem = (
            SELECT personagem.idpersonagem 
            FROM personagem 
            WHERE UPPER(personagem.nome_personagem) = '{per.nome.upper()}'
        AND vantagens.idvantagem = {van.id}) 
    """)
    comprado = c.fetchone()[0]
    c.close()
    return comprado

def comprar(per, van, db):
    c = db.cursor()
    c.execute(f"""UPDATE personagem_vantagens
    SET comprado = 1
    WHERE personagem_vantagens.idvantagem = {van.id} 
    AND personagem_vantagens.idpersonagem = (
        SELECT personagem.idpersonagem 
        FROM personagem 
        WHERE UPPER(personagem.nome_personagem) = 
            '{per.nome.upper()}'
    )""")
    c.execute(f"""UPDATE personagem
    SET pontos = personagem.pontos
    - (
        SELECT vantagens.valor_vantagem
        FROM vantagens
        WHERE vantagens.idvantagem = {van.id}
    )
    WHERE UPPER(personagem.nome_personagem) = 
	    '{per.nome.upper()}'""")
    c.close()

def descomprar(per, van, db):
    c = db.cursor()
    c.execute(f"""UPDATE personagem_vantagens
    SET comprado = 0
    WHERE personagem_vantagens.idvantagem = {van.id} 
    AND personagem_vantagens.idpersonagem = (
        SELECT personagem.idpersonagem 
        FROM personagem 
        WHERE UPPER(personagem.nome_personagem) = 
            '{per.nome.upper()}'
    )""")
    c.execute(f"""UPDATE personagem
    SET pontos = personagem.pontos
    + (
        SELECT vantagens.valor_vantagem
        FROM vantagens
        WHERE vantagens.idvantagem = {van.id}
    )
    WHERE UPPER(personagem.nome_personagem) = 
	    '{per.nome.upper()}'""")
    c.close()