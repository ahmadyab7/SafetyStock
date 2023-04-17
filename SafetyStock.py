import math
from scipy.stats import norm

def calculate_safety_stock() -> float:
    avg_demand = int(input("Enter Average demand number = "))
    standard = int(input("Enter Standard deviation number = "))
    lead_time = int(input("Enter Lead time number = "))
    level = float(input("Enter Service level number = "))

    z_value = norm.ppf(level)

    result = standard * z_value * math.sqrt(lead_time)

    return round(result, 2)

def run_program():
    print("This App for calculated safety stock\n")

    chose = "1"
    while chose != "0":
        print("Safety stock result --> ", calculate_safety_stock())
        print("\n\n")
        chose = input("If you need exit the program enter 0, else input anything = ")

    print("Thank you for using program")

run_program()
