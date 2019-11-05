ls=[10, 20, 30, 40, 50]

'''
sum=0
for i in ls:
    sum+=
print(sum)
'''

'''
for i in range(2, 10, 2):
    print(i)
'''

'''
n=int(input())
sum=0

for i in range(1, n+1):
    sum+=i
print(sum)
'''

'''
for var in range(1, 10):
    for dan in range(2, 10):
        print('{0}*{1}={2}\t'.format(dan, var, dan*var),end='')
    print()
'''

'''
print('개수 입력 : ', end='')
count=int(input())
'''

'''
for i in range(0, count):
    for j in range(0, count):
        print('*', end='')
    print()
'''

'''
for i in range(0, count+1):
    for j in range(0, i):
        print('*', end='')
    print()
'''

'''
for i in range(count, 0, -1):
    for j in range(i):
        print('*', end='')
    print()
'''

dic={}
dic[100]='hong'
dic[200]='kang'
dic[300]='park'

for i in dic.keys():
    print('{0} : {1}'.format(i, dic[i]))
print()

for k, v in dic.items():
    print('{0} : {1}'.format(k, v))
