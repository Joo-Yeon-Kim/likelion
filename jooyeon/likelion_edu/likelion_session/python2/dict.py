# 딕셔너리 (내장함수)

pairs = {'잔나비' : '뜨거운 여름밤은 가고', '소희' : '산책', '홍크' : '어쩌면'}

# 하나의 key-value 쌍을 추가하는 방법
# 딕셔너리형 변수[key] = value
print(pairs)

pairs['스탠딩 에그'] = '휴식'

print(pairs)


# 특정 key-value 삭제하는 방법 : del 함수
# del 변수[키]
del pairs['잔나비']
print(pairs)

# key로 value 얻기 : 변수.get('key')

v = pairs.get('스탠딩 에그')
print(v)
