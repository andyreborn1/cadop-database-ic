import psycopg2
from queries import create_tables_queries, drop_tables_queries

def create_database():
    #Conecta no banco de dados padrão do postgres
    conn = psycopg2.connect(
        database="postgres",
        user="student",
        password="student",
        host="127.0.0.1",
        port="5433",
    )
    
    conn.autocommit = True
    cursor = conn.cursor()
    
    #Cria o banco de dados com codificação UTF-8
    cursor.execute('drop database if exists relatorio_contabil')
    cursor.execute("create database relatorio_contabil with template = template0 encoding = 'UTF8' ")
    
    #Fecha conexões com o banco de dados padrão
    conn.close()
    cursor.close()
    
    #Conecta ao banco de dados relatorio_contabil
    conn = psycopg2.connect(
        database="relatorio_contabil",
        user="dio",
        password="dio",
        host="127.0.0.1",
        port="5433",
    )
    
    cursor = conn.cursor()
    
    return conn, cursor


def drop_tables(conn, cur):
    for query in drop_tables_queries:
        cur.execute(query)
        
    conn.commit()
    
def create_tables(conn, cur):
    for query in create_tables_queries:
        cur.execute(query)
        
    conn.commit()
    
