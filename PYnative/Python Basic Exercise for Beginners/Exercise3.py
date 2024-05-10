"""Write a program to accept a string from the user and display characters that are present at an even index number.

For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

Expected Output:

Orginal String is  pynative
Printing only even index chars
p
n
t
v
"""


origanel_string = input('Enter wolrd')

print("Orginal String is ", origanel_string,'\n',"Printing only even index chars")
for i in range(0,len(origanel_string),2):
    print(origanel_string[i])