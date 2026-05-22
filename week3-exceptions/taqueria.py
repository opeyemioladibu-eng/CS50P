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
                    order = input("Order:").title()
            #check if item is in menu(case sensitive)
                    if order in menu:
                        total += menu[order]
            #print total formatted to 2 decimal place
                        print(f"${total:.2f}")
            #if not in menu do nothing 
                    elif order not in menu:
                        pass
                except EOFError:
                    break
                
                
calculate_price()
    
            