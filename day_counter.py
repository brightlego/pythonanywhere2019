import matplotlib.pyplot as plt
def find_startday(y):
    s = y%100
    s /= 4
    s += 1
    s += 1
    if bool(not(y%4) and (not(y%400) or y%100)):
        s -= 1
    s += [6,4,2,0][(y%400)/100]
    s += y%100
    s %= 7
    return((s-2)%7)


days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
mon_len = [[31,28,31,30,31,30,31,31,30,31,30,31],[31,29,31,30,31,30,31,31,30,31,30,31]]
week_mon = {}
start_date = int(raw_input('Start year: '))
end_date = int(raw_input('End year: '))
viable_dates = raw_input('Viable dates: ').split(',')
day = find_startday(start_date)
for i in range(start_date,end_date):
    for j in mon_len[bool(not(i%4) and (not(i%400) or i%100))]:
        for k in range(j):
            if str(k+1) in viable_dates or len(viable_dates) == 1:
                str_day = str(6-day)+'0'*(2-len(str(30-k)))+str(30-k)+days[day]+' '+str(k+1)
                if str_day not in week_mon:
                    week_mon[str_day] = 1
                else:
                    week_mon[str_day] += 1
            day += 1
            day %= 7
week_mon = zip(week_mon.values(),week_mon.keys())
week_mon.sort(reverse = True)
data = [[],[]]
for i in week_mon:
    data[0].append(i[0])
    data[1].append(i[1][3:])
'''plt.clf()
plt.ylim((min(data[0]),max(data[0])))
plt.bar(range(len(data[0])),data([0]))
#plt.xticks(data[1])
plt.savefig('day_count_bar.png')'''
for i in week_mon:
    print(i[1][3:] + ':\t' + str(i[0]))