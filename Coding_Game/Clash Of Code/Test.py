input = "AB-AB-CAAB"

s =""

for e in input:
    if e.isalpha():
        s += str(ord(e) - ord('A'))
    else :
        s += str(e)

print(s)