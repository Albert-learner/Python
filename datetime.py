import _datetime

now = _datetime.datetime.now()

print("\n-- 현재시간 : ", now, "\n")

if now.hour < 12:
    print("현재 시간은 {HOUR}시로 오전입니다.".format(HOUR = now.hour))
else:
    print("현재 시간은 {HOUR}시로 오후입니다.".format(HOUR = now.hour))

print("\nEND\n")
