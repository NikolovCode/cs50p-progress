def main():
    di = {}
    get_grocery(di)
    sorted_items = sorted(di)

    for key in sorted_items:
        print(f"{di[key]} {key}")
def get_grocery(d):
    while True:
        try:
            item = input("").upper()
            d[item] = d.get(item, 0) + 1
        except EOFError:
            return d
main()

