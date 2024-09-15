my_dict = {"Daniil": 2005, "DJ": 1995}
print(my_dict)
print(my_dict["Daniil"])
print(my_dict.get("Dima",
                  "Такого нет в наличии "))
my_dict.update({"Nikita": 1234567,
                "Jordan": 7654321})
birthday = my_dict.pop('DJ')
print(birthday)
print(my_dict)
my_set = {1, 23, 456, "Daniil"}
print(my_set)
my_set.add(7890)
my_set.add((12, 13))
my_set.update([111, (12, 13)])
my_set.discard(1)
print(my_set)