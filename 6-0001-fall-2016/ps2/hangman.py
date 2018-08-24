# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random

WORDLIST_FILENAME = "words.txt"
with_hints = False

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    return sorted(list(set(list(secret_word)))) == sorted(letters_guessed)



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    s = ""
    for ch in secret_word:
        if ch in letters_guessed:
            s += ch
        else:
            s += "_ "
    return s



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = set()
    for i in range(ord('a'), ord('z')+1):
        letters.add(chr(i))
    not_guessed = letters.symmetric_difference(set(letters_guessed))
    return ''.join(sorted(list(not_guessed)))
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    guesses = 6
    letters_guessed = [] # unique
    all_letters_guessed = []
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    warnings = 3
    print("You have", warnings, "warnings left.")
    
    while guesses > 0:
        print("------------")
        print("You have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        
        letter = input("Please guess a letter: ")

        # Too lazy to retype hangman
        if with_hints and letter == '*':
            if len(letters_guessed) < 1:
                print("No guesses allowed for now.")
            else:
                got_hint = True
                print("Possible word matches are:")
                show_possible_matches(guessed_word)
                continue

        
        duplicate_guess, valid_guess = letter in all_letters_guessed, str.isalpha(str.lower(letter))
        if duplicate_guess or not valid_guess:
            warnings -= 1
            if warnings >= 0:
                if duplicate_guess:
                    print("Oops! You've already guessed that letter. You have", warnings, "warning(s) left:",\
                          guessed_word)
                else:
                    print("Oops! That is not a valid letter. You have", warnings, "warning(s) left:", \
                          guessed_word)
            else:
                if duplicate_guess:
                    print("Oops! You've already guessed that letter. You have no warnings left so you",\
                          "lose one guess:", guessed_word)
                else:
                    print("Oops! That is not a valid letter. You have no warnings left so you",\
                          "lose one guess:", guessed_word)
                guesses -= 1
                warnings = 3
            continue
        
        temp_lg = letters_guessed[::]
        
        letters_guessed.append(letter)
        all_letters_guessed.append(letter)
            
        temp = get_guessed_word(secret_word, letters_guessed)
        if temp != guessed_word:
            print("Good guess:", temp)
            guessed_word = temp
        else:
            print("Oops! That letter is not in my word:", guessed_word)
            if letter not in 'aeiou':
                guesses -= 1
            else:
                guesses -= 2
            letters_guessed = temp_lg[::]
        
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            print("Your total score for this game is:", len(letters_guessed) * guesses)
            return
    print("-----------")
    print("Sorry, you ran out of guesses. The word was {0}.".format(secret_word))
        



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(' ', '')
    len_my_word, len_other = len(my_word), len(other_word)
    if len_my_word != len_other:
        return False

    for i in range(len_other):
        if my_word[i] == '_':
            continue
        # L - usual check. R - check for multiple occurrences of revealed word or lack of it
        if my_word[i] != other_word[i] or my_word.count(my_word[i]) != other_word.count(my_word[i]):
            return False

    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    found_match = False
    my_word = my_word.replace(' ', '')
    l = len(my_word)
    for word in wordlist:
        if len(word) != l:
            continue
        # O(n^2)
        good = True
        for i in range(l):
            if my_word[i] == '_':
                continue
            if my_word[i] != word[i] or my_word.count(word[i]) != word.count(word[i]):
                good = False
                break
        if good:
            found_match = True
            print(word)
    if not found_match:
        print("No matches found")




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    global with_hints
    with_hints = True
    hangman(secret_word)
    with_hints = False



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
