def main():
    user_input = (input("Enter Word:"))
    print(shorten(user_input))

def shorten(word):
    result = ""
    for char in word:
        if char not in "aeiouAEIOU":
            result += char
    return(result)


if __name__ == "__main__":
    main()
