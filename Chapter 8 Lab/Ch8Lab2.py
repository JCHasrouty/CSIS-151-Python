# read file contents and calculate average words per sentence
# count number of words and divide by number of sentences
# need to keep track of how many sentences and how many words
# if you reach '' that is end of the file
# if string has '\n' then you need to ignore 
def main():
    inFile = open('text.txt', 'r')
    line_count = 0
    word_count = 0
    total_words = 0
    average_words = 0

    for line in inFile:
        line_count += 1
        word_count = len(lines.split())
        num_words += word_count
    average_words = num_words / line_count

    inFile.close()

    print("Average number of words per sentence:", average_words)

main()
