from app import add_numbers

def test_add_numbers():
    assert add_numbers(3, 4) == 5
    assert add_numbers(-2, 2) == 0