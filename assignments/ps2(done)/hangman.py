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
import string

WORDLIST_FILENAME = "words.txt"


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
    print("  ", len(wordlist), "words loaded.")
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
    is_guessed = [l in letters_guessed for l in secret_word]
    
    return all(is_guessed)




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ''
    for l in secret_word:
        if l in letters_guessed:
          guessed_word += l
        else:
          guessed_word += '_ '
    return guessed_word 




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = [l for l in string.ascii_lowercase if l not in letters_guessed]    
    return ''.join(available_letters)
    


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
    print('Welcome to the game Hangman')
    print('I am thinking of a word that is', len(secret_word), 'letter long')
    print('--------------------')    
    letters_guessed = []
    number_of_guesses = 6
    warning_left = 3
    while(not is_word_guessed(secret_word, letters_guessed) and number_of_guesses > 0):
      print('You have', number_of_guesses, 'guesses left')
      print('Available letters are', get_available_letters(letters_guessed))
      warning_message = 'Oops! That is not a valid letter. You have'
      user_input = input('please guess a letter: ')
      user_input = user_input.lower()
      is_alpha = user_input.isalpha()
      already_guessed = user_input in letters_guessed
      if (not is_alpha) or already_guessed:
        warning_left -= 1
        if already_guessed:
          warning_message = 'The letter has already been guessed before,'
        if warning_left >= 0:
          print(warning_message, warning_left, 'warning left:', get_guessed_word(secret_word, letters_guessed))
        else:
          number_of_guesses -= 1
          print(warning_message)
          print('You have no warning, so you loose one guess')
        
        print('------------------')
        continue
        
      letters_guessed.append(user_input)
      if(user_input in secret_word):
        print('Good guess:', get_guessed_word(secret_word, letters_guessed))
      else:
        print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
        number_of_guesses -= 1
        if user_input in 'aeiou':
          number_of_guesses -= 1
      print('-------------------')
        
    if(is_word_guessed(secret_word, letters_guessed)):
      print('Congratulation, you won!')
      unique_letters = ''
      for l in secret_word:
        if l not in unique_letters:
          unique_letters += l        
      print('Your total score for the game is:', number_of_guesses * len(unique_letters))
    
    if(number_of_guesses <= 0):
      print('You lost')
      print('The word is:', secret_word)
      


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
  my_word = my_word.strip()
  my_word = my_word.replace(" ", "")
  known_letters = ''.join([l for l in my_word if l != '_'])
  if(len(my_word) != len(other_word)):
    return False
  is_matched = [True for l in my_word]
  i = 0
  for l in my_word:
    if l != '_':
      is_matched[i] = l == other_word[i]
    else:
      is_matched[i] = other_word[i] not in known_letters
    i += 1
  return(all(is_matched))
    


def show_possible_matches(my_word):
  '''
  my_word: string with _ characters, current guess of secret word
  returns: nothing, but should print out every word in wordlist that matches my_word
            Keep in mind that in hangman when a letter is guessed, all the positions
            at which that letter occurs in the secret word are revealed.
            Therefore, the hidden letter(_ ) cannot be one of the letters in the word
            that has already been revealed.
  '''
  possible_matches = ''
  for word in wordlist:
    if(match_with_gaps(my_word, word)):
      possible_matches += word
      possible_matches += " "

  if(len(possible_matches) < 1):
    print('There is no match')
  else:
    print(possible_matches)

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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman')
    print('I am thinking of a word that is', len(secret_word), 'letter long')
    print('--------------------')    
    letters_guessed = []
    number_of_guesses = 6
    warning_left = 3
    while(not is_word_guessed(secret_word, letters_guessed) and number_of_guesses > 0):
      print('You have', number_of_guesses, 'guesses left')
      print('Available letters are', get_available_letters(letters_guessed))
      warning_message = 'Oops! That is not a valid letter. You have'
      user_input = input('please guess a letter: ')
      user_input = user_input.lower()
      is_alpha = user_input.isalpha()
      already_guessed = user_input in letters_guessed
      if user_input == '*':
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        print('--------------------')   
        continue
      if (not is_alpha) or already_guessed:
        warning_left -= 1
        if already_guessed:
          warning_message = 'The letter has already been guessed before,'
        if warning_left >= 0:
          print(warning_message, warning_left, 'warning left:', get_guessed_word(secret_word, letters_guessed))
        else:
          number_of_guesses -= 1
          print(warning_message)
          print('You have no warning, so you loose one guess')
        
        print('------------------')
        continue
        
      letters_guessed.append(user_input)
      if(user_input in secret_word):
        print('Good guess:', get_guessed_word(secret_word, letters_guessed))
      else:
        print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
        number_of_guesses -= 1
        if user_input in 'aeiou':
          number_of_guesses -= 1
      print('-------------------')
        
    if(is_word_guessed(secret_word, letters_guessed)):
      print('Congratulation, you won!')
      unique_letters = ''
      for l in secret_word:
        if l not in unique_letters:
          unique_letters += l        
      print('Your total score for the game is:', number_of_guesses * len(unique_letters))
    
    if(number_of_guesses <= 0):
      print('You lost')
      print('The word is:', secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":

  #show_possible_matches("a_pl_")
  #secret_word = choose_word(wordlist)
  #hangman(secret_word)
  #print(match_with_gaps("a_ _ le", "apple"))
  #show_possible_matches("a_ pl_ ")

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
