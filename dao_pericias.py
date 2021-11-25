import mysql.connector

def get_pontos_gastos(pers, peri, db):
    c = db.cursor()
    c.execute(f"""SELECT personagem_pericias.pontos_gastos
        FROM personagem_pericias
        INNER JOIN personagem ON (personagem.idpersonagem = personagem_pericias.idpersonagem)
        INNER JOIN pericias ON (pericias.idpericias = personagem_pericias.idpericias)
        WHERE personagem.idpersonagem = (
            SELECT personagem.idpersonagem 
            FROM personagem 
            WHERE UPPER(personagem.nome_personagem) = '{pers.nome.upper()}'
        AND pericias.idpericias = {peri.id})  
    """)
    comprado = c.fetchone()[0]
    c.close()
    return comprado

def alterar_pontos(pers, peri, pontos, soma, db):
    c = db.cursor()
    c.execute(f"""UPDATE personagem_pericias
    SET pontos_gastos = {pontos}
    WHERE personagem_pericias.idpericias = {peri.id} 
    AND personagem_pericias.idpersonagem = (
        SELECT personagem.idpersonagem 
        FROM personagem 
        WHERE UPPER(personagem.nome_personagem) = 
            '{pers.nome.upper()}'
    ) 
    """)
    if soma > 0:
        c.execute(f"""UPDATE personagem
        SET pontos = personagem.pontos
        - {int(soma)}
        WHERE UPPER(personagem.nome_personagem) = 
            '{pers.nome.upper()}'""")
    else:
        c.execute(f"""UPDATE personagem
        SET pontos = personagem.pontos
        + {int(soma)}
        WHERE UPPER(personagem.nome_personagem) = 
            '{pers.nome.upper()}'""")
    c.close()