import os
import logging

from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine, Engine

log_format = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)
log = logging.getLogger(__name__)

load_dotenv()


TABLES = {
    'bilheteria': 'bilheteria-diaria-obras-por-distribuidoras',
    'obras_crt': 'crt-obras-nao-publicitarias',
    'obras_brasileiras': 'obras-nao-pub-brasileiras',
    'obras_estrangeiras': 'obras-nao-pub-estrangeiras',
}


def read_csvs(path: str) -> pd.DataFrame:
    '''
    Função para ler vários arquivos csvs e criar um único dataframe,
    é esperado que os csvs tenham a mesma estrutura

    args:
        - path: caminho de diretório onde os csvs estão
    '''
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    dfs = []
    for file in files:
        tmp_df = pd.read_csv(os.path.join(path, file), sep=";")
        dfs.append(tmp_df)
    
    msg = f'{path} - pandas DataFrame criado com sucesso'
    log.info(msg)
    return pd.concat(dfs, ignore_index=True)


class ConvertDatabase:
    def __init__(self):
        self.engine = self.create_con()


    def connection_string(self) -> str:
        '''
        Função para criar a string de conexão para o banco MySQL
        baseado nos argumentos passados no arquivo .env
        '''
        user = os.getenv('MYSQL_USER')
        pwd = os.getenv('MYSQL_PWD')
        host = os.getenv('MYSQL_HOST')
        port = os.getenv('MYSQL_PORT')
        database = os.getenv('MYSQL_DATABASE')
        return f'mysql://{user}:{pwd}@{host}:{port}/{database}'


    def create_con(self) -> Engine:
        '''
        Função para criar a conexão no banco MySQL usando SQLAlchemy
        '''
        try:
            engine = create_engine(self.connection_string())
            msg = 'Conectado ao banco MySQL'
            log.info(msg)
            return engine
        except Exception as e:
            msg = f'Erro ao conectar ao banco - {e}'
            log.error(msg)


    def load_table(self, df: pd.DataFrame, table_name: str) -> None:
        '''
        Função para carregar as tabelas, baseadas em pandas DataFrames,
        no banco passado pela engine, neste caso, o banco MySQL

        args:
            - df: pandas DataFrame contendo os dados da tabela a ser carregada
            - table_name: nome da tabela no banco
        '''
        try:
            df.to_sql(name=table_name, con=self.engine, if_exists='replace')
            msg = f'Tabela {table_name} carregada no banco MySQL com sucesso'
            log.info(msg)
        except Exception as e:
            msg = f'Erro ao carregar a tabela {table_name} no banco MySQL - {e}'
            log.error(msg)


    def close_con(self) -> None:
        '''
        Função para encerrar a conexão com o banco
        '''
        self.engine.dispose()


if __name__ == '__main__':
    convert = ConvertDatabase()
    
    for table in TABLES:
        path = f'downloads/{TABLES[table]}/'
        df = read_csvs(path)
        convert.load_table(df, table)
    
    convert.close_con()
