# Problem 5:

# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is
# a string that reads the same forwards and backwards.)

# Madam, Malayalam, dalda are some of the examples of palindrome.

# Function to check if a string is a palindrome
def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    sanitized_string = input_string.replace(" ", "").lower()
    # Check if the string reads the same forwards and backwards
    return sanitized_string == sanitized_string[::-1]

# Main program
if __name__ == "__main__":
    # Ask the user for input
    user_input = input("Enter a string: ")

    # Check if the string is a palindrome
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome!")
    else:
        print(f"'{user_input}' is not a palindrome.")
