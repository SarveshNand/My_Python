def handle_multiple_exceptions():
    try:
        num1 = int(input("Enter numerator: "))
        num2 = int(input("Enter denominator: "))
        result = num1 / num2
        print("Result:", result)
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

handle_multiple_exceptions()