from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

def _pass():
    pass

with DAG (
    dag_id='ancine',
    start_date=datetime(2024, 4, 15),
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    download = PythonOperator(
        task_id='download',
        python_callable=_pass
    )

    convert = PythonOperator(
        task_id='convert',
        python_callable=_pass
    )

    download >> convert