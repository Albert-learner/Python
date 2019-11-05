import time, math

n = int(input("자연수를 입력하세요 : "))
print("n = ", n)

start_time = time.time()
print("start time = ", start_time)
flag = 0


for i in range(2, n):
    if n % i == 0:
        print("{}은 {}로 나누어 떨어집니다.".format(n, i))
        flag = 1
    break

if flag == 1:
    print("{}은 소수입니다.".format(n))
else:
    print(("{}은 소수가 아닙니다.".format(n)))

print("\nending time = ", time.time())
print("계산에 걸린 시간 : ",  time.time() - start_time)
