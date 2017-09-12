
################
#   Computer Project 09
#   
#   Prompts the user to open a file. 
#       correct message will be displayed if file cannot be found and continuously\
#       ask to input a file again.
#   Create a dictionary to calculate word completions. if no completion available\
#       appropriate message will display
#   Return sets of possible completions for prefix word inputted 
#   Continues to ask for a prefix to complete until user quits program.
#################
import string

def open_file():
    ''' prompts user to open a file. If the file cannot be found, an error \
    message will be displayed. Functions loops until correct file is opened and \
    returns a file a file pointer.
    '''
    the_file = input("Input a file name: ")
    while True:
        try:
            fp = open(the_file, "r")
            return fp
        except FileNotFoundError:
            the_file = input ("Error. Input a file name: ")
      

def fill_completions(fd):
    ''' Builds a dictionary to calculate possible words. when the dictionary is\
    returned, the keys are tuples, and the values are sets. 
    '''
    word_dict = {}
    for line in fd:
        line_lst = line.strip().split() 
        #splits to seperate the strings on whitespace
        for word in line_lst:
            word = word.lower().strip(string.punctuation) 
            #reads all words by making all lowercase and ignores any punctuation
            if word.isalpha() and len(word) > 1:
                #word must be made up of letters and words such as "a" or "I" \
                #will be ignored.
                for i,ch in enumerate(word):
                #returns the index numbers and its pertaining character
                    if (i,ch) in word_dict:
                        word_dict[(i,ch)].add(word)
                    else:
                        word_dict[(i,ch)] = {word}
                    #since the word is not in dict, it creates it.
    return word_dict
      

def find_completions(prefix, c_dict):
    '''Uses the dictionary created in fill_completions and the prefix inputted\
    by user. Returns set of words pertaining to the prefix entered. 
    '''
    for i,ch in enumerate (prefix):
        #will match up index and charachter of prefix entered
        tup = (i,ch) #set index and character to be a tuple
        if tup in c_dict:
            if i == 0:
                word_set = c_dict[tup]
            else:
                word_set = word_set & c_dict[tup]
                #redefine word_set because must intersect all sets of the word
        else:
            return None
     
    return word_set
  

def main():
    '''calls open_file to get file pointer. Program will continue to ask for \
    prefix and display its pertaining completions. if there are no completions \
    to a prefix appropriate message will display.
    '''
    file=open_file()
    word_dict = fill_completions(file)
    prefix = ''
    prefix = input("Enter the prefix to complete (or '#' to quit): ")
    while prefix != '#':
        #if # is entered, program will quit
        completions = find_completions (prefix, word_dict)

        if completions == 'None':
            print("There are no completions to this prefix")
            #appropraite message displayed if no prefix to a word
            
        else:
            print("Completions of "+ prefix +": ", end = ' ')
            for word in completions:
                print(word,end=' ')
            #words will be printed without being in set format
        print()    
        prefix = input("Enter the prefix to complete (or '#' to quit): ")
        #must continue to ask for prefix until user quits.
    


main()


#Q1:7
#Q2:4
#Q3:4
#Q4:5
