import requests

url = "https://api.github.com/users/SufBit/repos"
response = requests.get(url, params = {"per_page":100, "page":1}, timeout=10)


repos = response.json()

# print(len(repos))

# for repo in repos:
#     print(f"Name: {repo['name']}, Language: {repo['language']}, Updated At: {repo['updated_at']}")

all_repos = []
page = 1
while True:
    response = requests.get(url, params = {"per_page":100, "page":page}, timeout=10)
    response.raise_for_status()
    batch = response.json()
    if not batch:
        break
    all_repos.extend(batch)
    page += 1

print(len(all_repos))

for repo in all_repos:
    print(f"Name: {repo['name']}, Language: {repo['language']}, Updated At: {repo['updated_at']}")
