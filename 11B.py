import math
def calculate_hypotenuse(angle_degrees, adjacent):
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle_degrees)

    # Calculate the hypotenuse using the cosine function
    hypotenuse = adjacent / math.cos(angle_radians)

    return hypotenuse
def main():
    # Input: Nearest angle in degrees and length of the adjacent side
    try:
        angle_degrees = float(input("Enter the nearest angle in degrees: "))
        adjacent = float(input("Enter the length of the adjacent side: "))
    except ValueError:
        print("Invalid input! Please enter numerical values.")
        return

    # Calculate the hypotenuse
    hypotenuse = calculate_hypotenuse(angle_degrees, adjacent)

    # Output: Length of the hypotenuse
    print(f"The length of the hypotenuse is: {hypotenuse:.2f}")


if __name__ == "__main__":
    main()
