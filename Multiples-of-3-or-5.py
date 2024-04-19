# If we list all the natural numbers below 10 that are multiples of 3 or 5 we get 3,5,6 and 9. The sum of these multiples is 23.
# For negative numbers sum = 0
# Find the sum of all the multiples of 3 or 5 below 1000.

def retunr_sum(num):
    # Store sum of numbers
    sum = 0
    
    # take the numbers less than given number one by one and check if divisible by 3 or 5 or not
    for i in range(number): # NOTE:- number is not included
        if i % 3 == 0 or i % 5 == 0:
            sum += i    # if divisible add i to sum
    return sum

number = int(input("Enter a number: "))
print(retunr_sum(number))



