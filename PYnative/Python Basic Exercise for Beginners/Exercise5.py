"""Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

Given:

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
Expected Output:

Given list: [10, 20, 30, 40, 10]
result is True

numbers_y = [75, 65, 35, 75, 30]
result is False"""

list_string_int = input('entre number list of number')
def retrunlist(chaine : str):
    premier_carater_list = list_string_int[0]
    last_carater_list = list_string_int[-1]

    if premier_carater_list == last_carater_list:
        return True
    else:
        return False

print("resulta is",retrunlist(list_string_int))