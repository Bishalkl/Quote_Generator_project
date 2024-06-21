class Operation:
    # constructor
    def __init__(self, first_number, second_number):
        self.first = first_number
        self.second = second_number

    # method for addition
    def add(self):
        return self.first + self.second

    # method for subtraction
    def sub(self):
        return self.first - self.second

    # method for multiplication
    def mul(self):
        return self.first * self.second

    # method for division
    def div(self):
        if self.second != 0:
            return self.first / self.second
        else:
            return "Error: Division by zero!"

# Function to display the menu and get user input
def menu():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

if __name__ == '__main__':
    while True:
        menu()
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            calc = Operation(num1, num2)

            if choice == '1':
                print(f"The result is: {calc.add()}")
            elif choice == '2':
                print(f"The result is: {calc.sub()}")
            elif choice == '3':
                print(f"The result is: {calc.mul()}")
            elif choice == '4':
                print(f"The result is: {calc.div()}")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid operation.")
