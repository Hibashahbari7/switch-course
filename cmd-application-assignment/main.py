INPUT_LENGTH  = 15


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
    return len(inp) > INPUT_LENGTH


def is_empty(inp: str):
    return inp == ""



operations = {
    1: is_palindrome,
    2: is_lower,
    3: is_digit,
    4: is_long,
    5: is_empty
}


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
        if choice not in operations:
            print("Invalid choice.\n")
            continue
        inp = input("Enter an input: ")
        result = operations[choice](inp)
        print(f"The answer is: {result}\n")


if __name__ == "__main__":
    main()
