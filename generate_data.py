import pandas as pd
import random
from datetime import datetime, timedelta

# Create intentional messy data
data = {
    "user_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "activity": ["Running", " Calisthenics ", "running", "Cycling", "Running", "CALISTHENICS", "Running", None, "Calisthenics", "Running"],
    "duration_minutes": [45, 60, -15, 120, 30, 45, None, 50, -10, 25], # Negative and null values
    "distance_km": [5.2, 0, 3.1, 20.5, 4.0, 0, 8.5, 0, 0, 2.5],
    "date": [(datetime.today() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(10)]
}

df = pd.DataFrame(data)
df.to_csv("kolaf_raw_logs.csv", index=False)
print("✅ Created kolaf_raw_logs.csv with messy dummy data!")