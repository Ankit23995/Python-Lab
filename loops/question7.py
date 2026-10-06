def change_string(string):
    words = string.split()
    result = []

    for word in words:
        new_word = ""

        for i in range(len(word)):
            current = word[i]

            if i == 0:
                new_word += current.upper()
            elif word[i - 1].lower() < current.lower():
                new_word += current.upper()
            elif word[i - 1].lower() > current.lower():
                new_word += current.lower()
            else:
                new_word += current

        result.append(new_word)

    return " ".join(result)


string = input("Enter a string: ")
print(change_string(string))
