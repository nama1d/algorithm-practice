words = [input() for i in range(5)]
max_len = max([len(word) for word in words])

changed_words = []

for word in words:
    if len(word) < max_len:
        changed_words.append(word + "*"* (max_len-len(word)))
    else:
        changed_words.append(word)


word_list = []

for i in range(max_len):
     for word in changed_words:
         word_list.append(word[i])

print("".join(word_list).replace("*",""))