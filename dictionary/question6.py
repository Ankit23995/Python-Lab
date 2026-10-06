translation_dict = {
    "hello": "hola",
    "thank you": "gracias",
    "goodbye": "adios"
}
word = input("Enter an English word: ").lower()
print(translation_dict.get(word, "Translation not found"))
