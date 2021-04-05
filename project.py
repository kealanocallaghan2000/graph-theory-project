import sys
import os

# Asks the user to enter their file location
# User must enter their file path in the format c/users/keala/repo/graph-theory-project/README.txt
# This is to deal with the /mnt/ file problem when using a WSL
user_input = input("Enter the path of your file in the format c/users/file.txt: ")

#Asserts the path exists
assert os.path.exists("/mnt/"+user_input), "I did not find the file at, "+str(user_input)

# variable f applied to the txt file
f = open("/mnt/"+user_input)

# prints each line in the txt file
for line in f:
    print(line)


f.close()








