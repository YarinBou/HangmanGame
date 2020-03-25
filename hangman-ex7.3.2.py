def check_win(secret_word, old_letters_guessed):
    hidden_word = show_hidden_word(secret_word, old_letters_guessed)
    if hidden_word.count("_") > 0:
        print(hidden_word)
        return False
    else:
        print(hidden_word)
        return True


def show_hidden_word(secret_word, old_letters_guessed):
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
    secret_word = "friends"
    old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k', 'f']
    print(check_win(secret_word, old_letters_guessed))
    secret_word2 = "yes"
    old_letters_guessed2 = ['d', 'g', 'e', 'i', 's', 'k', 'y']
    print(check_win(secret_word2, old_letters_guessed2))


if __name__ == '__main__':
    main()
