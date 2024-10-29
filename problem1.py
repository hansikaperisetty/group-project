# Understand: We need a function to reverse a given string, where each character is placed in reverse order.

def reverse_string(s):
    # Code: Initialize an empty string to hold the reversed characters.
    reversed_string = ""

    # Apply: Loop through each character in the original string.
    for char in s:
        # Solve: Prepend each character to the beginning of reversed_string, reversing the order.
        reversed_string = char + reversed_string

    # Evaluate: Return the reversed string to check if it's correct.
    return reversed_string


# Example usage to test the function
print(reverse_string("hello"))  # Expected output: "olleh"
