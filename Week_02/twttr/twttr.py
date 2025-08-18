def main():
    s = input("Input: ")
    l = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    print(f"Output: {change(s, l)}")
def change(s, l):
    result = ""
    for c in s:
        if c not in l:
            result += c
    return result
main()
