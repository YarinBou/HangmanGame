def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    the function check if the user input is valid.
    if it is a new letter = return true ;
    else return true
    :param letter_guessed:
    :return:true or false
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


def main():
    user_guessed = input("Guess a letter: ")
    old_letters = ['a', 'p', 'c', 'f']
    print(try_update_letter_guessed(user_guessed, old_letters))
    return


if __name__ == '__main__':
    main()
