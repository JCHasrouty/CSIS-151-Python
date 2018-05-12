import csv
import random

def main():
    state_capitals = {}
    
    state_capitals = fill_dictionary(state_capitals)
    print(state_capitals)
    guess_capital(state_capitals)

def fill_dictionary(dictionary):
    with open('capitals.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dictionary = dict(reader)
##        for row in reader:
##            dictionary[row['State']] = row['Capital']
##        dictionary = {rows[0]:rows[1] for rows in reader}
##        for row in reader:
##            key = row[0]
##            dictionary[key] = row[1:]
        return dictionary
    


def guess_capital(dictionary):
    random_choice = random.randrange(0,len(dictionary))
    random_choice = random.choice(dictionary.keys())
    correct_answer = dictionary.get(random_choice)
    user_input = input("Enter the capital of", random_choice)
    if user_input.upper() != "QUIT":
        if user_input == correct_answer:
            print("That is correct")
        elif user_input != correct_answer:
            print("Wrong!!! The capital of", random_choice,"is",correct_answer)
    else:
        print("Thank you for taking CSIS-151 class")
        
main()
    
