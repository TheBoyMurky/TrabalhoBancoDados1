import mysql.connector

def get_for(p, db):
    c = db.cursor()
    c.execute(f"""SELECT personagem_atributo.pontos_gastos 
        FROM personagem_atributo 
        INNER JOIN personagem ON (personagem.idpersonagem = personagem_atributo.idpersonagem) 
        INNER JOIN atributos ON (atributos.idatributos = personagem_atributo.idatributos) 
        WHERE personagem.idpersonagem = (
            SELECT personagem.idpersonagem 
            FROM personagem 
            WHERE UPPER(personagem.nome_personagem) = '{p.nome.upper()}') 
        AND atributos.idatributos = 1""") # Pegar os pontos_gastos em força (idatributo = 1)
    r = c.fetchone()[0]
    c.execute("SELECT atributos.valor_atributo FROM atributos WHERE atributos.idatributos = 1") # Pegar o valor_atributo de um idatributo = 1 e o idpersonagem = personagem passado como argumento
    r_val = c.fetchone()[0]
    c.close()
    return int(10 + (r / r_val))

def get_for_val(db):
    c = db.cursor()
    c.execute("SELECT atributos.valor_atributo FROM atributos WHERE atributos.idatributos = 1") # Pegar o valor_atributo de um idatributo = 1 e o idpersonagem = personagem passado como argumento
    r_val = c.fetchone()[0]
    c.close()
    return r_val

def update_melhoria_pontos_for(p, db):
    c = db.cursor()
    c.execute(f"""UPDATE personagem_atributo
        SET pontos_gastos = personagem_atributo.pontos_gastos
            + (
            SELECT atributos.valor_atributo
            FROM atributos
            WHERE atributos.idatributos = 1
            )
        WHERE personagem_atributo.idatributos = 1 
        AND personagem_atributo.idpersonagem = (
            SELECT personagem.idpersonagem 
            FROM personagem 
            WHERE UPPER(personagem.nome_personagem) = 
                '{p.nome.upper()}'
        )""") # Soma em pontos gastos o valor do atributo
    c.execute(f"""UPDATE personagem
        SET pontos = personagem.pontos
	    - (
            SELECT atributos.valor_atributo
	        FROM atributos
	        WHERE atributos.idatributos = 1
	    )
        WHERE UPPER(personagem.nome_personagem) = 
	        '{p.nome.upper()}'""") # Subtrai em pontos de personagem o valor do atributo
    c.close()

def update_diminuicao_pontos_for(p, db):
    c = db.cursor()
    c.execute(f"""UPDATE personagem_atributo
        SET pontos_gastos = personagem_atributo.pontos_gastos
            - (
            SELECT atributos.valor_atributo
            FROM atributos
            WHERE atributos.idatributos = 1
            )
        WHERE personagem_atributo.idatributos = 1 
        AND personagem_atributo.idpersonagem = (
            SELECT personagem.idpersonagem 
            FROM personagem 
            WHERE UPPER(personagem.nome_personagem) = 
                '{p.nome.upper()}'
        )""") # Subtrai em pontos gastos o valor do atributo
    c.execute(f"""UPDATE personagem
        SET pontos = personagem.pontos
	    + (
            SELECT atributos.valor_atributo
	        FROM atributos
	        WHERE atributos.idatributos = 1
	    )
        WHERE UPPER(personagem.nome_personagem) = 
	        '{p.nome.upper()}'""") # Soma em pontos de personagem o valor do atributo
    c.close()

def get_des(p, db):
    c = db.cursor()
    c.execute(f"""SELECT personagem_atributo.pontos_gastos 
        FROM personagem_atributo 
        INNER JOIN personagem ON (personagem.idpersonagem = personagem_atributo.idpersonagem) 
        INNER JOIN atributos ON (atributos.idatributos = personagem_atributo.idatributos) 
        WHERE personagem.idpersonagem = (
            SELECT personagem.idpersonagem 
            FROM personagem 
            WHERE UPPER(personagem.nome_personagem) = '{p.nome.upper()}') 
            AND atributos.idatributos = 2""")
    r = c.fetchone()[0]
    c.execute("SELECT atributos.valor_atributo FROM atributos WHERE atributos.idatributos = 2")
    r_val = c.fetchone()[0]
    c.close()
    return int(10 + (r / r_val))

