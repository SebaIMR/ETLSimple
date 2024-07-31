import requests

def extract_data(url):
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    data = extract_data(url)
    with open('../data/extracted_data.json', 'w') as f:
        json.dump(data, f)