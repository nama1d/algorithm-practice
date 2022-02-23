chess = [list(input()) for i in range(8)]
count = 0

for i in range(8):
    if i %2 == 0:
        for j in range(0,8,2):
            if chess[i][j] == "F":
                count += 1
    if i%2 == 1:
        for j in range(1,8,2):
            if chess[i][j] == "F":
                count += 1

print(count)

# chess = [list(input()) for i in range(8)]
# count = 0

# for i in range(8):
#     for j in range(8):
#         if i % 2 == j % 2 and chess[i][j] == "F":
#             count += 1

# print(count)