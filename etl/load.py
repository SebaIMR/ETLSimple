import pandas as pd
from sqlalchemy import create_engine
import os

def load_data(file_path, db_url):
    engine = create_engine(db_url)
    df = pd.read_csv(file_path)
    df.to_sql('posts', engine, if_exists='replace', index=False)

if __name__ == "__main__":
    db_url = os.getenv('DATABASE_URL')
    load_data('../data/transformed_data.csv', db_url)