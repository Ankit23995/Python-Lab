shopping_list = ["rice", "oil", "salt", "sugar"]

print("First item:", shopping_list[0])
print("Last item:", shopping_list[-1])

shopping_list.append("tea")
shopping_list.insert(1, "milk")
shopping_list.remove("salt")

removed_item = shopping_list.pop()

print("Removed item:", removed_item)
print("Updated shopping list:", shopping_list)
print("Total number of items:", len(shopping_list))
print("Shopping items:", ", ".join(shopping_list))
