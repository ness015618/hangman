def get_word():
    word = input("(Chooser Player) Put your secret word here : ")
    return word

def get_lives():
    lives = int(input("(Chooser Player) Choose the number of lives : "))
    return lives

def get_guess(suggested_letters):
    guessed_letter = input("(Guesser Player) Guess a letter : ")

    while guessed_letter in suggested_letters or len(guessed_letter) > 1: 
        if len(guessed_letter) > 1:
            invalid_guessed_letter_message = "You can only suggest one letter. "
        elif guessed_letter in suggested_letters:
            invalid_guessed_letter_message = "This letter has already been suggested. "
        guessed_letter = input(f"{invalid_guessed_letter_message} Try again : ")

    suggested_letters.append(guessed_letter)
    return guessed_letter

def assess_guess(secret_word, guessed_letter, lives_left):
    if guessed_letter not in secret_word:
        lives_left -= 1
        print(f"False ! The letter {guessed_letter} is not in the secret word.")
    else:
        print(f"True ! The letter {guessed_letter} is in the secret word.")
    return lives_left

def display_word(secret_word, suggested_letters):
    secret_word_found = False
    secret_word_list = [f"{letter.upper()} " if letter in suggested_letters else '_ ' for letter in secret_word] 
    guessed_secret_word = "".join(letter for letter in secret_word_list) 
    print(guessed_secret_word)
    
    if '_ ' not in secret_word_list:
        secret_word_found = True
    
    return secret_word_found

def main():
    secret_word = get_word()
    min_lives = len(set(secret_word))
    lives = get_lives()
    suggested_letters = []
    game_over = False
    nb_rounds = 0
    word_found = False
    
    while lives < min_lives:
        print(f"Your guesser will need at least {min_lives} to guess your word.")
        lives = get_lives()
    
    while not game_over:
        nb_rounds += 1
        guessed_letter = get_guess(suggested_letters) # returns guessed_letter
        lives = assess_guess(secret_word, guessed_letter, lives) # returns lives
        word_found = display_word(secret_word, suggested_letters) 
        if word_found or lives == 0:
            game_over = True
    
    if word_found:
        score = (f"Congrats, you found the secret word {secret_word.upper()} in {nb_rounds} rounds.")
    else:
        score = (f"You lost, the secret word was {secret_word.upper()}. Better luck next time !")
    
    return print(score)
main()