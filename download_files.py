from pathlib import Path
from ftplib import FTP
from zipfile import ZipFile
import requests
import glob

#Baixar arquivos de relatório do ftp
def download_ftp(domain, dirname, years):
    ftp_conn = FTP(domain)
    ftp_conn.login()

    for a in years:
        path = dirname+'/'+a
        ftp_conn.cwd(path)
        lista = ftp_conn.nlst()
        
        for f in lista:
            print('Baixando o arquivo {}'.format(f))
            with open('data/reports/{}'.format(f),'wb') as fl:
                ftp_conn.retrbinary('RETR {}'.format(f), fl.write, 1024)

    ftp_conn.quit()

#Descompacta os arquivos baixados
def unzip_files():
    all_zip = glob.glob("data/reports/*.zip")
    
    for z in all_zip:
        with ZipFile(z, 'r') as zf:
            zf.extractall("data/reports/")
    
def main():
    #Cria a estrutura de pastas, caso não exista
    Path('./data').mkdir(parents=True,exist_ok=True)
    Path('./data/reports').mkdir(parents=True,exist_ok=True)
    Path('./data/cadop').mkdir(parents=True,exist_ok=True)
    
    download_ftp('ftp.dadosabertos.ans.gov.br','/FTP/PDA/demonstracoes_contabeis/'
                 ,['2019','2020','2021'])
    
    print('Descompactando arquivos')
    unzip_files()
    
    #Download do arquivo de operadoras do cadop
    url = 'http://www.ans.gov.br/externo/site_novo/informacoes_avaliacoes_oper/lista_cadop.asp'
    with open('data/cadop/cadop.csv', 'wb') as fd:
        fd.write(requests.get(url).content)
    
if __name__ == '__main__':
    main()