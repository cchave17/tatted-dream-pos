"""

"""


def display_menu():
    print("Welcome to the Tattoo Database Console App")
    print("1. Customers")
    print("2. New Tattoo")
    print("3. View Schedule")
    print("4. Admin")
    print("5. Quit")
    print()

def main():
    display_menu()

    choice = int(input("Enter your choice: "))

    while choice != 4:
        if choice == 1:
            # Display all customers
            pass
        elif choice == 2:
            # Display all tattoos
            pass
        elif choice == 3:
            # Display all sessions
            pass
        elif choice == 4:
            # Add a new customer
            pass
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

        display_menu()
        choice = int(input("Enter your choice: "))