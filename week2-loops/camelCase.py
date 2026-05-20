results = ""
user_input = input("Enter word in camelCase:")
for u in user_input:
    if u.isupper():
        results += "_" + u.lower()
    else:
        results += u


print(results)
        
