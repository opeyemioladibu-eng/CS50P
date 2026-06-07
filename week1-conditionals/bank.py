def main():
    greeting = input("Good Day....?").casefold().strip()
    print(value(greeting))


def value(greet):
    if greet.startswith("hello"):
        return("You receive $0")
    elif greet.startswith("h"):
        return("You receive $20")
    else:
        return("You receive $100")


if __name__ == "__main__":
    main()
