import pandas as pd
from sqlalchemy import create_engine
import sys

# --- CONFIGURATION ---
DB_USER = "root"          
DB_PASSWORD = 9887992780  
DB_HOST = "localhost"
DB_NAME = "anshudb"
CSV_FILE = "kolaf_raw_logs.csv"

def extract_data(file_path):
    """EXTRACT: Read the raw CSV file."""
    print("Extracting data...")
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"❌ Error extracting data: {e}")
        sys.exit(1)

def transform_data(df):
    """TRANSFORM: Clean and format the data."""
    print("Transforming data...")
    
    # 1. Standardize text: Remove extra spaces and make title case (e.g., " running" -> "Running")
    df['activity'] = df['activity'].str.strip().str.title()
    
    # 2. Handle Missing Values: Drop rows where the activity type is completely missing
    df = df.dropna(subset=['activity'])
    
    # 3. Filter Invalid Data: Remove impossible negative durations or null durations
    df = df[df['duration_minutes'] > 0]
    
    # 4. Fill Missing Distances: If it's Calisthenics, distance is 0 km. 
    df.loc[df['activity'] == 'Calisthenics', 'distance_km'] = 0.0
    
    return df

def load_data(df, db_user, db_password, db_host, db_name):
    """LOAD: Push the clean data to MySQL."""
    print("Loading data into MySQL...")
    
    # Connect using SQLAlchemy & PyMySQL
    connection_string = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
    
    try:
        engine = create_engine(connection_string)
        
        # This will create the table 'clean_activity_logs' automatically if it doesn't exist
        # and append the data to it.
        df.to_sql('clean_activity_logs', con=engine, if_exists='append', index=False)
        print("✅ Data successfully loaded into the database!")
        
    except Exception as e:
        print(f"❌ Database error: {e}")
        print("Make sure MySQL is running and the database exists!")

# --- EXECUTION FLOW ---
if __name__ == "__main__":
    # 1. Extract
    raw_df = extract_data(CSV_FILE)
    
    # 2. Transform
    clean_df = transform_data(raw_df)
    
    # 3. Load
    # Note: Create the database `fitness_analytics` in your MySQL workbench first!
    load_data(clean_df, DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)