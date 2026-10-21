menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def calculate_price():
    total = 0.00
    while True:
        try:
            order = input("Item: ").title()

            if order in menu:
                total += menu[order]
                # Print the running total immediately after each valid item
                print(f"Total: ${total:.2f}")

        except EOFError:
            print()  # Moves cursor to a new line when Ctrl-D is pressed
            break


calculate_price()
