electronic_gadget_top={"ram","shyam","sita","hari"}
cosmetic_top={"hari","sita","gita","rita"}
grocery_top={"ram","hari","gita","rabi"}

top_of_all=electronic_gadget_top & cosmetic_top &  grocery_top
print(top_of_all)

atleast_one_top= electronic_gadget_top | cosmetic_top |  grocery_top
print(atleast_one_top)

electronic_but_no_cos= electronic_gadget_top - cosmetic_top
print(electronic_but_no_cos)

electronic_and_cos = electronic_gadget_top | cosmetic_top
print(electronic_and_cos)

electronic_and_grocery=electronic_gadget_top & grocery_top
print(electronic_and_grocery)

exactly_one= electronic_gadget_top-grocery_top-cosmetic_top | cosmetic_top-grocery_top-electronic_gadget_top | grocery_top-cosmetic_top-electronic_gadget_top
print(exactly_one)

exactly_two = (electronic_gadget_top & cosmetic_top )- grocery_top | electronic_gadget_top & grocery_top - cosmetic_top | grocery_top & cosmetic_top - electronic_gadget_top
print(exactly_two)

