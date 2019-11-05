inls=input().split()
first=int(inls[0])
second=int(inls[1])

if first>second:
    print('difference is {0}'.format(first-second))
elif second>first:
    print('difference is {0}'.format(second-first))
else:
    print('difference is {0}'.format(first-second))
    
