'''
from random import *

 i = randint(1, 100)  # 1부터 100 사이의 임의의 정수
print(i)
 
f = random()   # 0부터 1 사이의 임의의 float
print(f)
 
f = uniform(1.0, 36.5)   # 1부터 36.5 사이의 임의의 float
print(f)
 
i = randrange(1, 101, 2) # 1부터 100 사이의 임의의 짝수
print(i)
 
i = randrange(10)  # 0부터 9 사이의 임의의 정수
print(i)
'''
import random

def lotto_number(): # 난수 생성 함수
    num_list = [] # 6개의 추첨 번호를 넣을 리스트

    for i in range(6): # 6번 for문을 돌면서
        num = random.randint(1,45) # num 변수에 1~45 사이의 난수 생성
        while num in num_list: # 만약 num_list 안에 방금 생성한 난수가 존재하면
            num = random.randint(1,45) # 다시 난수 생성
        num_list.append(num) # 중복되지 않는다면 num_list에 추가함.
    
    bonus_num = random.randint(1,45) # bonus 숫자
    while bonus_num in num_list: # 보너스 숫자 또한 앞에서 뽑은 6개의 수에 중복되지 않게 while 문을 통해 난수 생성
        bonus_num = random.randint(1,45)

    return num_list, bonus_num #6개의 추첨 번호 리스트와 보너스 번호 반환

def print_lotto_number(lotto_num, bonus_num):
    print(lotto_num, end=' + ') # 6개의 추첨 번호 리스트 출력 후, 끝에 줄바꿈이 아닌 + 출력
    print(bonus_num) # bonus 번호 출력

def check_number(user_num):
    num_count = 0 # 6개의 추첨 번호에서 몇 개가 일치하는지 카운트 하기 위한 변수
    bonus_count = 0 # 사용자가 입력한 6개의 번호중 보너스 번호가 있는지 카운트하기 위한 변수(1 또는 0)
    for num in user_num: #사용자가 입력한 6개의 번호 리스트를 차례대로 순회 ex) [2, 1, 4, 3, 6, 5]
        if num in lotto_numbers: # 만약 추첨한 6개의 번호 중 사용자가 선택한 번호가 있으면 num_count + 1
            num_count += 1
        if num == bonus_number: # 사용자가 선택한 번호들의 리스트를 순회하며 보너스 번호가 있으면 bonus_count = 1
            bonus_count = 1
    
		#추첨 번호들과 사용자가 선택한 번호를 모두 확인 후
    if num_count == 6: #당첨번호 6개 숫자일치
        print("1등")
    elif num_count == 5: #당첨번호 5개 숫자일치하고
        if bonus_count == 1: #보너스 번호도 일치
            print("2등")
        else: #보너스 번호는 불일치
            print("3등")
    elif num_count == 4: #당첨번호 4개 숫자일치
        print("4등")
    elif num_count == 3: #당첨번호 3개 숫자일치
        print("5등")
    else:
        print("복권 하나 더 사!")

lotto_numbers = []
bonus_number = 0

while(True):
    print("1. 로또 번호 추첨")
    print("2. 번호 당첨 확인")
    print("3. 종료")
    mode = int(input("실행할 번호를 입력 : "))
    if (mode == 1):
        lotto_numbers, bonus_number = lotto_number()
        print_lotto_number(lotto_numbers, bonus_number)
    
    elif (mode == 2):
        user_number = []
        for i in range(6):
            user_input = int(input("1 ~ 46 사이의 번호를 입력해주세요: "))
            user_number.append(user_input)
        check_number(user_number)

    elif (mode == 3):
        print("프로그램 종료")
        break

