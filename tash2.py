import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def search_data(data, keyword):
    return [item for item in data if keyword.lower() in item['title'].lower() or keyword.lower() in item['body'].lower()]

def display_results(results):
    for item in results:
        print(f"ID: {item['id']}")
        print(f"Title: {item['title']}")
        print(f"Body: {item['body']}")
        print("-"*40)

def main():
    print("Fetching API data...\n")
    data = fetch_data()

    if not data:
        return

    keyword = input("Enter keyword to search: ")
    filtered = search_data(data, keyword)

    print(f"\nFound {len(filtered)} result(s):\n")
    display_results(filtered)

if __name__ == "__main__":
    main()
