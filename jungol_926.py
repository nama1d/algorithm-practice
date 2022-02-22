first_array = [list(map(int, input().split())) for i in range(2)]
second_array = [list(map(int, input().split())) for i in range(2)]

for i in range(2):
    print([first_array[i][j]*second_array[i][j] for j in range(4)])