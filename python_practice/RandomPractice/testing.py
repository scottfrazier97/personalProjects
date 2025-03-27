# def add_and_maybe_multiply(a, b, c=None):
#     result = a + b
#     if c is not None:
#         result = result * c
#     return result

# add_and_maybe_multiply(5,6)
# add_and_maybe_multiply(5,6,2)

# print(add_and_maybe_multiply(5, 6))  # Output: 11
# print(add_and_maybe_multiply(5, 6, 2))  # Output: 22

def calculate_square(number):
    """Function to calculate the square of a number."""
    return number ** 2

def calculate_sum_of_squares(numbers):
    """Function to calculate the sum of squares of a list of numbers."""
    sum_of_squares = 0
    for num in numbers:
        square = calculate_square(num)  # Using the result returned by calculate_square
        sum_of_squares += square
    return sum_of_squares

# Example usage:
my_numbers = [1, 2, 3, 4, 5]
result = calculate_sum_of_squares(my_numbers)
print("Sum of squares:", result)