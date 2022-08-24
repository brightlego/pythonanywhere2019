MonthName =  ["January", "February", "March", "April", "May", "June", 'July', 'August', 'September', 'October', 'November', 'December']
# Input the monthly bills and store them in a separate array Bills.

# This was typed to make it easier.

Bills = []
for i in range(12):
	Bills.append(int(input(MonthName[i]+': ')))


# Find the maximum amount together with the month name

Bill_month = list(zip(Bills,MonthName))
max_num = [-1]
for i in Bill_month:
    if i[0] > max_num[0]:
        max_num = i
print(max_num[1]+":",max_num[0])
