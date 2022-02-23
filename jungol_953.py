# 미완성

foul = {}
players = input().split()

for player in players:
    if player in foul:
        foul[player] += 1
    else:
        foul[player] = 1

sorted_ = sorted(foul.items(), key = lambda x : x[1])

for i in sorted_:
    if sorted_[i][1] == sorted[0][1]:
        print(sorted_[i][0])