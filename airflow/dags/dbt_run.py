import os
from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow_dbt.operators.dbt_operator import (
    DbtRunOperator
)


def list_models(dbt_path):
    model_path = os.path.join(dbt_path, 'models')
    sql_files = [f for f in os.listdir(model_path) if f.endswith('.sql')]
    file_names = [os.path.splitext(os.path.basename(file))[0] for file in sql_files]
    return file_names


DBT_PATH = '/dbt/ancine'

default_args = {
  'dir': DBT_PATH,
  'start_date': datetime(2024, 4, 15),
  'catchup': False
}

models = list_models(DBT_PATH)

with DAG(
    dag_id='dbt_run', 
    default_args=default_args, 
    schedule_interval='@daily'
) as dag:
    
    dbt_debug = BashOperator(
        task_id='dbt_debug_connection',
        bash_command=f'dbt debug --connection --project-dir {DBT_PATH} --profiles-dir {DBT_PATH}'
    )
    
    for model in models:

        dbt_run = DbtRunOperator(
            task_id=f'model_{model}',
            models=model
        )

        dbt_debug >> dbt_run
