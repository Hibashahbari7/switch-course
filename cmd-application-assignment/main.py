THRESHOLD = 15


def print_menu():
    print("\nThe available operations are:\n")
    print("1 - Palindrome: Check if the input is palindrome")
    print("2 - Lower: Check if all characters in the input are lowercase")
    print("3 - Digit: Check if all characters in the input are digits")
    print("4 - Long: Check if the input length is longer than 15")
    print("5 - Empty: Check if the input is empty")
    print("6 - Exit: Exit successfully from the application")
    print()


def is_palindrome(inp: str):
    return inp == inp[::-1]


def is_lower(inp: str):
    return inp.islower()


def is_digit(inp: str):
    return inp.isdigit()


def is_long(inp: str):
    return len(inp) > THRESHOLD


def is_empty(inp: str):
    return inp == ""


def main():
    while True:
        print_menu()
        choice = input("Please enter the number of the operation you choose: ")

        if not choice.isdigit():
            print("Invalid choice, please enter a number between 1-6.\n")
            continue

        choice = int(choice)

        if choice == 6:
            print("\nExit successfully")
            break

        inp = input("Enter an input: ")

        if choice == 1:
            result = is_palindrome(inp)
        elif choice == 2:
            result = is_lower(inp)
        elif choice == 3:
            result = is_digit(inp)
        elif choice == 4:
            result = is_long(inp)
        elif choice == 5:
            result = is_empty(inp)
        else:
            print("Invalid option.\n")
            continue

        print(f"The answer is: {result}\n")


if __name__ == "__main__":
    main()
