n, m = map(int,input().split())
ppl = {}

for i in range(n+m):
    name = input()
    if name in ppl:
        ppl[name] += 1
    else:
        ppl[name] = 1

ppl_2 =[key for key in ppl if ppl[key]==2]

print(len(ppl_2))
for j in sorted(ppl_2):
    print(j)
