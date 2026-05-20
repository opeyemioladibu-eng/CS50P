consumer_input = input("Enter desired fruit:").casefold()
fruit_list = {
    "apple" : 130,
    "avocado" : 50,
    "banana" : 110,
    "cantaloupe" : 50,
    "grapefruit" : 60,
    "grapes" : 90,
    "watermelon" : 80,
    "tangerine" : 50,
    "sweet cherries ":100,
    "strawberries" : 50,
    "plums": 70,
    "pineapple" : 50,
    "pear" : 100,
    "peach" : 60,
    "orange" : 80,
    "nectarine" : 60,
    "lime" : 20,
    "lemon" : 15,
    "kiwifruit": 90,
    "honeydew":50, 
}

calories = fruit_list.get(consumer_input)
if calories:
    print(f"Calories: {calories}")