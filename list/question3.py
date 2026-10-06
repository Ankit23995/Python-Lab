book_list = ["harry_potter", "lord_of_rings", "harry_potter", "math", "science"]

print("Position of first harry_potter:", book_list.index("harry_potter"))

book_list.remove("harry_potter")
print("After removing harry_potter:", book_list)

book = input("Enter a book name: ").lower()

if book in book_list:
    print(f"{book} is present in the list.")
else:
    print(f"{book} is not present in the list.")

book_list.append("the_hobbit")
print("After adding the_hobbit:", book_list)

book_list.insert(2, "game_of_thrones")
print("After inserting game_of_thrones:", book_list)

print("Number of lord_of_rings:", book_list.count("lord_of_rings"))

removed_book = book_list.pop(1)

print("Removed book:", removed_book)
print("Updated book list:", book_list)
print("Total number of books:", len(book_list))
print("Books:", ", ".join(book_list))
