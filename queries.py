#CREATE TABLES
cadop_table_create = '''
create table operadoras(
    registro_ans int primary key,
    cnpj bigint not null,
    razao_social varchar(150) not null,
    nome_fantasia varchar(150),
    modalidade varchar(50) not null,
    logradouro varchar(50) not null,
    numero int not null,
    complemento varchar(150),
    bairro varchar(50) not null,
    cidade varchar(50) not null,
    uf varchar(2) not null,
    cep varchar(8) not null,
    ddd varchar(2),
    telefone varchar(10),
    fax varchar(10),
    email varchar(20),
    representante varchar(150) not null,
    cargo_representante varchar(20) not null,
    data_registro date not null
    );
'''