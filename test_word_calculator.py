from word_calculator import calc


def test_addition():
    result = calc("2 plus 2")
    assert result is not None
