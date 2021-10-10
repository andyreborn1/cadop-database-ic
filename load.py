import psycopg2
import pandas as pd
from queries import *
import glob
import sys
from io import StringIO

# Carrega dados das planilhas de relatóros no banco de dados
def load_reports(cur, conn, path):
    filename = path.split('\\')[-1]
    
    #Transforma o csv em dataframe
    relatorios = pd.read_csv(path,sep=';',
                             parse_dates=['DATA'],
                             encoding='unicode_escape')
    
    #Converte a coluna de saldo para o tipo float
    relatorios['VL_SALDO_FINAL'] = relatorios['VL_SALDO_FINAL'].str.replace(',','.')
    relatorios['VL_SALDO_FINAL'].astype('float64')
    
    #Cria um buffer na memória para fazer a importação dos arquivos para o db
    buffer = StringIO()
    relatorios.to_csv(buffer, header=False, index=False, sep=';')
    buffer.seek(0)
    
    try:
        #Importa os arquivos do buffer para o db
        print('Inserindo registros do arquivo {}'.format(filename))
        cur.copy_from(buffer, sep=';', table='relatorio_contabil',
                      columns=(relatorio_columns))
        
        conn.commit()
        print('Registros do arquivo {} foram inseridos'.format(filename))
        
    except(Exception) as error:
        print('Error {}'.format(error))
        conn.rollback()


# Carrega dados das operadoras no banco de dados
def insert_cadop(cur, conn, path):
    
    #Carrega os dados do csv em um dataframe
    values_na = ['-','---']
    operadoras = pd.read_csv(path, sep=';', 
                         parse_dates=['Data Registro ANS'], 
                         skiprows=2, na_values=values_na,
                         encoding='unicode_escape')
    operadoras['DDD'].fillna(0, inplace=True)
    
    #Cria um buffer na memória para fazer a importação dos arquivos para o db
    buffer = StringIO()
    operadoras.to_csv(buffer, header=False, index=False, sep=';')
    buffer.seek(0)
    
    try:
        #Importa os arquivos do buffer para o db
        print('Inserindo registros das operadoras')
        cur.copy_from(buffer, sep=';', table='operadoras')
        conn.commit()
        print('Registros do cadop inseridos')

    except (Exception) as error:
        print("Error: %s" % error)
        conn.rollback()
    
def main():
    
    #Cria uma conexão com o banco de dados
    try:
        conn = psycopg2.connect(
            database="relatorio_contabil",
            user="student",
            password="student",
            host="127.0.0.1",
            port="5432",
        )
    except (Exception) as error:
        print(error)
        sys.exit(1)
    
    cur = conn.cursor()
    
    #Chamada das funções de inserção
    insert_cadop(cur, conn, path="data/cadop/cadop.csv")
    
    all_path = glob.glob("data/reports/*.csv")
    for path in all_path:
        load_reports(cur, conn, path)
    
    
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
