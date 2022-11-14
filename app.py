"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

def factorial(number):
    result = 1
    counter = 1

    while counter <= number:
        result *= counter
        counter += 1
    return result

def main():
    limit = 1000000

    numbers_equal_to_sum = []
    for i in reversed(range(3, limit + 1)):
        factorial_sum = 0
        for digit in str(i):
            factorial_sum += factorial(int(digit))
        
        if factorial_sum == i:
            numbers_equal_to_sum.append(i)
    
    print(sum(numbers_equal_to_sum))

if __name__ == "__main__":
    main()
