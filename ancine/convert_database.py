import os
import logging

from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

log_format = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)
log = logging.getLogger(__name__)

load_dotenv()


FILES = [
    'bilheteria-diaria-obras-por-distribuidoras',
    'crt-obras-nao-publicitarias',
    'obras-nao-pub-brasileiras',
    'obras-nao-pub-estrangeiras'
]


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
    
    return pd.concat(dfs, ignore_index=True)


def connection_string() -> str:
    user = os.getenv('MYSQL_USER')
    pwd = os.getenv('MYSQL_PWD')
    host = os.getenv('MYSQL_HOST')
    port = os.getenv('MYSQL_PORT')
    database = os.getenv('MYSQL_DATABASE')
    return f'mysql://{user}:{pwd}@{host}:{port}/{database}'


def create_con() -> create_engine:
    try:
        engine = create_engine(connection_string())
        msg = 'Conectado ao banco MySQL'
        log.info(msg)
        return engine
    except Exception as e:
        msg = f'Erro ao conectar ao banco - {e}'
        log.error(msg)


def load_table(df: pd.DataFrame, engine: create_engine, table_name: str) -> None:
    try:
        df.to_sql(name=table_name, con=engine, if_exists='replace')
        msg = f'Tabela {table_name} carregada no banco MySQL com sucesso'
        log.info(msg)
    except Exception as e:
        msg = f'Erro ao carregar a tabela {table_name} no banco MySQL - {e}'
        log.error(msg)


def close_con(engine) -> None:
    engine.dispose()


if __name__ == '__main__':
    path = "downloads/crt-obras-nao-publicitarias/"
    df = read_csvs(path)
    engine = create_con()
    load_table(df, engine, 'titulos')
    close_con(engine)
