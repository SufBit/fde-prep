from fetch import fetch_all
from clean import clean_repo

repos = fetch_all("https://api.github.com/users/SufBit/repos")

good = []
bad = []
for repo in repos:
    try:
        good.append(clean_repo(repo))
    except ValueError:
        bad.append(repo)

print(len(good), len(bad))