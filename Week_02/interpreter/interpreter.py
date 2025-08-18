def main():
    exp = input("Enter an expression: ")
    calculate(exp)


def calculate(numbers):
    x, y, z = numbers.split(" ")
    x = int(x)
    z = int(z)
    if y == "+":
        result = x + z
        print(f"{result:.1f}")
    elif y == "-":
        result = x - z
        print(f"{result:.1f}")
    elif y == "/":
        result = x / z
        print(f"{result:.1f}")
    elif y == "*":
        result = x * z
        print(f"{result:.1f}")
main()
