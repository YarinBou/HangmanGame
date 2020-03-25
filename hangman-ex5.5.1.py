def is_valid_input(letter_guessed):
    """
    the function check if the user input is valid.

    :param letter_guessed:
    :return:true or false
    """
    if (len(letter_guessed) > 1) or (not (letter_guessed.isalpha())):
        print(False)
        return
    else:
        print(True)
        return


def main():
    user_guess = input("Guess a letter: ")
    is_valid_input(user_guess)
    return


if __name__ == '__main__':
    main()
