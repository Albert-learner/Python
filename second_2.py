print('년도 입력 : ', end='')
year=int(input())

if year%400 == 0 or year%4 == 0 and year%100 != 0:
    print('Leap year')
else:
    print('not Leap year')
    
