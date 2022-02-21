# 슬라이싱만 사용하여 풀이

word = input()

if word[::-1] == word:
     print("1")
else:
     print("0")

# print(1 if word == word[::-1] else 0)
# print(int(word == word[::-1]))


# 반복문만 사용하여 풀이
word = input()
reversed_word = ""

for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]

if word == reversed_word:
    print(1)
else:
    print(0)
