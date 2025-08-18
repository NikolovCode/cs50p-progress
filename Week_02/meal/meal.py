def main():

    t = input("What is the time: ")
    final_hour = convert(t)

    if 7 <= final_hour <= 8:
        print("breakfast time")
    elif 12 <= final_hour <= 13:
        print("lunch time")
    else:
        print("dinner time")
def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes) / 60
    final_hour = hours + minutes
    return final_hour


if __name__ == "__main__":
    main()
