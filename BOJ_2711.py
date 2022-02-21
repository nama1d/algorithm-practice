T = int(input())

for i in range(T):
    num, word = input().split()
    num = int(num)
    changed_word = word[:num-1] + word[num:]
    print(changed_word)