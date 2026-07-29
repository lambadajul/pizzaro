from src.task_manager import complete

def test_complete():

    task = {"completed": False}

    complete(task)

    assert task["completed"]
