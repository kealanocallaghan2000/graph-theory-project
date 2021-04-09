import sys
import os

# Asks the user to enter their file location
# User must enter their file path in the format c/users/keala/repo/graph-theory-project/README.txt
# This is to deal with the /mnt/ file problem when using a WSL
#file_path = input("Enter the path of your file in the format c/users/file.txt: ")

#output = ""
#count = 1

#Asserts the path exists
#assert os.path.exists("/mnt/"+file_path), "I did not find the file at, "+str(user_input)

regex = input("Enter the regex you would like to postfix: ")

def shunt(regex):
    """Convert infix expressions to postfix."""
    # The eventual output.
    postfix = ""
    # The shunting yard operator stack.
    stack = ""
    # array for alphabet
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # Operator precedence.
    prec = {'*': 100, '.': 90, '|': 80}
    # Loop through the input a character at a time.
    for c in regex:
        # c is a digit.
        if c in alphabet:
            # Push it to the output.
            postfix = postfix + c
        # c is an operator.
        elif c in {'*', '.', '|'}:
            # Check what is on the stack.
            while len(stack) > 0 and stack[-1] != '(' and prec[stack[-1]] >= prec[c]:
                # Append operator at top of stack to output.
                postfix = postfix + stack[-1]
                # Remove operator from stack.
                stack = stack[:-1]
            # Push c to stack.
            stack = stack + c
        elif c == '(':
            # Push c to stack.
            stack = stack + c
        elif c == ')':
            while stack[-1] != "(":
                # Append operator at top of stack to output.
                postfix = postfix + stack[-1]
                # Remove operator from stack.
                stack = stack[:-1]
            # Remove open bracket from stack.
            stack = stack[:-1]
    # Empty the operator stack.
    while len(stack) != 0:
        # Append operator at top of stack to output.
        postfix = postfix + stack[-1]
        # Remove operator from stack.
        stack = stack[:-1]
    # Return the postfix version of infix.
    return postfix

if __name__ == "__main__":
        print(f"infix:   {regex}")
        print(f"postfix: {shunt(regex)}")
        print()

# variable f applied to the txt file
#f = open("/mnt/"+file_path)

# prints each line in the txt file
#for line in f:
#    if regex in line:
#        output = regex
#        print(f"Line {count}: {output}") 
#        count = count + 1
#f.close()