from plates import is_valid

def main():
    test_is_valid_count()
    test_is_valid_twoletters()
    test_is_valid_middle()
    test_is_valid_punk()

def test_is_valid_twoletters():
    assert is_valid("A5AA") == False
    assert is_valid("5AA5") == False
    assert is_valid("22") == False
def test_is_valid_count():
    assert is_valid("AA") == True
    assert is_valid("A") == False
def test_is_valid_middle():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False
def test_is_valid_punk():
    assert is_valid("AA,AA") == False


if __name__ == "__main__":
    main()
