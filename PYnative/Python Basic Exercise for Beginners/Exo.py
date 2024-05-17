bananas = 1
monkeys = "1,2,3"
str_elements = monkeys.split(',')
int_m = [int(element) for element in str_elements]
int_m.sort()
num_monkey_feed = 0
for i in range(len(int_m)):
    if bananas >= int_m[i]:
        bananas = bananas - int_m[i]
        num_monkey_feed +=1
    else:
        print(num_monkey_feed)