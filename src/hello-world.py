def add_numbers(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        int or float: Sum of a and b
    """
    return a + b


if __name__ == "__main__":
    # Example 1: Adding two integers
    num1 = 5
    num2 = 3
    result = add_numbers(num1, num2)
    print(f"Addition of {num1} and {num2} is: {result}")
    
    # Example 2: Adding two floats
    num3 = 10.5
    num4 = 20.3
    result2 = add_numbers(num3, num4)
    print(f"Addition of {num3} and {num4} is: {result2}")
    
    # Example 3: User input
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        sum_result = add_numbers(a, b)
        print(f"The sum of {a} and {b} is: {sum_result}")
    except ValueError:
        print("Please enter valid numbers")