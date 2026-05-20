result = ""
user_input = input("Enter Input:").casefold()
for i in user_input:
    if i not in "aeiou":
        result += i


print(result)
