def main():
    while True:
        try:
            user_input = input("Enter Fuel Amount in fraction [positive integers only]:")
            percentage = convert(user_input)
            print(gauge(percentage))
            break
        except(ValueError, ZeroDivisionError):
            pass


def convert(fraction):
            numerator_str, denominator_str = fraction.split('/')
            x = int(numerator_str)
            y = int(denominator_str)

            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            percentage = round((x/y) * 100)
            return percentage


def gauge(percentage):
    if percentage <= 1:
        return("E")
    elif percentage >= 99:
        return("F")
    else:
        return(f"{percentage}%")


if __name__ == "__main__":
    main()