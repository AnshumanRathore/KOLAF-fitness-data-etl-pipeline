# KOLAF (MY FITNESS APP) - Fitness Data ETL Pipeline 🏃‍♂️📊

A robust, localized Data Engineering pipeline built with Python and SQL. This project simulates the backend data processing architecture for a fitness tracking application (handling logs like Calisthenics and Running). 

## 🚀 The Pipeline Architecture (ETL)
1. **Extract:** Ingests raw, unstructured user activity logs from a `.csv` source.
2. **Transform:** Utilizes `pandas` to clean data anomalies (handling null values, standardizing string formats, and filtering out impossible metrics like negative durations).
3. **Load:** Establishes a connection via `SQLAlchemy` and loads the normalized data into a structured `MySQL` relational database.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Manipulation:** Pandas
* **Database:** MySQL
* **ORM / Connectors:** SQLAlchemy, PyMySQL

## 💡 Why I Built This
I built this project to demonstrate fundamental backend and data engineering principles. It showcases practical experience with data normalization, relational database structures, and handling "messy" real-world data gracefully using Python.

## ⚙️ How to Run Locally
1. Clone the repository: `git clone https://github.com/AnshumanRathore/KOLAF-fitness-data-etl-pipeline.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Create a MySQL database named (according to you)`fitness_analytics`.
4. Update the DB credentials in `etl_pipeline.py`.
5. Run the data generator: `python generate_data.py`
6. Execute the pipeline: `python etl_pipeline.py`