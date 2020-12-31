str = input()
cnt = 0

str = str.strip()

if (len(str) == 0): # 공백만 입력된 경우
    print(0)
    exit(0)

for i in str:
    if(i == " "):
        cnt += 1

print(cnt + 1)

# n = input().split() # my name is juyeong -- split --> ['my', 'name', 'is', 'juyeong']
# print(len(n))
