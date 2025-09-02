import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        filename = sys.argv[1]
        if not filename.lower().endswith(".csv"):
            sys.exit("Not a csv file")
        else:
            print(make_table(sys.argv[1]))

def make_table(f):
    try:
        with open(f) as file:
            reader = csv.reader(file)
            headers = next(reader)
            table = []
            for row in reader:
                table.append(row)
            return (tabulate(table, headers, tablefmt = "grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")
main()
