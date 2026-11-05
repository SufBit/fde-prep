from clean import clean_repo
import pytest

def make_repo():
    return {
        "name": "demo",
        "fork": False,
        "language": "Python",
        "description": "A demo repo",
        "updated_at": "2024-08-06T00:18:17Z",
        "stargazers_count": 3,
    }


def test_normal_repo():
    result = clean_repo(make_repo())
    assert result == {
        "name": "demo",
        "language": "Python",
        "description": "A demo repo",
        "updated_at": "2024-08-06",
        "stars": 3,
    }

def test_fork_repo():
    repo = make_repo()
    repo["fork"] = True
    with pytest.raises(ValueError):
        clean_repo(repo)

def test_missing_language():
    repo = make_repo()
    repo["language"] = None
    result = clean_repo(repo)
    assert result["language"] == "Unknown"

def test_missing_description():
    repo = make_repo()
    repo["description"] = None
    result = clean_repo(repo)
    assert result["description"] == "No description provided"