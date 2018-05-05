def main():
    user_input = input("Please enter a string: ")
    max_char = ""
    max_count = 0

    for ch in user_input:
        #calculate frequency of ch in string user_input
        #examine every character and see if they are the same
        #then increment by 1 because they are the same
        count = char_frequency(ch, user_input)
        
        #now 'count' tells me what is the frequency of the character 'ch'

        if count > max_count:
            max_char = ch
            max_count = count
        
    print("Most frequently used character:", max_char)
    print("Number of occurences:", max_count)

def char_frequency(ch, string):
    count = 0
    for c in string:
        if c == ch:
            count += 1
    return count
    
main()
