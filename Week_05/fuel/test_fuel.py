from fuel import convert
from fuel import gauge
import pytest

def main():
    test_convert()
    test_gauge()
def test_convert():
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("1/1") == 100
    assert convert("0/1") == 0
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("-1/3")
    with pytest.raises(ValueError):
        convert("1/-3")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(45) == "45%"

if __name__ == "__main__":
    main()
