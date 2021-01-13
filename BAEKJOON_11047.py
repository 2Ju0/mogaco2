lst = []
result = 0
num = list(map(int, input().split()))
for i in range(num[0]):
    lst.append(int(input()))
lst.reverse()

for i in lst:
    if(num[1] / i == 0):
        continue
    result += num[1] // i
    num[1] %= i

print(result)
