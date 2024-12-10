from airflow import DAG, Dataset
from airflow.decorators import task
from datetime import datetime


my_file = Dataset("/tmp/my_file.txt")

with DAG(
    dag_id="comsumer",
    tags=['custom'],
    start_date=datetime(2022, 1, 1),
    # when my_file is updated, the DAG will be triggered
    schedule=[my_file],
    catchup=False
) as dag:

    @task()
    def read_dataset():
        with open(my_file.uri, 'r') as f:
            print(f.read())

    read_dataset()