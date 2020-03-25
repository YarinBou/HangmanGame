def check_valid_input(letter_guessed, old_letters_guessed):
    """
    the function check if the user input is valid.
    if it is a new letter = return true ;
    else return true
    :param letter_guessed:
    :return:true or false
    """
    if (len(letter_guessed) > 1) or (not (letter_guessed.isalpha())) or (letter_guessed in old_letters_guessed):
        return False
    else:
        old_letters_guessed.append(letter_guessed)
        return True


def main():
    user_guessed = input("Guess a letter: ")
    old_letters = old_letters = ['a', 'b', 'c']
    print(check_valid_input(user_guessed, old_letters))
    return


if __name__ == '__main__':
    main()
