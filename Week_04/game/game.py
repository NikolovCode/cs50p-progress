import random

def main():
    level = get_level()
    print(get_guess(level))

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1:
                rando = random.randint(1, level)
                return rando
        except ValueError:
            pass
def get_guess(level):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > level:
                print("Too large!")
            elif guess < level and guess > 0:
                print("Too small!")
            elif guess == level:
                return "Just right!"
        except ValueError:
            pass
main()
