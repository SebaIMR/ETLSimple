from extract import extract_data
from transform import transform_data
from load import load_data
import json
import os

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    data = extract_data(url)
    
    with open('../data/extracted_data.json', 'w') as f:
        json.dump(data, f)
    
    transformed_data = transform_data(data)
    transformed_data.to_csv('../data/transformed_data.csv', index=False)
    
    db_url = os.getenv('DATABASE_URL')
    load_data('../data/transformed_data.csv', db_url)