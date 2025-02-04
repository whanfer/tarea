word = input("write a word: ")

top = len(word)
right = 0
lef = top - 1

while right <= lef:
    if word[right] == word[lef]:
        right += 1
        lef -= 1
    else:
        print("no es palindroma")
        break
else:
    print("es palindroma")
