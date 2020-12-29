""" 리스트 """

# subway1 = 10, subway2 = 20, subway3 = 30
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태움 : insert
subway.insert(1, "정형돈") # 리스트에 삽입 : insert(index,객체)
print(subway)

# 지하철에 있는 사람 한 명씩 뒤에서 꺼냄 : pop
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 다양한 자료형 함께 사용 가능
mix_list = ["조세호", 20, True]
print(mix_list)
  
# 리스트 확장 (하나의 리스트로 합치기) 가능
num_list.extend(mix_list)
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

""" 사전 """
cabinet = {3: "유재석", 100 : "김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
#print(cabinet[5]) # [] : 값이 없는 경우에 오류
print(cabinet.get(5)) # get : 값이 없는 경우에 None 반환
print(cabinet.get(5, "사용 가능")) # 값이 없는 경우에 문자열 반환

print(3 in cabinet) # 사전 자료형에 값이 있는지 없는지 확인 > True
print(5 in cabinet) # False

# 문자열 key도 가능
cabinet = {"A-3": "유재석", "B-100" : "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국" # 값 업데이트
cabinet["C-20"] = "조세호" # 값 추가

# 간 손님 (key 삭제)
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 모든 값 삭제
cabinet.clear()

""" 튜플 """
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# 튜플은 값 추가 및 변경 불가 > 고정된 값에 대해서만 사용 가능

name = "tom"
age = 20
hobby = "coding"
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

""" 집합 """
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) # 리스트를 set으로

# 교집합 (java와 python을 모두 할 수 있는 사람)
print(java & python)
print(java.intersection(python))

# 합집합 (java도 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊었어요
java.remove("김태호")
print(java)

""" 자료구조의 변경 """
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu)) # type을 list로 변경

menu = tuple(menu)
print(menu, type(menu)) # type을 tuple로 변경

menu = set(menu)
print(menu, type(menu)) # type을 set으로 변경

""" 
Quiz ) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
-- 당첨자 발표 -- 
치킨 당첨자 : 1
커피 당첨자 : [1, 2 ,3]
-- 축하합니다 -- 
"""
from random import *
users = range(1, 21) # 1부터 20까지 숫자를 생성 > type이 range이므로 list로 변경 필요
users = list(users)
shuffle(users)

winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피
print("-- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 -- ")

""" if """
weather = input("오늘 날씨는 어때요? > ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요")

temp = int(input("기온은 어때요? > "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")

""" for """
for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1, 5): # range(5) : 0 ~ 5
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

""" while """
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기 처분되었습니다.")

customer = "아이언맨"
index = 1
# while True: # 무한 반복
#    print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
#    index += 1

customer = "토르"
person = "Unkown"
while person != customer :
    print("{0}님, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")

""" continue, break """
absent = [2, 5] # 결석
no_book = [7] # 책을 안가져옴
for student in range(1, 11): # 출석 번호 1 ~ 10번 
    if student in absent:
        continue # continue를 만나면 다음 문장을 실행하지 않고 다음 반복으로
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

""" 한줄 for """
# 출석번호 : 1 2 3 4 / 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1,2,3,4,5]
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["iron man", "thor", "i am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["iron man", "thor", "i am groot"]
students = [i.upper() for i in students]
print(students)

""" 
Quiz) 당신은 cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[0] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[0] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분
"""
cnt = 0
for client in range(1, 51): # 1 부터 50까지의 수 (승객)
    time = randrange(5, 51) # 5분 ~ 50분 소요시간
    if 5 <= time <= 15: # 매칭 성공
        print("[O] {0}번째 손님 (소요시간 :{1}분)".format(client, time))
        cnt += 1
    else: # 매칭 실패
        print("[ ] {0}번째 손님 (소요시간 :{1}분)".format(client, time))

print("총 탑승 승객 : {0}분".format(cnt))

""" 함수 """
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): #출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance-money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다.잔액은 {0} 원 입니다.".format(balance))

def withdraw_night(balance, money):
    commission = 100 # 수수료 100원
    return commission, balance - money - commission # 여러개 값 반환 가능

balance = 0 # 잔액
balance = deposit(balance, 1000)
#balance = withdraw(balance, 500)
#balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang)) # \ + enter : 구분만하고 한줄

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 기본 값
def profile2(name, age = 17, main_lang = "python"): # age와 main_lang을 전달받지 않았을 경우 기본 값 지정
    print("이름 : {0}\t 나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))

profile2("유재석")
profile2("김태호")

# 키워드 값
def profile3(name, age, main_lang):
    print(name, age, main_lang)

profile3(name = "유재석", main_lang = "파이썬", age = 20)
profile3(main_lang = "자바", age = 25, name = "김태호")

# 가변인자
def profile4(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ") # end = " " : print문이 끝날 때 줄바꿈을 하지 않는다.
    print(lang1, lang2, lang3, lang4, lang5)

profile4("유재석", 20, "python", "Java", "C", "C++", "C#")
profile4("김태호", 25, "Kotlin", "Swift", "","","")

def profile5(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ") # end = " " : print문이 끝날 때 줄바꿈을 하지 않는다.
    for lang in language:
        print(lang, end = " ")
    print()

profile5("유재석", 20, "python", "Java", "C", "C++", "C#", "JavaScript")
profile5("김태호", 25, "Kotlin", "Swift")

# 지역변수와 전역변수
gun = 10
def checkpoint(soldiers):
    #gun = 20 # 지역 변수
    global gun # 전역 공간에 있는 gun 사용
    gun -= soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    #gun = 20 # 지역 변수
    #global gun # 전역 공간에 있는 gun 사용
    gun -= soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
#checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

"""
Quiz) 표준 체중을
* 표준 체중 : 각 개인의 키에 적당한 체중
(성별에 따른 공식)
    남자 : 키(m) x 키(m) x 22
    여자 : 키(m) x 키(m) x 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
    * 함수명 : std_weight
    * 전달값 : 키(height), 성별(gender)

조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
"""
def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height  = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
