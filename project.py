import sys
import os

# Asks the user to enter their file location
# User must enter their file path in the format c/users/keala/repo/graph-theory-project/README.txt
# This is to deal with the /mnt/ file problem when using a WSL
file_path = input("Enter the path of your file in the format c/users/file.txt: ")

output = ""
count = 1

# Asserts the path exists
assert os.path.exists("/mnt/"+file_path), "I did not find the file at, "+str(file_path)

regex = input("Enter the regex you would like to postfix: ")

def shunt(regex):
    """Convert infix expressions to postfix."""
    # The eventual output.
    postfix = ""
    # The shunting yard operator stack.
    stack = ""
    # Operator precedence.
    prec = {'*': 100, '.': 90, '|': 80}
    # Loop through the input a character at a time.
    for c in regex:
        # c is an operator.
        if c in {'*', '.', '|'}:
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
                # c is a non-special.
        else:
            # Push it to the output.
            postfix = postfix + c

    # Empty the operator stack.
    while len(stack) != 0:
        # Append operator at top of stack to output.
        postfix = postfix + stack[-1]
        # Remove operator from stack.
        stack = stack[:-1]
    # Return the postfix version of infix.
    return postfix

class State:
    """A state and its arrows in Thompson's construction."""
    def __init__(self, label, arrows, accept):
        """label is the arrow labels, arrows is a list of states to
           point to, accept is a boolean as to whether this is an accept
           state.
        """
        self.label = label
        self.arrows = arrows
        self.accept = accept
    
    def followes(self):
        """The set of states that are gotten from following this state
           and all its e arrows."""
        # Include this state in the returned set.
        states = {self}
        # If this state has e arrows, i.e. label is None.
        if self.label is None:
            # Loop through this state's arrows.
            for state in self.arrows:
                # Incorporate that state's earrow states in states.
                states = (states | state.followes())
        # Returns the set of states.    
        return states

class NFA:
    """A non-deterministic finite automaton."""
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def match(self, s):
        """Return True iff this NFA (instance) matches the string s."""
        # A list of previous states that we are still in.
        previous = self.start.followes()
        # Loop through the string, a character at a time.
        for c in s:
            # Start with an empty set of current states.
            current = set()
            # Loop throuth the previous states.
            for state in previous:
                # Check if there is a c arrow from state.
                if state.label == c:
                    # Add followes for next state.
                    current = (current | state.arrows[0].followes())
            # Replace previous with current.
            previous = current
        # If the final state is in previous, then return True. False otherwise. 
        return (self.end in previous)

def re_to_nfa(postfix):
    # A stack for NFAs.
    stack = []
    # Loop through the postfix r.e. left to right.
    for c in postfix:
        # Concatenation.
        if c == '.':
            # Pop top NFA off stack.
            nfa2 = stack[-1]
            stack = stack[:-1]
            # Pop the next NFA off stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Make accept state of NFA1 non-accept.
            nfa1.end.accept = False
            # Make it point at start state of nfa2.
            nfa1.end.arrows.append(nfa2.start)
            # Make a new NFA with nfa1's start state and nfa2's end state.
            nfa = NFA(nfa1.start, nfa2.end)
            # Push to the stack.
            stack.append(nfa)
        elif c == '|':
            # Pop top NFA off stack.
            nfa2 = stack[-1]
            stack = stack[:-1]
            # Pop the next NFA off stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Create new start and end states.
            start = State(None, [], False)
            end = State(None, [], True)
            # Make new start state point at old start states.
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa2.start)
            # Make old end states non-accept.
            nfa1.end.accept = False
            nfa2.end.accept = False
            # Point old end states to new one.
            nfa1.end.arrows.append(end)
            nfa2.end.arrows.append(end)
            # Make a new NFA.
            nfa = NFA(start, end)
            # Push to the stack.
            stack.append(nfa)
        elif c == '*':
            # Pop one NFA off stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Create new start and end states.
            start = State(None, [], False)
            end = State(None, [], True)
            # Make new start state point at old start state.
            start.arrows.append(nfa1.start)
            # And at the new end state.
            start.arrows.append(end)
            # Make old end state non-accept.
            nfa1.end.accept = False
            # Make old end state point to new end state.
            nfa1.end.arrows.append(end)
            # Make old end state point to old start state.
            nfa1.end.arrows.append(nfa1.start)
            # Make a new NFA.
            nfa = NFA(start, end)
            # Push to the stack.
            stack.append(nfa)
        else:
            # Create an NFA for the non-special character c.
            # Create the end state.
            end = State(None, [], True)
            # Create the start state.
            start = State(c, [], False)
            # Point new start state at new end state.
            start.arrows.append(end)
            # Create the NFA with the start and end state.
            nfa = NFA(start, end)
            # Append the NFA to the NFA stack.
            stack.append(nfa)
    
    # There should only be one NFA on the stack.
    if len(stack) != 1:
        return None
    else:
        return stack[0]

if __name__ == "__main__":

    infix = regex # regular expression
    postfix = shunt(regex) # postfix / shunting algorithm output
    nfa = re_to_nfa(postfix) # non finite automata

    print()
    print(f"infix: {infix} -> postfix: {postfix}")
    print(f"nfa:     {nfa}")
    print()

    counter = 1 # line 1..2..3..

    file = open("/mnt/"+file_path) # reads file

    for line in file: # for every line in the txt file
        print(f"Line: {counter}  ")
        for word in line.split(): # for every word in the line
            match = nfa.match(word) # match the word to the regular expression
            print(f"{word} - {match}")
        counter = counter + 1
        print()
    print()