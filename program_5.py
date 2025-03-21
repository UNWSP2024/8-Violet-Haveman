# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

def course_info():
    courses = {}
    while True:
        ID = input("Enter a course ID (or enter STOP to stop): ")
        if ID == "STOP":
            break
        name = input("Enter a name for the Course ID you just entered: ")
        courses[ID] = name
    subject = input("Subject: ")
    if subject in courses:
        courses.get(subject)
    return courses

course_info()

