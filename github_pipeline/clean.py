
from fetch import fetch_all


repos = fetch_all("https://api.github.com/users/SufBit/repos")
#print("First repo in list:", repos[0].keys())


def clean_repo(repo: dict) -> dict:
    # reject forks: we only want repos that are my own work
    if repo["fork"]:
        raise ValueError("Fork")

    # keep repos with no language so they still show up in language counts
    language = repo["language"]
    if language is None:
        language = "Unknown"

    # missing description gets a readable default
    description = repo["description"]
    if description is None:
        description = "No description provided"

    # keep only the date part of the timestamp (2024-08-06)
    updated_at = repo["updated_at"][:10]

    return {
        "name": repo["name"],
        "language": language,
        "description": description,
        "updated_at": updated_at,
        "stars": repo["stargazers_count"],
    }