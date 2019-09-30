#Gabi Gervasi
#Gabrielle.Gervasi1@marist.edu
#Sentence Statistics that show word count, character count, and word length average

def main():
    print("This program will tell you about your sentence statistics")

    string= input("Please enter the sentence: ")
    print()

    #number of words
    word=len(string.split())
    print("The number of words: ", word)

    #number of characters
    character=len(string)
    print("The number of characters: ", character)

    #average of word length
    average= character/word
    print("The average word lenght: ", average)

main()
