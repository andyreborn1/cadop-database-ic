import psycopg2
from queries import create_tables_queries, drop_tables_queries
import sys

def create_database():
    #Conecta no banco de dados padrão do postgres
    try:
        conn = psycopg2.connect(
            database="postgres",
            user="",
            password="",
            host="127.0.0.1",
            port="5432",
        )
    except (Exception) as error:
        print(error)
        sys.exit(1)
    
    conn.autocommit = True
    cursor = conn.cursor()
    
    #Cria o banco de dados com codificação UTF-8
    cursor.execute('drop database if exists relatorio_contabil')
    cursor.execute("create database relatorio_contabil with template = template0 encoding = 'UTF8' ")
    
    #Fecha conexões com o banco de dados padrão
    conn.close()
    cursor.close()
    
    #Conecta ao banco de dados relatorio_contabil
    try:
        conn = psycopg2.connect(
            database="relatorio_contabil",
            user="",
            password="",
            host="127.0.0.1",
            port="5432",
        )
    except (Exception) as error:
        print(error)
        sys.exit(1)
    
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
    
def main():
    conn, cur = create_database()
    
    drop_tables(conn, cur)
    create_tables(conn, cur)
    
    conn.close()
    cur.close()
    
if __name__ == '__main__':
    main()