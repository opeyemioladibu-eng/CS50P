import emoji


def main():
    # prompt user for str input
    user_input = input("Enter Emoji in str:")
    emojized_str = emoji.emojize(user_input, language="alias")
    print(f"Output: {emojized_str}")


if __name__ == "__main__":
    main()
