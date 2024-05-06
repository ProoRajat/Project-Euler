def Fibonacci_Series(num):
    series = [1, 2]
    while series[-1] < num:
        series.append(series[-1] + series[-2])
    else:
        del series[-1]
    return series

def sum_of_even_numbers():

number = int(input("Last term should not exceed value of:- "))

print(Fibonacci_Series(number))
