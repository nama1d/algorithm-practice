N = int(input())

for i in range(N):
    if i % 2 == 0:
        print("* " * (N-1) + "*")
    else:
        print(" *" * N)

# 6min 