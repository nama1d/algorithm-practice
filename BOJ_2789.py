word = input()
cam = "CAMBRIDGE"

for i in word:
    for j in cam:
        word = word.replace(j, "")
        
print(word)