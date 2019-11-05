'''
print('단 입력 : ', end='')
dan=int(input())

i=1
while i<=9:
    print('{0}*{1}={2}'.format(dan, i, dan*i))
    i+=1

print()
print()
'''
dan=2
var=1

while dan <= 9:
    while var <= 9:
        print('{0}*{1}={2}'.format(dan, var, dan*var))
        var+=1
    dan+=1
    var=1
    print()
    

while var <= 9:
    while dan <= 9:
        print('{0}*{1}={2}\t'.format(dan, var, dan*var), end='')
        dan+=1
    var+=1
    dan=2
    print()
    
