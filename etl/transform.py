import pandas as pd

def transform_data(data):
    df = pd.DataFrame(data)
    # Realizar transformaciones, por ejemplo, eliminar columnas innecesarias
    df = df[['userId', 'id', 'title', 'body']]
    return df

if __name__ == "__main__":
    with open('../data/extracted_data.json') as f:
        data = json.load(f)
    transformed_data = transform_data(data)
    transformed_data.to_csv('../data/transformed_data.csv', index=False)