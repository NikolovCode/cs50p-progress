due = 50
owed = 0
while due > 0:
    incert = int(input("Inser a coin: "))
    if incert == 5 or incert == 10 or incert == 25:
        due -= incert
        if due > 0:
            print(f"Amount due: {due}")
    else:
        due = 50
        print(f"Amount Due: {due}")
if due <= 0:
    print(f"Change Owed: {abs(due)}")
