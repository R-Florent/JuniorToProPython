"""Exercise 4: Remove first n characters from a string

Write a program to remove characters from a string starting from zero up to n and return a new string.

For example:

remove_chars("pynative", 4) so output must be tive. Here, we need to remove the first four characters from a string.
remove_chars("pynative", 2) so output must be native. Here, we need to remove the first two characters from a string.
Note: n must be less than the length of the string.

"""
origanel_string = input('Enter wolrd')
string_remove= input('entre number for remove input')
string_remove_int = int(string_remove)
taille_string = len(origanel_string)

if string_remove_int >= taille_string:
    print("Oops!  That was no valid number.  Try again...")
print(origanel_string[0:string_remove_int])



"""Solution """

def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))