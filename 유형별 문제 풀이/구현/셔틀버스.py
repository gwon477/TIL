timetable = ["09:10", "09:09", "08:00"]
n = 2
t = 10
m = 2

# 09:09

sorted_timetables = sorted(timetable, reverse=True)
seats = m * n

arrive = '09:00'
index = ''
while seats > 1:
    seat = m
    for _ in sorted_timetables:
        if seat == 0:
            break
        else:
            if _ <= arrive:
                index = _
                seat -= 1
                seats -= 1
                sorted_timetables.pop()
            else:
                break

    a_h,a_m = map(int,arrive.split(':'))
    n_h = a_h
    n_m = a_m + t
    if n_m >= 60:
        n_h = a_h + 1
        n_m -= 60
        if n_m > 23:
            n_m = 0

    arrive = f'{n_h:02}:{n_m:02}'

print(index)

