import random

def main():
    #step 0: create an empty dictionary
    states = {}
    
    #step 1: open and load the CSV file into the dictionary
    input_file = open('capitals.csv', 'r')

    for line in input_file:
        pair = line.rstrip('\n').split(",")
        ## for the key of the dictionary = assign the value of pair 1
        ## when line is split, you get list of [State, Capital] therefore
        ## when you are executing the line below, you are assigning
        # list[0] which is State into the key of the dictionary
        # and list[1] which is the capital into the value seciton of the dictionary
        states[pair[0]] = pair[1]
    input_file.close()    
    #step 2: loop, generate a random number, select one state
    # ask the user for the capital, compare and respond
    # if the user enter "QUIT", then exit the program

    user_input = ""
    random.seed(1000)
    
    while user_input.upper() != "QUIT":
        random_number = random.randrange(0, len(states))
        state = list(states.keys()) [random_number]
        user_input = input("Enter the capital of " + state + ": ")
        if user_input.upper() == "QUIT":
            print("Thank you for taking CSIS-151 class")
        else:
            if states[state].upper() == user_input.upper():
                print("That is correct!")
            else:
                ## states[state] == state is key and states is dictionary so it retreives
                print("Wrong!!! The capital of", state, "is", states[state])
                
main()
