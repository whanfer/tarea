word = input("write a word: ")

for a, b in zip(word, reversed(word)):
    if a != b:
        print("no es palindroma")
        break
else:
    print("es palindroma")

