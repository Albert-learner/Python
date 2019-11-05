import math, time

n = int(input(">> 자연수를 입력하세요 : "))
print("n = ", n)

start_time = time.time()
print("start time = ", start_time)
root = int(math.sqrt(n))

for i in range(2, root+1):
    if n % i == 0:
        print("{}은 {}로 나누어 떨어집니다.".format(n, i))
        break
    else:
        print("{}은 소수입니다.".format(n))
        break
print("\nending time = ", time.time())
print("계산에 걸린 시간 : ", time.time() - start_time)
