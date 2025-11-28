# -----------------------------------------
# Part 1: Arithmetic Functions
# -----------------------------------------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# -----------------------------------------
# Part 3: Input Validation Function
# -----------------------------------------

def get_number(message):
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


# -----------------------------------------
# Part 4: Menu Display (For Both Versions)
# -----------------------------------------

def show_menu():
    print("\n===========================")
    print("Basic Calculator")
    print("===========================")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("===========================")


# -----------------------------------------
# Part 5: Object-Oriented Calculator
# -----------------------------------------

class Calculator:

    def add(self, a, b):
        return add(a, b)

    def subtract(self, a, b):
        return subtract(a, b)

    def multiply(self, a, b):
        return multiply(a, b)

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    def menu(self):
        show_menu()  # reuse the same menu

    def run(self):
        print("\nWelcome to the Calculator!")

        while True:
            self.menu()
            choice = input("Enter your choice (1-5): ")

            if choice not in ['1', '2', '3', '4', '5']:
                print("Invalid choice. Please select between 1-5.")
                continue

            if choice == '5':
                print("Thank you for using the calculator.")
                break

            # Get numbers with validation
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            print("\n----------------------")

            if choice == '1':
                print(f"{num1} + {num2} = {self.add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {self.subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {self.multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} = {self.divide(num1, num2)}")


# -----------------------------------------
# Create Calculator Object and Run
# -----------------------------------------

calc = Calculator()
calc.run()