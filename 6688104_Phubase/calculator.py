"""Simple calculator module with basic arithmetic operations."""


def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def subtract(a, b):
    """Subtract two numbers and return the result."""
    return a - b


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def divide(a, b):
    """Divide two numbers and return the result.
    
    Raises:
        ValueError: If attempting to divide by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    """Interactive calculator interface."""
    print("Simple Calculator")
    print("-" * 40)
    
    while True:
        print("\nOperations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("\nEnter choice (1/2/3/4/5): ").strip()
        
        if choice == "5":
            print("Goodbye!")
            break
        
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please try again.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == "1":
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == "2":
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == "3":
                print(f"Result: {num1} × {num2} = {multiply(num1, num2)}")
            elif choice == "4":
                print(f"Result: {num1} ÷ {num2} = {divide(num1, num2)}")
                
        except ValueError as e:
            print(f"Error: {e}")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")


if __name__ == "__main__":
    main()
