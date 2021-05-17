# 문자열 ( 내장함수)

str = "멋쟁이 사자처럼"

# 인덱싱
print(str[4])

# 슬라이싱
# [x:y] --> x번째 인덱스부터 y인덱스 "전까지"
print(str[0:4])

# 문자열의 길이 : len(문자열 변수)
print(len(str))

# 문자열 내에서 특정 문자의 등장 횟수: 문자열 변수.count('특정문자')
print(str.count('사'))

# 문자열을 (특정 기준으로) 나누기: 문자열 변수.split()
print(str.split())  # 공백 기준으로 나누겠다
str2 = "멋'쟁이' 사자처'럼"
print(str2.split("'"))

# 특정 문자 인덱스 찾기: find('문자'), index('문자')
# 찾고자 하는 문자가 "없을 때" 차이 있음
print(str.index('사'))

