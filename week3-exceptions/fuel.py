def get_positive_fraction():
    while True:
        try:
            user_input = input("Enter fuel amount in fraction[positive integers only]:")
            numerator_str, denominator_str = user_input.split('/')
            x = int(numerator_str)
            y = int(denominator_str)

            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError

            percentage = round((x/y) * 100)
            if percentage <=1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")

        except (ValueError, ZeroDivisionError):
            pass


get_positive_fraction()