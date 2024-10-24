# name = input("Enter your name: ")
# print(name)

# --------------------

# size_input = input("How big is your house (in square feet): ")
# square_meters = int(size_input) / 10.8
# print(square_meters) 

# ---------------------------

size_input = input("How big is your house (in square feet): ")
square_meters = int(size_input) / 10.8
result = "{}平方英尺數 = {} 平方米數 "
with_feet_meters = result.format(size_input,square_meters)
print(with_feet_meters)
print(f"{size_input}平方英尺數 = {square_meters:.2f} 平方米數 ") 