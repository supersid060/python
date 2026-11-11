import math

def trig_values(angle, in_degrees=True):
    """
    Calculate sine, cosine, and tangent for a given angle.
    
    :param angle: The angle value (float or int).
    :param in_degrees: If True, interpret angle as degrees; otherwise radians.
    :return: Dictionary with sin, cos, and tan values.
    """
    try:
        # Convert degrees to radians if needed
        radians = math.radians(angle) if in_degrees else angle
        
        # Calculate values
        sin_val = math.sin(radians)
        cos_val = math.cos(radians)
        
        # Handle tangent carefully (avoid division by zero)
        try:
            tan_val = math.tan(radians)
        except Exception:
            tan_val = float('inf')  # Infinite when cos(radians) == 0
        
        return {
            "sin": sin_val,
            "cos": cos_val,
            "tan": tan_val
        }
    except (TypeError, ValueError):
        raise ValueError("Angle must be a valid number.")

if __name__ == "__main__":
    try:
        # User input
        angle_input = float(input("Enter the angle: "))
        unit_choice = input("Is this angle in degrees? (y/n): ").strip().lower()
        
        in_degrees = unit_choice == 'y'
        
        results = trig_values(angle_input, in_degrees)
        
        print(f"\nResults for angle {angle_input} {'degrees' if in_degrees else 'radians'}:")
        print(f"sin = {results['sin']:.6f}")
        print(f"cos = {results['cos']:.6f}")
        print(f"tan = {results['tan']:.6f}")
        
    except ValueError as e:
        print(f"Error: {e}")