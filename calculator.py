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


    # loop for doing until true
    while (True):

        # user menu
        opeartion.menu()

        # get user choice
        choice = int(input("Enter choice (1/2/3/4/5): "))

        # now condition
        if choice in [1, 2, 3, 4]:

            # try for input the value from user
            try:
                num1= float(input("Enter the first number: "))
                num2= float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            # now creating object
            operator  = opeartion()

            # condition for operation
            if choice == 1:
                print(f"The output is {operator.add(num1, num2)}")
            elif choice == 2:
                print(f"The output is {operator.sub(num1, num2)}")
            elif choice == 3:
                print(f"The output is {operator.mul(num1, num2)}")
            else:
                print(f"The output is {operator.div(num1, num2)}")

            
        elif choice == 5:
            print("The Operation is ended")
            break
        else:
            print("Please enter the correct value!!")


        








