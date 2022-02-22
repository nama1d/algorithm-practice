c = int(input())

for i in range(c):

    score = list(map(int,input().split()))
    num_student = score.pop(0)
    average = sum(score) / num_student
    count = 0

    for j in range(num_student):

        if score[j] > average:
            count += 1

    print(f"{count/num_student*100:.3f}%")
