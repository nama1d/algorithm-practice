T = int(input())

for i in range(T):
    
    R, S = input().split()
    R = int(R)
    P = []

    for j in range(len(S)):
        P.append(S[j] * R)

    print("".join(P))