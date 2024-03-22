import os

from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

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


if __name__ == '__main__':
    path = "downloads/crt-obras-nao-publicitarias/"
    df = read_csvs(path)
    engine = create_engine(connection_string())
    df.to_sql(name='titulos', con=engine, if_exists='replace')