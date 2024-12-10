from airflow import DAG, Dataset
from datetime import datetime
from airflow.decorators import task


my_file = Dataset("/tmp/my_file.txt")

with DAG(
    dag_id="producer",
    tags=['custom'],
    start_date=datetime(2022, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:
    
    @task(outlets=[my_file])
    def update_dataset():
        with open(my_file.uri, 'a+') as f:
            f.write("producer update")

    update_dataset()