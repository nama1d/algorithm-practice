num_list = [int(input()) for i in range(9)]
max_num = max(num_list)

print(max_num, num_list.index(max_num)+1, sep="\n")