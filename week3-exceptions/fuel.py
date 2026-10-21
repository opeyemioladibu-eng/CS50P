def get_positive_fraction():
    while True:
        try:
            user_input = input("Amount of fuel: ")
            numerator_str, denominator_str = user_input.split('/')
            x = int(numerator_str)
            y = int(denominator_str)
            
            # Check for 0 denominator, negative numbers, or if X is greater than Y
            if y == 0:
                raise ZeroDivisionError
            elif x < 0 or y < 0 or x > y:  # <--- UPDATED: Checks for negative values
                raise ValueError
                
            percentage = round((x / y) * 100)
            
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
                
            break 
            
        except (ValueError, ZeroDivisionError):
            pass

get_positive_fraction()
