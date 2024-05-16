def prime_factors(num):
    if num in (0,1):
        return "Not Defined"

    # divide the number by 2 until it does not have it as its prime factor
    while num%2 == 0:
        num /= 2
    
    # --> Divides the number by i until it does not have it as its prime factor.
    # --> Its is like finding prime factors in math and we do not have to worry about compossite number.
    i = 3
    while i <= num:
        while num%i == 0:
            num /= i
        i += 2  # Not taking even numbers
    return i

number = int(input("Please Enter a number: "))
print(f"The Largest prime factors of {number} is {prime_factors(abs(number))}")
