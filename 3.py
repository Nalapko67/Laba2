import math
import sys

def calculate_x(v: float) -> float:
    if 0 <= v < 0.1 - 1e-9:
        return (1.26 ** v) + v
    else:
        return (math.pi / 2) - math.atan(v + 0.4)

def main():
    try:
        v_start = float(input("Enter start v (e.g. 0): "))
        v_end = float(input("Enter end v (e.g. 4): "))
        step = float(input("Enter step dv (e.g. 0.1): "))

        if step <= 0 or v_start >= v_end:
            raise ValueError("Invalid range or step value.")

        print(f"\n{'No.':<6}| {'v':<10}| {'x':<12}")
        print("-" * 32)

        v = v_start
        point_no = 1

        while v < v_end - 1e-9:
            x = calculate_x(v)
            print(f"{point_no:<6}| {v:<10.4f}| {x:<12.6f}")
            v += step
            point_no += 1

    except ValueError as error:
        print(f"Input Error: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()