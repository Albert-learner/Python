#반복문
n=int(input())

i=2
sum=0
while i<=n:
    if i%2 == 0:
        sum+=i
        i+=2
print(sum)
