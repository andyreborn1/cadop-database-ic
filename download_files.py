from pathlib import Path
from ftplib import FTP


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
    
    
def main():
    #Cria a estrutura de pastas, caso não exista
    Path('./data').mkdir(parents=True,exist_ok=True)
    Path('./data/reports').mkdir(parents=True,exist_ok=True)
    Path('./data/cadop').mkdir(parents=True,exist_ok=True)
    
    download_ftp('ftp.dadosabertos.ans.gov.br','/FTP/PDA/demonstracoes_contabeis/'
                 ,['2019','2020','2021'])
    
if __name__ == '__main__':
    main()