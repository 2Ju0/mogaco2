str = input()
cnt = 0

if (len(str) == 0): # 아무것도 입력하지 않은 경우
    print(0)
    exit(0)

str = list(str) # list로 자료구조를 변경해야 str[0] = "" 와 같이 할당 가능
if (str[0] == " "):
    str[0] = "" 
if (str[len(str)-1] == " "):
    str[len(str)-1] = ""
str = ''.join(str) # ''를 구분자로 하여 문자열로 합치기

if (len(str) == 0): # 공백만 입력된 경우
    print(0)
    exit(0)

for i in str:
    if(i == " "):
        cnt += 1

print(cnt + 1)

# 더 좋은 알고리즘
n = input().split() # my name is juyeong -- split --> ['my', 'name', 'is', 'juyeong']
print(len(n))
