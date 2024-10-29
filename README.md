## Basic DAG Example
This project demonstrates a simple Apache Airflow Directed Acyclic Graph (DAG) that consists of three basic tasks: start_task, run_task, and end_task.

## Prerequisites
Ensure you have Python (preferably 3.7 or above) and pip installed.

**Step 1:** Install Apache Airflow
To set up Airflow, we recommend creating a virtual environment for easier dependency management.

- Create and activate a virtual environment:
```shell
python3 -m venv airflow_env
source airflow_env/bin/activate  # For Windows, use `airflow_env\Scripts\activate`
```
- Install Apache Airflow:
```shell
pip install apache-airflow
```
- Initialize Airflow:
```shell
airflow db init or airflow db migrate
```

**Step 2:** Set Up the DAG Folder and File
- Create the DAG directory:
```shell
mkdir -p ~/airflow/dags
```
- Save the DAG file: Copy the provided DAG code and save it in ~/airflow/dags/basic_dag_example.py.     
- Verify the DAG location: Ensure Airflow is configured to use ~/airflow/dags as the DAG directory by checking airflow.cfg (dags_folder = ~/airflow/dags).

**Step 3:** Start Airflow Web Server and Scheduler
- Start the web server:
```shell
airflow webserver --port 8082
```
- Start the scheduler:
```shell
airflow scheduler
```
- Access the Airflow UI: Navigate to http://localhost:8082 in your browser. You should see the DAG basic_dag_example in the list of available DAGs. Toggle the DAG to "On" to schedule it.