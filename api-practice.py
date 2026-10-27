import time
import requests


def get_with_retry(url: str, params: dict, retries: int = 3) -> requests.Response:
    for attempt in range(retries):
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt == retries - 1:
                raise
            time.sleep(2)
    
def fetch_all(url:str) -> list[dict]:

    all_repos = []
    page = 1
    while True:
        response = get_with_retry(url, {"per_page":100, "page":page})
        batch = response.json()
        if not batch:
            break
        all_repos.extend(batch)
        page += 1

    return all_repos

try:
    repos = fetch_all("https://api.github.com/users/SufBit/repos")
    for repo in repos:
        print(f"Name: {repo['name']}, Language: {repo['language']}, Updated At: {repo['updated_at']}")
    print(f"Total repositories fetched: {len(repos)}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching repositories: {e}")




