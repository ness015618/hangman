class Hangman:
    """
    Class to play hangman, characterized by :
    - possible words to find
    - the word to find
    - the number of remaining lives
    - the correctly guessed letters
    - the wrongly guessed letters
    - the number of turns by the player
    - the error count
    """
    
    def __init__(self):
        """Constructor"""
        import random
        
        self.possible_words = ['python', 'hangman', 'computer', 'keyboard', 'programming', 'algorithm', 'function', 'variable', 'syntax', 'debugging', 'compiler', 'software', 'hardware', 'network', 'database', 'interface', 'becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = [letter for letter in self.possible_words[random.randint(0,20)]]
        self.lives = 5
        self.correctly_guessed_letters = ['_' for letter in self.word_to_find]
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0
    
    
    """
    Method that asks the player to enter a letter. 
    If the player guessed a letter well, it is added to correctly_guessed_letters. 
    If not, it is added to the wrongly_guessed_letters and error_count is incremented.
    """
    def play(self):
        is_letter = False
        is_new_input = False
        valid_guess_letter = False
        
        guessed_letter = input("Guess a letter : ")
        
        if len(guessed_letter) == 1 and guessed_letter.isalnum() and not guessed_letter.isdigit(): 
            is_letter = True
        if guessed_letter not in self.wrongly_guessed_letters and guessed_letter not in self.correctly_guessed_letters: 
            is_new_input = True
        if is_letter and is_new_input:
            valid_guess_letter = True