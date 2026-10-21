def main():
    greeting = input("Greeting:")
    print(f"You receive ${value(greeting)}")

 
def value(greet):
    greet = greet.strip().casefold()
    if greet.startswith("hello"):
        return 0
    elif greet.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()