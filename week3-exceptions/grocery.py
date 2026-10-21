groceries = {}

while True:
    try:
        item = input().strip().upper()
        if item:  # Ensures empty inputs aren't counted
            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1
    except EOFError:
        break

for item in sorted(groceries.keys()):
    print(f"{groceries[item]} {item}")
