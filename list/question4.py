list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

combined_list = list_1 + list_2
print("Combined list:", combined_list)

list_1.extend(list_2)
print("Extended list_1:", list_1)

book_list = ["harry_potter", "lord_of_rings", "math"]
book_2 = ["math", "science", "history"]

book_list.extend(book_2)
print("After extending:", book_list)

book_list.sort()
print("Ascending order:", book_list)

book_list.sort(reverse=True)
print("Descending order:", book_list)

book_list.sort(key=len)
print("Sorted by length:", book_list)

book_copy = book_list.copy()
book_copy.append("the_hobbit")

print("Original list:", book_list)
print("Copied list:", book_copy)