def main():
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    deep(answer.lower().strip())

def deep(s):
    if s == "42" or s == "forty-two" or s == "forty two":
        print("Yes")
    else:
        print("No")

main()
