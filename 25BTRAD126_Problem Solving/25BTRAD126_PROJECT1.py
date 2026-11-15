# Program with Unit Converter

print("UNIT CONVERTER")
print("1. Kilometers to Meters")
print("2. Meters to Centimeters")
print("3. Meters to Kilometers")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    # Kilometers to Meters
    km = float(input("Enter quantity in kilometers: "))
    m = km * 1000
    print("Quantity in meters =", m)

elif choice == 2:
    # Meters to Centimeters
    m = float(input("Enter quantity in meters: "))
    cm = m * 100
    print("Quantity in centimeters =", cm)

elif choice == 3:
    # Meters to Kilometers
    m = float(input("Enter quantity in meters: "))
    km = m / 1000
    print("Quantity in kilometers =", km)

else:
    print("Invalid choice")