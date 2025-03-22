# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).
def state_quiz():
    correct = 0
    states = {"Alabama":"Montgomery", "Alaska":"Junaeu", "Arizona":"Pheonix", "Arkansas":"Little Rock", 'California':'Sacracmento', "Colorado":'Denver',"Conneticut":'Hartford', "Delaware":'Dover', 'Flordia':'Tallahasse', 'Georgia':'Atlanta', 'Hawaii':'Honolulu', 'Idado':'Boise', 'Illinois':'Springfield', 'Indiana':'Indianaplois', "Iowa":'Des Moines', 'Kansas':'Topeka', 'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge', 'Maine':'Augusta', 'Maryland':'Annapolis','Massachusetts':'Boston', 'Michigan':'Lansing', 'Minnesota':'Saint Paul', 'Missisippi':'Jackson', 'Missouri':'Jefferson City', 'Montana':'Helena', 'Nebraska':'Lincoln','Nevada':'Carson City', 'New Hampshire':'Concord', 'New Jersey':'Trenton', 'New Mexico':'Santa Fe', 'New York':'Albany', 'North Carolina':'Raleigh', 'North Dakota':'Bismarck', 'Ohio':'Columbus', 'Oklahoma':'Oklahoma City', 'Oregon':'Salem', 'Pennsylavnia':'Harrisburg', 'Rhode Island':'Providence', "South Carolina":'Columbia', 'South Dakota':'Pierre', 'Tennessee':'Nashville', 'Texas':'Austin', "Utah":'Salt Lake City', 'Vermont':'Montepelier', 'Virginia':'Richmond', 'Washington':'Olympia', "West Virginia":'Charleston', 'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}
    import random
    while correct <= 50:
        state = random.choice(list(states))
        print(state)
        correct_answer = states.get(state)
        user_answer = input("What is the capital of the state provided? ")
        if user_answer == correct_answer:
            correct += correct + 1
            print("Correct!")
        else:
            print ("Your answer is incorrect, try again")
    print("Quiz Complete")

state_quiz()




