# first for all the opeartion
class opeartion:
    # constructor
    def __init__(self, first, second):
        self.first = first
        self.second = second

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
        if self.second == 0:
            return 'Error! Division by zero'
        return self.first / self.second
    
    # method for menu
    def menu(self):
        """This function display the menu"""
        print("Simple calculator")
        print("Select opeartion: ")
        print("1. add")
        print("2. subtraction")
        print("3. multiplication")
        print("4. division")
        print("5. exit the program")


        

# constructor for main()
if __name__ == '__main__':

    # creating a object

    # creating a infinite loop
    while True:

    #for choice
        if choice in ['1', '2', '3', '4']:
        
        # get number from user
        # also using the expection and error handling
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter the second number: "))

            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
        opeartor = opeartion(num1, num2)
        opeartor.menu()

        # perform opeartion based on user choice
            if choice == '1':
                print(f"The result is:{opeartor.add(num1, num2)}")
            elif choice == '2':
                print(f"The result is:{opeartor.sub(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {opeartor.mul(num1, num2)}")  
            elif choice == '4':
                print(f"The result is: {opeartor.div(num1, num2)}")  

            elif choice == '5':
                print("Exiting the program.")
                break
            else:
            print("Invalid choice. Please select a valid operation.")



