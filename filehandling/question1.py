import os

path = os.path.expanduser("~/Desktop/python.txt")

with open(path, "w") as file:
    file.write("Python is a powerful and easy-to-learn programming language. "
               "It is widely used for web development, data science, automation, "
               "artificial intelligence, and many other applications.")



import os

path = os.path.expanduser("~/Desktop/python.txt")

with open(path, "a") as file:
    file.write("\nI will learn Error Handling Next")


import os

python_path = os.path.expanduser("~/Desktop/python.txt")
java_path = os.path.expanduser("~/Desktop/java.txt")

with open(python_path, "r") as file:
    content = file.read()

content = content.replace("Python", "Java").replace("python", "java")

with open(java_path, "w") as file:
    file.write(content)

python_size = os.path.getsize(python_path) / 1024
java_size = os.path.getsize(java_path) / 1024

print("python.txt size:", python_size, "KB")
print("java.txt size:", java_size, "KB")


import re
from collections import Counter

with open("E:\projects\filehandling\nobel_prize_speech.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

words = re.findall(r"\b[a-z]+\b", text)
most_repeated = Counter(words).most_common(1)

print(most_repeated[0][0])
