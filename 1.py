import math
import sys

def calculate_culinary_coefficient(x: float) -> float:
    if x >= 3.2:
        raise ValueError("Argument x is outside the domain of definition (must be x < 3.2).")
    
    if x <= 0:
        return math.cos(x**2)**3 - math.sin(x**2)**3
    elif x <= 1.0:
        return x**2 - 0.75
    else:
        return -(1.4 + x) / math.log(x)

def main():
    try:
        user_input = input("Enter culinary parameter x: ")
        x = float(user_input)
        y = calculate_culinary_coefficient(x)
        print(f"Calculated culinary coefficient y = {y:.6f}")
    except ValueError as error:
        print(f"Input/Domain Error: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()