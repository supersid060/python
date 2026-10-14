def print_reverse_right_angle_triangle(n):
    """
    Prints a reverse right-angle triangle pattern of '*' characters.
    Example for n=5:
    *****
    ****
    ***
    **
    *
    """
    for i in range(n, 0, -1):  
        print('*' * i)


def main():
    try:
        
        n = int(input("Enter the number of rows (positive integer): "))
        if n <= 0:
            print("Error: Number of rows must be a positive integer.")
            return
        print_reverse_right_angle_triangle(n)
    
    except ValueError:
        print("Error: Please enter a valid integer.")


if __name__ == "__main__":
    main()