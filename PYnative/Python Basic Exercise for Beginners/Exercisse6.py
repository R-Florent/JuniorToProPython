"""
Exercise 6: Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers which are divisible by 5

Expected Output:

Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55
"""
given_list = [10,20,33,46,52]
print("Given list:", given_list)
print('Divisible by 5:')

for element in given_list:
    if element % 5 ==0:
        print(element)