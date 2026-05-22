groceries = {}


while True:
    try:
        item = input("Enter Item: ").upper()
    #If item already in dictionary, add 1
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1
    except EOFError:
        break
    
        
for items in sorted(groceries):
    print(f"{groceries[items]} {items}")