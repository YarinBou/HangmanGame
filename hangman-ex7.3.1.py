def show_hidden_word(secret_word, old_letters_guessed):
    """

    :param secret_word:
    :param old_letters_guessed:
    :return:
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


def main():
    secret_word = "Yarin bouzaglo"
    old_letters_guessed = ['y', 'i', 'n', 'm', 'z', 'l', 'a']
    print(show_hidden_word(secret_word, old_letters_guessed))
    return


if __name__ == '__main__':
    main()
