# Function to calculate area of a triangle

def calculate_area(base, height):
    area = 0.5 * base * height
    return area

# Prompt the user to enter the base and height

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Call the function to calculate the area
area = calculate_area(base, height)

# Print the area
print(f"The area of the triangle with base {base} and height {height} is {area:.2f}")
