s = int(input())
file_names = [input() for i in range(s)]
pattern = list(file_names.pop(0))

for file in file_names:
    for i in range(len(file)):
        if pattern[i] != file[i]:
            pattern[i] = "?"

print("".join(pattern))