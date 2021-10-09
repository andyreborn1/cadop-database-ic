import pandas as pd
from io import StringIO

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
