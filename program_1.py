# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names, 
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11

def initials_generator(name1, name2, name3):

    #    Add your logic here
    initial1 = name1[0]
    initial2 = name2[0]
    initial3 = name3[0]
    personsInitials = initial1 +"." + " " + initial2 + "." + " " + initial3 + "."
    return personsInitials.strip()
name1 = input("What is your first name? ")
name2 = input("What is your middle name? ")
name3 = input("What is your last name? ")
personsName = name1 + " " + name2 + " " + name3

initials = initials_generator(name1, name2, name3)

print(initials)