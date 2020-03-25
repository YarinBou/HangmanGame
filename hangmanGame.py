HANGMAN_OPENING_FILE = """ 
                Let the games begin                                       
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
"""
MAX_TRIES = 6
HANGMAN_PHOTOS = {0: "  x-------x", 1: """ 
            x-------x
            |
            |
            |
            |
            |
        """, 2: """ 
            x-------x
            |       |
            |       0
            |
            |
            |
    """, 3: """ 
            x-------x
            |       |
            |       0
            |       |
            |
            |

        """, 4: """
            x-------x
            |       |
            |       0
            |      /|\\
            |
            |
        """, 5: """ 
            x-------x
            |       |
            |       0
            |      /|\\
            |      /
            |

    """, 6: """
            x-------x
            |       |
            |       0
            |      /|\\
            |      / \\
            |

        """}


def choose_word(file_path, index):
    """
    :param file_path:  a string representing a path to a text file containing spaces separated by words
    :param index: integer representing a particular word's placement in the file.
    :return: a tuple consisting of two organs. the word in the right inedex and the right numbers of words in the list.
    """
    file_txt = open(file_path, "r")
    words_in_list = []
    for line in file_txt:
        current_word = (line.split(" "))
        words_in_list = current_word
    words_in_list_without_duplicate = []
    for word in words_in_list:
        if word in words_in_list_without_duplicate:
            continue
        else:
            words_in_list_without_duplicate.append(word)
    number_of_elements = len(words_in_list_without_duplicate)

    if index < len(words_in_list):
        return words_in_list[index - 1], number_of_elements
    elif index > len(words_in_list):
        actual_num = (index % len(words_in_list))
        return words_in_list[actual_num - 1], number_of_elements


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    The function uses the check_valid_input.
    If the character is invalid or has already guessed the character in the past,
    the function prints the character X (as a big letter),
    below it the list of letters already guessed and returns false.
    If the character is incorrect and has not been guessed before -
    the function adds the character to the guess list and returns true.
    :param old_letters_guessed: list
    :param letter_guessed:char
    :return true or false
    """
    if (len(letter_guessed) > 1) or (not (letter_guessed.isalpha())) or (letter_guessed in old_letters_guessed):
        print("X")
        sort = sorted(old_letters_guessed)
        arrow = " -> "
        print(arrow.join(sort))
        return False
    else:
        old_letters_guessed.append(letter_guessed)
        return True


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Boolean function that receives a character and a list of letters that the user has previously guessed.
    The function checks two things: the correctness of the input and whether it is legal to guess this signal
    (i.e., the player has not guessed this signal before) and returns true or false accordingly.
    :param old_letters_guessed: list
    :param letter_guessed: char
    :return: true or false
    """
    if (len(letter_guessed) > 1) or (not (letter_guessed.isalpha())) or (letter_guessed in old_letters_guessed):
        return False
    else:
        old_letters_guessed.append(letter_guessed)
        return True


def show_hidden_word(secret_word, old_letters_guessed):
    """
    A function that returns a string consisting of letters and underscores.
    The string displays the letters from the old_letters_guessed list that are in the secret_word string
    in their respective positions,
    and the rest of the letters in the string (which the player has not yet guessed) as underscores.
    :param secret_word: string
    :param old_letters_guessed: list
    :return: string
    """
    secret_word = secret_word.lower()
    hidden_word = ""
    for char in secret_word:
        if char in old_letters_guessed:
            hidden_word += char + " "
            continue
        else:
            space = " _ "
            hidden_word += space

    return hidden_word


def check_win(secret_word, old_letters_guessed):
    """
    Boolean function that returns true if all the letters that make up the secret word are included
    in the list of letters the user guessed.
    Otherwise, the function returns false.
    :param secret_word: string
    :param old_letters_guessed: list
    :return: true or false.
    """
    hidden_word = show_hidden_word(secret_word, old_letters_guessed)
    if hidden_word.count("_") > 0:
        return False
    else:
        return True


def opening_view():
    print(HANGMAN_OPENING_FILE)
    print(MAX_TRIES)


def hangman_game(secret_word):
    num_of_tries = 0
    old_letter_guessed = []
    print("Let's start!")
    print(HANGMAN_PHOTOS[num_of_tries])
    print(show_hidden_word(secret_word, old_letter_guessed))
    player_guess = input("Guess a letter: ")
    while num_of_tries < MAX_TRIES:
        if check_valid_input(player_guess, old_letter_guessed):
            if player_guess in secret_word:
                print(show_hidden_word(secret_word, old_letter_guessed))
                if check_win(secret_word, old_letter_guessed):
                    print("WIN")
                    return
                player_guess = input("Guess a letter: ")
                continue
            else:
                num_of_tries += 1
                print(":(")
                print(HANGMAN_PHOTOS[num_of_tries])
                print(show_hidden_word(secret_word, old_letter_guessed))
                player_guess = input("Guess a letter: ")
                continue
        else:
            try_update_letter_guessed(player_guess, old_letter_guessed)
            player_guess = input("Guess a letter: ")
            continue
    print(show_hidden_word(secret_word, old_letter_guessed))
    print("LOSE")


def main():
    opening_view()
    file_path = input("Enter file path: ")
    index = int(input("Enter index: "))
    tuple_words = choose_word(file_path, index)
    secret_word = tuple_words[0]
    hangman_game(secret_word)


if __name__ == '__main__':
    main()
