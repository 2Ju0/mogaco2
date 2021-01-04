""" 표준 입출력 """
print("Python", "Java", sep = ",", end = "?") # sep (seperate) : 띄어쓰기 부분을 대체하는 문자열
print("무엇이 더 재밌을까요?") # end : 문자열의 끝부분을 대체하는 문자열 / 줄바꿈 없이 출력

import sys
print("Python", "Java", file = sys.stdout) # 표준 출력
print("Python", "Java", file = sys.stderr) # 표준 에러

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust(8) : 8개의 공간을 만들고 왼쪽 정렬 / rjust(4) : 4개의 공간을 만들고 오른쪽 정렬

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # zfill(3) : 3크기 만큼의 공간을 확보하고 값이 없는 빈 공간에 대해서는 0으로 채운다

answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) # 사용자 입력 형태로 값을 받으면 항상 '문자열' 형태로 저장된다. 
print("입력하신 값은 " + answer + "입니다.")

""" 다양한 출력포맷 """
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500)) 
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500)) 
print("{0: >+10}".format(-500)) 
# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500)) 
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(10000000000))
# 3자리 마다 콤마를 찍어주고, 부호도 붙이고, 자릿수 확보, 빈자리는 ^로 채우기
print("{0:^<+30,}".format(10000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))

""" 파일 입출력 """
score_file = open("score.txt", "w", encoding="utf8") # 파일 열기
print("수학 : 0", file=score_file) # 내용을 파일에 쓰기
print("영어 : 50", file=score_file)
score_file.close() # 파일 닫기

score_file = open("score.txt", "a", encoding="utf8") # a (append) : 이미 존재하는 파일에 쓰기
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") # 줄바꿈 명시적으로 작성 필요
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # 파일 읽기
print(score_file.read()) # 모든 내용 읽기
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="") 
print(score_file.readline(), end="") 
print(score_file.readline(), end="") 

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end = "")

score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end = "")

score_file.close()

""" pickle """
import pickle
profile_file = open("profile.pickle", "wb") # wb : write, binary / encoding 설정 필요 없음
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile 에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러온다.
print(profile)
profile_file.close()

""" with """
with open("profile.pickle", "rb") as profile_file: # profile.pickle을 열고 profile_file에 저장
    print(pickle.load(profile_file)) # with문 탈출하면서 자동 종료하므로 close 할 필요 없음

with open("study.txt", "w", encoding="utf8") as study_file:
     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

"""
Quiz) 당신의 회사에서는 매주 1회 작성해야하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X 주차 주간보고 -
부서 :
이름 : 
업무 요약 :

1주차 부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.
"""
for i in range(1,51):
    with open(str(i)+"주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")
