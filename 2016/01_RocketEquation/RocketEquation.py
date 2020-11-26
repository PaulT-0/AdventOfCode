import math
import os

def calculate_fuel(module_mass):
    # Function for part 1, ignoring mass of additional fuel
    return(math.floor(module_mass/3)-2)

def recursive_calculate_fuel(mass):
    # Recursive function for part 2, accounts (crudely) for mass of additional fuel
    fuel = math.floor(mass/3)-2
    if fuel <= 0:
        return 0
    else:
        return fuel + recursive_calculate_fuel(fuel)

Fuelneeded = 0

with open('input.txt') as f:
    for module_mass in f:
        Fuelneeded += recursive_calculate_fuel(int(module_mass))

print(Fuelneeded)
