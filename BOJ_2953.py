score_list =[]

for i in range(5):
    score_list.append(sum(map(int,input().split())))

max_score = max(score_list)
print(score_list.index(max_score)+1, max_score)