# left, right = input().split("(^0^)")
# count_l, count_r = 0,0

# for i in range(len(left)):
#     if left[i] == "@":
#         count_l += 1

# for i in range(len(right)):
#     if right[i] == "@":
#         count_r += 1

# print(count_l, count_r)

left, right = input().split("(^0^)")
print(left.count("@"), right.count("@"))