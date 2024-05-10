
currentNumber = 0
previousNumber = 0
for currentNumber in range(0, 10 , 1):
    Sum = currentNumber + previousNumber
    print("Current Number", currentNumber ,"Previous Number : ",previousNumber,"Sum:",Sum)
    previousNumber = currentNumber

# SOLUTION
print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

# loop from 1 to 10
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    # modify previous number
    # set it to the current number
    previous_num = i