def get_des_val(db):
    c = db.cursor()
    c.execute("SELECT atributos.valor_atributo FROM atributos WHERE atributos.idatributos = 2") 
    r_val = c.fetchone()[0]
    c.close()
    return r_val

def update_melhoria_pontos_des(p, db):
    c = db.cursor()
    c.execute(f"""UPDATE personagem_atributo
        SET pontos_gastos = personagem_atributo.pontos_gastos
            + (
            SELECT atributos.valor_atributo
            FROM atributos
            WHERE atributos.idatributos = 2
            )
        WHERE personagem_atributo.idatributos = 2 
        AND personagem_atributo.idpersonagem = (
            SELECT personagem.idpersonagem 
            FROM personagem 
            WHERE UPPER(personagem.nome_personagem) = 
                '{p.nome.upper()}'
        )""") # Soma em pontos gastos o valor do atributo
    c.execute(f"""UPDATE personagem
        SET pontos = personagem.pontos
	    - (
            SELECT atributos.valor_atributo
	        FROM atributos
	        WHERE atributos.idatributos = 2
	    )
        WHERE UPPER(personagem.nome_personagem) = 
	        '{p.nome.upper()}'""") # Subtrai em pontos de personagem o valor do atributo
    c.close()

def update_diminuicao_pontos_des(p, db):
    c = db.cursor()
    c.execute(f"""UPDATE personagem_atributo
        SET pontos_gastos = personagem_atributo.pontos_gastos
            - (
            SELECT atributos.valor_atributo
            FROM atributos
            WHERE atributos.idatributos = 2
            )
        WHERE personagem_atributo.idatributos = 2 
        AND personagem_atributo.idpersonagem = (
            SELECT personagem.idpersonagem 
            FROM personagem 
            WHERE UPPER(personagem.nome_personagem) = 
                '{p.nome.upper()}'
        )""") # Subtrai em pontos gastos o valor do atributo
    c.execute(f"""UPDATE personagem
        SET pontos = personagem.pontos
	    + (
            SELECT atributos.valor_atributo
	        FROM atributos
	        WHERE atributos.idatributos = 2
	    )
        WHERE UPPER(personagem.nome_personagem) = 
	        '{p.nome.upper()}'""") # Soma em pontos de personagem o valor do atributo
    c.close()

def get_int(p, db):
    c = db.cursor()
    c.execute(f"""SELECT personagem_atributo.pontos_gastos 
    FROM personagem_atributo 
    INNER JOIN personagem ON (personagem.idpersonagem = personagem_atributo.idpersonagem) 
    INNER JOIN atributos ON (atributos.idatributos = personagem_atributo.idatributos) 
    WHERE personagem.idpersonagem = (
        SELECT personagem.idpersonagem 
        FROM personagem 
        WHERE UPPER(personagem.nome_personagem) = '{p.nome.upper()}') 
        AND atributos.idatributos = 3""") 
    r = c.fetchone()[0]
    c.execute("SELECT atributos.valor_atributo FROM atributos WHERE atributos.idatributos = 3") 
    r_val = c.fetchone()[0]
    c.close()
    return int(10 + (r / r_val))

def get_int_val(db):
    c = db.cursor()
    c.execute("SELECT atributos.valor_atributo FROM atributos WHERE atributos.idatributos = 3") 
    r_val = c.fetchone()[0]
    c.close()
    return r_val

def update_melhoria_pontos_int(p, db):
    c = db.cursor()
    c.execute(f"""UPDATE personagem_atributo
        SET pontos_gastos = personagem_atributo.pontos_gastos
            + (
            SELECT atributos.valor_atributo
            FROM atributos
            WHERE atributos.idatributos = 3
            )
        WHERE personagem_atributo.idatributos = 3
        AND personagem_atributo.idpersonagem = (
            SELECT personagem.idpersonagem 
            FROM personagem 
            WHERE UPPER(personagem.nome_personagem) = 
                '{p.nome.upper()}'
        )""") # Soma em pontos gastos o valor do atributo
    c.execute(f"""UPDATE personagem
        SET pontos = personagem.pontos
	    - (
            SELECT atributos.valor_atributo
	        FROM atributos
	        WHERE atributos.idatributos = 3
	    )
        WHERE UPPER(personagem.nome_personagem) = 
	        '{p.nome.upper()}'""") # Subtrai em pontos de personagem o valor do atributo
    c.close()

