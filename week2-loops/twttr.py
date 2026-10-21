result = ""
user_input = input("Enter Input:")
for i in user_input:
    if i.casefold() not in "aeiou":
        result += i


print(result)
