import sys
import csv


try:
    
    if len(sys.argv) >3:
        sys.exit("Too many command line arguments")

    elif len(sys.argv) < 3:
        sys.exit("Too few command line argument")

    else:
        before = sys.argv[1]
        after = sys.argv[2]
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

# open and format initial file
initialFile = []

with open(before) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last_name, first_name = row["name"].split(",")
            house = row["house"]
            initialFile.append({"first" :first_name, "last" : last_name, "house" : house})

#Open and write to new file
with open(after, "w") as newfile:
    writer = csv.DictWriter(newfile, fieldnames = {"first", "last", "house"})
    writer.writeheader()
    for row in initialFile:
        writer.writerow(row)