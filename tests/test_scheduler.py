from src.scheduler import add_session

def test_add_session():

    schedule = []

    add_session(schedule, {"subject": "Math"})

    assert len(schedule) == 1
