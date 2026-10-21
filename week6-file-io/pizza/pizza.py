import sys
import csv
from tabulate import tabulate


table = []


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command line arguments")
else:
        file = sys.argv[1]
        try:
            if not file.endswith(".csv"):
                sys.exit("Not a csv file")
            else:
                with open(file) as file:
                    reader = csv.reader(file)
                    for row in reader:
                        table.append(row)
                    print(tabulate(table,tablefmt = "grid", headers = "firstrow"))

        
        except FileNotFoundError:
            sys.exit("File not found")