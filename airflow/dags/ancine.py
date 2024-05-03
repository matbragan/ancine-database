from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from settings import BASE_URL, FILE_TABLES
from download import download_and_unzip
from convert_database import ConvertDatabase, read_csvs


def execute_download():
    for file in FILE_TABLES:
        download_and_unzip(BASE_URL, file)


def execute_convert_database():
    convert = ConvertDatabase()
    
    for file, table in FILE_TABLES.items():
        path = f'downloads/{file}/'
        df = read_csvs(path)
        convert.load_table(df, table)
    
    convert.close_con()


with DAG (
    dag_id='ancine',
    start_date=datetime(2024, 4, 15),
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    download = PythonOperator(
        task_id='download',
        python_callable=execute_download
    )

    convert = PythonOperator(
        task_id='convert',
        python_callable=execute_convert_database
    )

    download >> convert