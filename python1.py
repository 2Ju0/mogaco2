# 변수
name = "kong"
animal = "dog"
age = 1
hobby = "walking"
is_adult = age >=3

print("우리집" + animal +"의 이름은" + name +"입니다.")
print(name + "이는" + str(age) + "살 이며 " + hobby +"을 좋아합니다.")
print(name + "이는 어른인가요?" + str(is_adult))

# 주석
''' 
이렇게 하면 여러문장이 주석처리 됩니다
문장1 
문장2
'''

# 연산자  
print((3>0) and (3<5)) # &와 동일
print(not(1<3)) # 부정연산
print((3>0) or (3<5)) # |와 동일

# 숫자 처리 함수
print(abs(-5)) # abs : 절댓값 반환
print(pow(4,2)) # 4^2 = 16
print(max(5,12)) # max : 최댓값 반환
print(min(5,12)) # min : 최솟값 반환
print(round(3.14)) # round : 반올림 값 반환

from math import * # math library 안의 모든 함수 사용
print(floor(4.99)) # 내림 : 4
print(ceil(3.14)) # 올림 : 4
print(sqrt(16)) # 제곱근 : 4 

# 랜덤 함수
from random import *
print(random()) # 0.0 이상 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 이상 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 이상 10미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 이상 10 이하의 임의의 값 생성
print(int(random()*45) + 1) # 1 이상 45 이하의 임의의 값 생성

print(randrange(1, 45)) # 1이상 45 미만의 임의의 값 생성
print(randrange(1, 46)) # 1이상 46 미만의(45 이하의) 임의의 값 생성

print(randint(1,45)) # 1이상 45 이하의 임의의 값 생성

# 문자열
sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3)

# 슬라이싱
jumin = "000728-0000000"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 (0,1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤 부터) : " + jumin[-7:])

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) # 콤마 뒤 : 찾기 시작 위치
print(python.find("Java")) # 원하는 것이 없다면 -1 반환
#print(python.index("Java")) # 원하는 것이 없다면 오류

# 문자열 포맷
# 방법1)
print("나는 %d살 입니다." %20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요" % "A")
#s
print("나는 %s살 입니다" %20) # %s하면 모두 가능
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법2)
print("나는 {}살입니다.".format(20))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간")) # 중괄호 안의 숫자 : format 뒤의 문자열 순서 정하기
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법3)
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))

# 방법4)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.") # f로 문자열을 시작하면 변수의 값을 가져와서 출력

# 탈출 문자
print("백문이 불여일견 \n 백견이 불어일타") # \n : 줄바꿈
print("저는 \"나도코딩\" 입니다.") # \" \" : 문장 내에서 큰따옴표 역할
print("C:\\Users\\lge25\\OneDrive\\바탕 화면\\PythonWorkspace>") # \\ : 문장내에서 \
print("Red Apple\rPine") # \r : 커서를 맨 앞으로
print("Redd\bApple") # \b : 백스페이스 (한 글자 삭제)
print("Red\tApple") # \t : tab 역할

"""
# Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

예) http://naver.com
규칙1: http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
                (nav)               (5)             (1)        (!)
예) 생성된 비밀번호 : nav51!
"""
url = "http://naver.com"
my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url,password))
