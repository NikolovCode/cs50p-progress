import inflect

def main():
    p = inflect.engine()
    names = []
    get_names(names)
    result = p.join(names)
    print(f"Adieu, adieu, to {result}")

def get_names(n):
    while True:
        try:
            name = input("")
            n.append(name)

        except EOFError:
            if len(n) >= 1:
                return n
main()
