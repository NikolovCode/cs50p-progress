import math
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    chars = []
    for char in s:
        chars.append(char)
    count = len(chars)
    if count < 2 or count > 6:
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    if not s.isalnum():
        return False
    i = 0
    while i < count:
        c = s[i]
        if c.isdigit():
            if c == "0":
                return False
            if not s[i:].isdigit():
                return False
            break
        i+=1
    return True

main()
