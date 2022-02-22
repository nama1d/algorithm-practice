word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=' ,'z=']

for alp in croatia:
    word = word.replace(alp, "*")

print(len(word))
            