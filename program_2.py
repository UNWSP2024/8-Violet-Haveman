# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13
def word_separator(sentence):

    new_sentence = ""
    # Add your logic here
    new_sentence += sentence[0]
    for s in range(1, len(sentence)):
        print(sentence[s])
        individual = sentence[s]
        # check if value at sentence[s] is uppercase
        # if it is uppercase append a space and its value to the new_sentence
        if individual.isupper():
            individual = individual.lower()
            new_sentence += ' ' + individual
        else:
            new_sentence += individual
    return new_sentence.strip()




# Example usage

sentence = "StopAndSmellTheRoses"

new_sentence = word_separator(sentence)

print(new_sentence)