usr = input("Input: ")
dict = {"apple": 130, "avocado": 50, "sweet cherries": 100, "pear": 100, "kiwifruit": 90}
k = usr.lower()
if k in dict:
    print(f"Calories: {dict[k]}")
