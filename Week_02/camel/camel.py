def main():
    camel = input("Camel case: ")
    print(snake_case(camel))

def snake_case(s):
    result = ""
    for c in s:
        if c.isupper():
            result += "_" + c.lower()
        else:
            result += c
    return result
main()
