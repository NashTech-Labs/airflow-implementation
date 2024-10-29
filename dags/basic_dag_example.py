from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'basic_dag_example',
    default_args=default_args,
    description='A simple basic DAG example',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    # Define tasks
    def start_task():
        print("Starting the DAG...")

    def run_task():
        print("Running the main task...")

    def end_task():
        print("DAG has completed successfully.")

    # Create PythonOperator tasks
    start = PythonOperator(
        task_id='start_task',
        python_callable=start_task,
    )

    run = PythonOperator(
        task_id='run_task',
        python_callable=run_task,
    )

    end = PythonOperator(
        task_id='end_task',
        python_callable=end_task,
    )

    # Set the order of task execution
    start >> run >> end
