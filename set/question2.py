unq_items_set= {"book","pen","pencil","marker","notebook"}
unq_items_set.add("sticky notes")
print(unq_items_set)

unq_items_set.add("pen")
print(unq_items_set)

new_items=["highlighter","chart paper"]
unq_items_set.update(new_items)
print(unq_items_set)

unq_items_set.remove("pen")
print(unq_items_set)

unq_items_set.discard("eraser")
print(unq_items_set)

pop_item= unq_items_set.pop()
print(pop_item)
print(unq_items_set)