def update_diminuicao_pontos_int(p, db):
    c = db.cursor()
    c.execute(f"""UPDATE personagem_atributo
        SET pontos_gastos = personagem_atributo.pontos_gastos
            - (
            SELECT atributos.valor_atributo
            FROM atributos
            WHERE atributos.idatributos = 3
            )
        WHERE personagem_atributo.idatributos = 3
        AND personagem_atributo.idpersonagem = (
            SELECT personagem.idpersonagem 
            FROM personagem 
            WHERE UPPER(personagem.nome_personagem) = 
                '{p.nome.upper()}'
        )""") # Subtrai em pontos gastos o valor do atributo
    c.execute(f"""UPDATE personagem
        SET pontos = personagem.pontos
	    + (
            SELECT atributos.valor_atributo
	        FROM atributos
	        WHERE atributos.idatributos = 3
	    )
        WHERE UPPER(personagem.nome_personagem) = 
	        '{p.nome.upper()}'""") # Soma em pontos de personagem o valor do atributo
    c.close()

def get_vit(p, db):
    c = db.cursor()
    c.execute(f"""SELECT personagem_atributo.pontos_gastos 
        FROM personagem_atributo 
        INNER JOIN personagem ON (personagem.idpersonagem = personagem_atributo.idpersonagem) 
        INNER JOIN atributos ON (atributos.idatributos = personagem_atributo.idatributos) 
        WHERE personagem.idpersonagem = (
            SELECT personagem.idpersonagem 
            FROM personagem 
            WHERE UPPER(personagem.nome_personagem) = '{p.nome.upper()}') 
            AND atributos.idatributos = 4""")
    r = c.fetchone()[0]
    c.execute("SELECT atributos.valor_atributo FROM atributos WHERE atributos.idatributos = 4")
    r_val = c.fetchone()[0]
    c.close()
    return int(10 + (r / r_val))

def get_vit_val(db):
    c = db.cursor()
    c.execute("SELECT atributos.valor_atributo FROM atributos WHERE atributos.idatributos = 4")
    r_val = c.fetchone()[0]
    c.close()
    return r_val

def update_melhoria_pontos_vit(p, db):
    c = db.cursor()
    c.execute(f"""UPDATE personagem_atributo
        SET pontos_gastos = personagem_atributo.pontos_gastos
            + (
            SELECT atributos.valor_atributo
            FROM atributos
            WHERE atributos.idatributos = 4
            )
        WHERE personagem_atributo.idatributos = 4
        AND personagem_atributo.idpersonagem = (
            SELECT personagem.idpersonagem 
            FROM personagem 
            WHERE UPPER(personagem.nome_personagem) = 
                '{p.nome.upper()}'
        )""") # Soma em pontos gastos o valor do atributo
    c.execute(f"""UPDATE personagem
        SET pontos = personagem.pontos
	    - (
            SELECT atributos.valor_atributo
	        FROM atributos
	        WHERE atributos.idatributos = 4
	    )
        WHERE UPPER(personagem.nome_personagem) = 
	        '{p.nome.upper()}'""") # Subtrai em pontos de personagem o valor do atributo
    c.close()

def update_diminuicao_pontos_vit(p, db):
    c = db.cursor()
    c.execute(f"""UPDATE personagem_atributo
        SET pontos_gastos = personagem_atributo.pontos_gastos
            - (
            SELECT atributos.valor_atributo
            FROM atributos
            WHERE atributos.idatributos = 4
            )
        WHERE personagem_atributo.idatributos = 4
        AND personagem_atributo.idpersonagem = (
            SELECT personagem.idpersonagem 
            FROM personagem 
            WHERE UPPER(personagem.nome_personagem) = 
                '{p.nome.upper()}'
        )""") # Subtrai em pontos gastos o valor do atributo
    c.execute(f"""UPDATE personagem
        SET pontos = personagem.pontos
	    + (
            SELECT atributos.valor_atributo
	        FROM atributos
	        WHERE atributos.idatributos = 4
	    )
        WHERE UPPER(personagem.nome_personagem) = 
	        '{p.nome.upper()}'""") # Soma em pontos de personagem o valor do atributo
    c.close()