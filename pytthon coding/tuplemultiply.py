from math import prod
def tuple_product(numbers_tuple):
    if not isinstance(numbers_tuple, tuple):
        raise TypeError("Input must be a tuple.")
    numeric_values = [n for n in numbers_tuple if isinstance(n, (int, float))]
    if not numeric_values:
        return None  
    return prod(numeric_values)  
if __name__ == "__main__":
    try:
        
        numbers = (2, 3, 4, 5)

        result = tuple_product(numbers)
        if result is None:
            print("Tuple contains no numeric values.")
        else:
            print(f"Product of tuple {numbers} is: {result}")

    except Exception as e:
        print(f"Error: {e}")