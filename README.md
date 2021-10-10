# cadop-database-ic
Criar um banco de dados para armazenar informações extraídas de arquivos csv baixados.

## Pré-requisitos
  - Python3
  - PostgreSQL
  
Bibliotecas necessárias para a execução dos arquivos:
  * requests
  ```
  pip install requests
  ```
  * psycopg2
  ```
  pip install psycopg2
  ```

## Execução
Adicione usuário e senha do seu banco de dados postgres nos arquivos load.py e create_tables.py

Para fazer o download dos arquivos, execute o seguinte código no cmd ou terminal:
 ```
  python3 download_files.py
 ```
Em seguida, execute o seguinte comando para criar o banco de dados e as tabelas:
  ```
  python3 create_tables.py
  ```
E então execute o arquivo load.py para fazer o carregamento dos registros no banco de dados e gerar os csv's com as queries.
 ```
  python3 load.py
 ```
