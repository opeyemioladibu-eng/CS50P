import validators


def main():
    user_email = str(input("What is your email? "))
    
    # validators.email() returns True if valid, else returns a ValidationFailure object
    result = validators.email(user_email)
    
    if result == True:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()