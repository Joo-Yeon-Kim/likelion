# 제어문 - 분가문
# if(조건):

# 예제 - 1

# 85점 이상 PASS, FAIL

score = int(input("input the score: "))

if (score>=85):
    print("PASS")
else:
    print("FAIL")


# 예제 - 2

activity = input("Your club? ")

if(activity=="likelion"):
    print("Me too")
else:
    print("Ok")
    

# 예제 - 3

# 5000이상: 아웃백 / 3000이상: 학식 / 1000이상: 컵라면 / ㅠㅠ: 공기밥

money = int(input("돈 얼마 있어? "))

if(money>=5000):
    print("아웃백가자")
elif(money>=3000):
    print("학식 먹자")
elif(money>=1000):
    print("컵라면 먹자")
else:
    print("공기밥")
