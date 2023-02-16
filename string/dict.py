# 초기화
a_dict = dict()
print(a_dict)

# 삽입
a_dict["a"] = 1
print(a_dict)

# key 중복 불가
a_dict["a"] = 2

# 탐색
print(a_dict["a"])
# print(a_dict["b"])

# 탐색2
print(a_dict.get("a"))
print(a_dict.get("b"))
# 탐색할떄는 get로 쓸것!!

a_dict["b"] = 2

# key 전부
print(a_dict.keys())
print(dir())
# key를 가져다 쓰고 싶으면 list로 치환해서 사용할것
print(list(a_dict.keys()))

# value 전부
print(a_dict.values())
# 쓰고 싶으면
print(list(a_dict.values()))

# key-value 쌍 전부
print(a_dict.items())
# 이용할때 리스트 사용