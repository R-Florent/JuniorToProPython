# ceux que j'ai fait
print("entre valeur numérqiue")
num1 = int(input())
num2 = int(input())

if num1*num2 <= 1000:
    print(num1*num2)
else:
    print(num1+num2)


#solution

def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return num1 + num2

# first condition
result = multiplication_or_sum(20, 30)
print("The result is", result)

# Second condition
result = multiplication_or_sum(40, 30)
print("The result is", result)