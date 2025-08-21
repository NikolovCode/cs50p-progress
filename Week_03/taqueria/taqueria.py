def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    final = get_order(menu)
    print(f"\nTotal: ${final:.2f}")

def get_order(d):
    result = 0
    while True:
        try:
            item = input("Item: ")
            item = item.title()
            if item in d:
                price = d.get(item)
                result += price
                print(f"Total: ${result:.2f}")
        except KeyError:
            pass
        except EOFError:
            return result


main()
