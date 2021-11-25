CREATE TABLE vantagens (
    idvantagem int not null primary key AUTO_INCREMENT,
    nome_vantagem varchar(45) not null,
    descricao text(200) not null,
    valor_vantagem int not null
);

CREATE TABLE personagem (
    idpersonagem int not null primary key AUTO_INCREMENT,
    nome_personagem varchar(45) not null,
    nome_jogador varchar(45),
    pontos int not null
);

CREATE TABLE personagem_vantagens (
    idpersonagem_vantagem int not null primary key AUTO_INCREMENT,
    idpersonagem int not null,
    idvantagem int not null,
    comprado boolean not null,
    foreign key (idpersonagem)
    references personagem(idpersonagem),
    foreign key (idvantagem)
    references vantagens(idvantagem)
);

CREATE TABLE atributos (
    idatributos int not null primary key AUTO_INCREMENT,
    nome_atributo varchar(13) not null,
    valor_atributo int not null
);

CREATE TABLE personagem_atributo (
    idpersonagem_atributo int not null primary key AUTO_INCREMENT,
    idpersonagem int not null,
    idatributos int not null,
    pontos_gastos int not null,
    foreign key (idpersonagem)
    references personagem(idpersonagem),
    foreign key (idatributos)
    references atributos(idatributos)
);

CREATE TABLE desvantagens (
    iddesvantagens int not null primary key AUTO_INCREMENT,
    nome_desvantagem varchar(45) not null,
    descricao text(200) not null,
    valor_desvantagem int not null
);

CREATE TABLE personagem_desvantagens (
    idpersonagem_desvantagens int not null primary key AUTO_INCREMENT,
    idpersonagem int not null,
    iddesvantagens int not null,
    comprado boolean not null,
    foreign key (idpersonagem)
    references personagem(idpersonagem),
    foreign key (iddesvantagens)
    references desvantagens(iddesvantagens)
);

CREATE TABLE pericias (
    idpericias INT NOT NULL primary key AUTO_INCREMENT,
    nome_pericia VARCHAR(45) NOT NULL,
    dificuldade INT NOT NULL,
    atributo INT NOT NULL,
    descricao text(200) NOT NULL
);

CREATE TABLE personagem_pericias (
    idpersonagem_pericias int not null primary key AUTO_INCREMENT,
    idpersonagem int not null,
    idpericias int not null,
    pontos_gastos int not null,
    foreign key (idpersonagem)
    references personagem(idpersonagem),
    foreign key (idpericias)
    references pericias(idpericias)
);