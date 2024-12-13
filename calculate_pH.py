import math


def calculate_pH(hydrogen_concentration):
    """
    Calculate the pH of a solution based on the hydrogen ion concentration.

    Parameters:
    hydrogen_concentration (float): Concentration of hydrogen ions in moles per liter (M).

    Returns:
    float: The pH of the solution.
    """
    if hydrogen_concentration <= 0:
        raise ValueError("Hydrogen ion concentration must be greater than 0.")

    pH = -math.log10(hydrogen_concentration)
    return pH


def main():
    try:
        # Input the concentration of hydrogen ions
        hydrogen_concentration = float(input("Enter the hydrogen ion concentration (in M): "))
        pH = calculate_pH(hydrogen_concentration)
        print(f"The pH of the solution is: {pH:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
