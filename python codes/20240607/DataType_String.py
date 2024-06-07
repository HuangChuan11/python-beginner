# 1 string可以被indexing和slicing
# indexing starts from 0
print("hello")
print("hello"[1])
#      01234
# print("hello"[5])
# error : string index out of range

myString = "hello"
print(myString[0])
print(myString[1])
print(myString[2])
print(myString[3])
print(myString[4])

# reverse
print(myString[-1])
print(myString[-2])
print(myString[-3])
print(myString[-4])
print(myString[-5])
# print(myString[-6])  # out of string

# slicing
# string[start(包含該index): end(不包含在內): stepsize(可不填)]
x = "abcdefg"
print(x[2:])  # 若:後不填，則跑完
print(x[:4])  # 反之，跑到指定index為止(不含index)
# print(x[1, 2]) 和JS不一樣，要用 ":"而非 ","不然會和tuple衝突

# stepsize(可不填，預設0，可為負(reverse效果)
print(x[::-1])
print(x[::2])  # 找偶數位 index 0,2,4,6
print(x[1::2])  # 從index 1 開始跑，每次2位，就變成奇數位 index 1,3,5
