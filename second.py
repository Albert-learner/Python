print("국어 점수 입력 : ", end="")
kor=int(input())
print("영어 점수 입력 :", end="")
eng=int(input())
print("수학 점수 입력 :", end="")
mat=int(input())

avg=(kor+eng+mat)/3

if avg>=90:
    print("Your grade is A")
elif avg>=80:
    print("Your grade is B")
elif avg>=70:
    print("Your grade is C")
elif avg>=60:
    print("Your grade is D")
else:
    print("Your grade is F")
