a=int(input("입력 진수 결정(16/10/8/2):"))

b=input("값 입력:")

c=int(b, a)

print("16진수 ==> ",hex(c))
print("10진수 ==> ",c)
print("8진수 ==> ",oct(c))
print("2진수 ==> ",bin(c))
