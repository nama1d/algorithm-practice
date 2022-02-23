n = int(input())
city = {}

for i in range(n):
    key, value = input().split()
    city[key] = value

print(city.get(input(),"Unknown Country"))

