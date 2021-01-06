""" 클래스 / __init__ """
# 마린  : 공격 유닛, 군인. 총을 쏠 수 있음
name = "마린" # 유닛의 이름
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반모드 / 시즈모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력 {2}]".format( \
        name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

# 일반 유닛
class Unit:
    def __init__(self, name, hp, damage): # 생성자 (객체 생성 시 자동 호출) : self 제외 매개변수 개수 맞춰 객체 생성
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

""" 멤버변수 """
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1. name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2. clocking = True # 객체의 변수를 외부에서 추가로 생성하여 사용 가능

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

""" 메소드"""
# 공격 유닛
class AttackUit:
        def __init__(self, name, hp, damage): # self : 자기 자신
            self.name = name
            self.hp = hp
            self.damage = damage
        
        def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
                .format(self.name, location, self.damage))

        def damaged(self, damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

""" 상속 """
# 일반 유닛
class Unit1: # 부모 클래스
    def __init__(self, name, hp, speed): 
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit1(Unit1): # 자식 클래스
    def __init__(self, name, hp, speed, damage): 
        Unit1.__init__(self, name, hp, speed)
        self.damage = damage

""" 다중 상속  / 메소드 오버라이딩 """
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit1, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit1.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 발키리 : 공중 공격 유닛
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

""" 메소드 오버라이딩 """
vulture = AttackUnit1("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")

""" pass """
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass # 아무것도 하지 않고 넘어감

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()

""" super """
class BuildingUnit(Unit1):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # super를 사용하면 괄호사용 + self 미작성
        self.location = location

# 다중상속 주의
class Unit2:
    def __init__(self):
        print("Unit 생성자")
    
class Flyable2:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit2, Flyable2): # 다중상속
    def __init__(self):
        # super().__init__() # 다중상속 시 super()를 사용하면 마지막에 상속받는 class에 대해서만 init 함수가 호출된다.
        Unit2.__init__(self)
        Flyable2.__init__(self)

dropship = FlyableUnit()

"""
Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

(출력 예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

[코드]
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        pass

    # 매물 정보 표시
    def show detail(self):
        pass
"""

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/10", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()

""" 예외처리 """
try:
    print(" 나누기 전용 계산기 입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)

""" 에러 발생 / 사용자 정의 예외처리 / finally """
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg
try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.") # 무조건 출력


""" 
Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
        출력 메시지 : "잘못된 값을 입력하였습니다."
조건 2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정 
        치킨 소진 시 사용자 정의 에러 [SoldOutError]를 발생시키고 프로그램 종료
        출력 메시지 :  "재고가 소진되어 더 이상 주문을 받지 않습니다."
"""
class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작
while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken: # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다." \
                .format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
