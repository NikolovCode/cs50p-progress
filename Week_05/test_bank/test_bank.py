from bank import value
def main():
    test_value()
def test_value():
    assert value("hello") == 0
    assert value("hello, there") == 0
    assert value("hey, there") == 20
    assert value("HEY, BOSS") == 20
    assert value("OTHER") == 100

if __name__ == "__main__":
    main()

