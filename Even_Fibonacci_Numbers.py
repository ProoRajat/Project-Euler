''' Known Problems to fix
- number should be an integer and gerater and equal to 2
- output when number is 2
'''

def Fibonacci_Series(num):
    series = [1, 2]
    while series[-1] < num:
        series.append(series[-1] + series[-2])
    else:
        del series[-1]
    return series

def sum_of_even_numbers(num):
    series = Fibonacci_Series(num)
    sum = 0
    for i in series:
        if i%2 == 0:
            sum += i
    return sum


number = int(input("Last term should not exceed value of:- "))

print("Fibonacci Series is : ",Fibonacci_Series(number))
print("Sum of even numbers in the series : ", sum_of_even_numbers(number))