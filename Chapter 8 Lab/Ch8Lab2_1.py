def main():
    with open('text.txt','r') as content:
        lineCount = 0
        Tot_wordCount = 0
        lines = content.readlines()
        for line in lines:
            lineCount = lineCount + 1       
            wordCount = len(line.split())
            Tot_wordCount += wordCount
        average_words = Tot_wordCount / lineCount
    print("Average number of words per sentence:", format(average_words, "2.2f"))
     
main()
