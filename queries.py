# DELETAR TABELAS
cadop_table_drop = 'drop table if exists operadoras'
relatorio_table_drop = 'drop table if exists relatorio_contabil'

# CRIAR TABELAS

cadop_table_create = '''
create table operadoras(
    registro_ans int primary key,
    cnpj bigint not null,
    razao_social varchar(150) not null,
    nome_fantasia varchar(150),
    modalidade varchar(50) not null,
    logradouro varchar(50) not null,
    numero varchar(20) not null,
    complemento varchar(150),
    bairro varchar(50) not null,
    cidade varchar(50) not null,
    uf varchar(2) not null,
    cep varchar(8) not null,
    ddd float,
    telefone varchar(20),
    fax varchar(20),
    email varchar(50),
    representante varchar(150) not null,
    cargo_representante varchar(50) not null,
    data_registro date not null
    );
'''

relatorio_table_create = '''
create table relatorio_contabil(
    id serial primary key,
    data_trimestre date not null,
    registro_ans int not null,
    conta_contabil int not null,
    descricao varchar(150) not null,
    saldo_final numeric not null
    );
'''

# Colunas
relatorio_columns = ['data_trimestre', 'registro_ans', 'conta_contabil',
                     'descricao', 'saldo_final']

#Busca de registros
registros_select = '''
select 
	r.registro_ans, o.razao_social, sum (r.saldo_final)
from relatorio_contabil r
left join operadoras o
using (registro_ans)
where r.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
and r.registro_ans = o.registro_ans
and r.data_trimestre >= '{}'
group by (r.registro_ans, o.razao_social, r.data_trimestre)
order by sum(r.saldo_final) desc
limit 10
'''

#LISTA DE QUERIES
drop_tables_queries = [cadop_table_drop, relatorio_table_drop]
create_tables_queries = [cadop_table_create, relatorio_table_create]