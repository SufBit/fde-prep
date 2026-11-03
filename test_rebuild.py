from rebuild import count_by

def test_count_by_status():
    completed = {"status" : "completed"}
    no_show = {"status" : "no-show"}

    assert count_by([completed, completed, no_show], "status") == {"completed": 2, "no-show": 1}

def test_count_by_empty():
    assert count_by([], "status") == {}

