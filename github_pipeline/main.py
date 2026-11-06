import sqlite3
from fetch import fetch_all
from clean import clean_repo
from store import create_table, insert_repos

def main():
    # 1. fetch the repos
    repos = fetch_all("https://api.github.com/users/SufBit/repos")
    # 2. clean each one (try/except ValueError), collect good and bad
    good_repos = []
    bad_repos = []
    for repo in repos:
        try:
            cleaned_repo = clean_repo(repo)
            good_repos.append(cleaned_repo)
        except ValueError:
            bad_repos.append(repo)
    # 3. connect to pipeline.db, create_table, insert_repos, close
    conn = sqlite3.connect("pipeline.db")
    create_table(conn)
    insert_repos(conn, good_repos)
    conn.close()
    # 4. print a summary: fetched, kept, rejected
    print(f"Fetched {len(repos)} repos, kept {len(good_repos)}, rejected {len(bad_repos)}")


if __name__ == "__main__":
    main()