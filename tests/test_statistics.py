from src.statistics import summary

def test_statistics():

    result = summary([], [])

    assert result["tasks"] == 0
