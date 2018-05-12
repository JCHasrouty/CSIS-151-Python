# read file contents and calculate average words per sentence
# count number of words and divide by number of sentences
# need to keep track of how many sentences and how many words
# if you reach '' that is end of the file
# if string has '\n' then you need to ignore 
def main():
##    with open('text.txt','r') as content:
##        lineCount = 0
##        Tot_wordCount = 0
##        lines = content.readlines()
##        for line in lines:
##            lineCount = lineCount + 1       
##            wordCount = len(line.split())
##            Tot_wordCount += wordCount
##        avg = Tot_wordCount / lineCount

##    inFile = open('text.txt', 'r')
##    line_count = 0
##    total_word_count = 0
##
##    for line in inFile:
##        line_count = line_count + 1
##        word_count = len(line.split())
##        total_word_count += word_count
##    average_words = total_word_count / line_count
##
##    inFile.close()

##    print("Average number of words per sentence:", format(average_words, "2.2f"))

    lc, wc = 0, 0
    with open('text.txt', 'r') as f:
        for line in f:
            lc += 1
            wc += len(line.strip().split())
    avg = wc/lc
    print(avg)

    content_file = open('text.txt', 'r')
    content = content_file.read()
    word_count = len(content.split())
    line_count = len(content.split('\n'))
    content_file.close()
    average_words = word_count/line_count
    print(average_words)
main()
