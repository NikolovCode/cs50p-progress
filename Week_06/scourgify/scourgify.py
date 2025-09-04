import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        filename = sys.argv[1]
        if not filename.lower().endswith(".csv"):
            sys.exit("Not a csv file")
        else:
            read_csv(filename)
def read_csv(f):
    with open (f) as before:
        reader = csv.DictReader(before)
        with open (sys.argv[2], 'w', newline = '') as after:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(after, fieldnames = fieldnames)
            writer.writeheader()
            for row in reader:
                first_last = row["name"]
                house = row["house"]
                last_name, first_name = first_last.split(", ")
                writer.writerow({'first': first_name, 'last': last_name, 'house': house})
main()


