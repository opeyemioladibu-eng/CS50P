deep_question = input("What is the answer to the Great Question of Life, the Universe and Everything ?").lower().strip()
if deep_question not in ["42", "forty two", "forty-two"]:
    print("No")
else:
    print("Yes")
