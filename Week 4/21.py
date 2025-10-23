def binary_to_decimal(binary_str):
    try:
        decimal = int(binary_str , 2)
        return decimal
    except ValueError:
        return "Invalid Binary Number"
    
binary_input = input("Enter a binary number: ")
result = binary_to_decimal(binary_input)

print(f"Decimal equivalent: {result}")