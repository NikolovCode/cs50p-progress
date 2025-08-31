def main():
    s = input("Enter fuel level: ")
    fuel = convert(s)
    print(gauge(fuel))

def convert(fraction):
    while True:
        try:
            f = fraction
            x, y = f.split("/")
            x = int(x)
            y = int(y)
            result = (x/y)*100
            if 0 <= result <= 100:
                return round(result)
        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
