import math
import sys

def calculate_y(x: float) -> float:
    denom = x**3 + 7.5
    cos_val = math.cos(0.5 * x)
    if denom == 0 or cos_val == 0:
        raise ValueError(f"Function is undefined at x = {x}")
    return math.tan(0.5 * x) / denom

def main():
    try:
        x_start = float(input("Enter start x: "))
        x_end = float(input("Enter end x: "))
        step = float(input("Enter step (dx): "))

        if step <= 0 or x_start > x_end:
            raise ValueError("Invalid range or step value.")

        print(f"\n{'No.':<6}| {'x':<10}| {'y':<12}")
        print("-" * 32)

        point_no = 1
        x = x_start
        while x <= x_end + 1e-9:
            y = calculate_y(x)
            print(f"{point_no:<6}| {x:<10.4f}| {y:<12.6f}")
            x += step
            point_no += 1

    except ValueError as error:
        print(f"Input/Domain Error: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()