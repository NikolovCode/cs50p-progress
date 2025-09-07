import pytest
from numb3rs import validate

def main():
    test_valid()

def test_valid():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("0.255.0.255") == True
def test_invalid():
    assert validate("-255.0.0.0") == False
    assert validate("255.321.0.0") == False
    assert validate("255.0.-2.0") == False
    assert validate("255.0.0.-20") == False
    assert validate("-255.-2.-2.-2") == False
    assert validate("0.0.0") == False
    assert validate("cat") == False
    assert validate("000.001.010.100") == False


if __name__ == "__main__":
    main()
