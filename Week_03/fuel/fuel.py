def main():
    fuel = get_int("Enter fuel level: ")
    if fuel >= 99:
        print("F")
    elif fuel <= 1:
        print("E")
    else:
        print(f"{fuel}%")
def get_int(prompt):
    while True:
        try:
            f = input(prompt)
            x, y = f.split("/")
            x = int(x)
            y = int(y)
            result = (x/y)*100
            if 0 <= result <= 100:
                return round(result)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
main()
