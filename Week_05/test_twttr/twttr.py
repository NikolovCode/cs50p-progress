import sys
def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")
def shorten(word):
    l = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    result = ""
    for c in word:
        if c not in l:
            result += c
    return result
if __name__ == "__main__":
    main()
