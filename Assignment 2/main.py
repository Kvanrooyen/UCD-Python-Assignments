# Ask the user for their name
name = input("What is your name? ")

# Ask the user for their height in centimeters
height_cm = float(input("What is your height in centimeters? "))

# Convert the height from centimeters into feet, inches, and quarter inches
# 1 inch = 2.54 cm
# 1 foot = 12 inches

height_inches = height_cm / 2.54
height_feet = int(height_inches // 12)
remaining_height_inches = height_inches % 12
whole_height_inches = int(remaining_height_inches // 1)
quarters = round((remaining_height_inches - whole_height_inches) / 0.25)

# Adjust for cases where rounding pushes the value above 12 inches
if quarters == 4:
    height_feet += 1
    whole_height_inches = 0
    quarters = 0

# Display the result
print(f"Dear {name.upper()}, you are {height_feet} ft {whole_height_inches} {quarters}/4 in tall.")
