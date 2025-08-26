import random


def main():
    level = get_level()
    tasks = 0
    points = 0

    while tasks < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        fail = 1
        while True:
            try:

                s = int(input(f"{x} + {y} = "))
                if s == answer:
                    points += 1
                    tasks += 1
                    break
                elif fail == 3:
                    print(answer)
                    fail = 1
                    tasks += 1
                    break
                elif s != answer:
                    print("EEE")
                    fail += 1
            except ValueError:
                    print("EEE")
                    fail += 1
    print(f"Score {points}")
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        nums = random.randint(0, 9)
        return nums
    elif level == 2:
        nums = random.randint(10, 99)
        return nums
    elif level == 3:
        nums = random.randint(100, 999)
        return nums
    else:
        raise ValueError

if __name__ == "__main__":
    main()
