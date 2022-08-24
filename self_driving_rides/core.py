
def is_valid(time,order,vehicles):

input_r = open('input.txt','r')
main_input = input_r.read()
main_input = main_input.split()
for i in range(len(main_input)):
    main_input[i] = main_input[i].split(' ')
grid = main_input[0][:2]
vehicles = main_input[0][2]
rides = main_input[0][3]
time = main_input[0][5]
