def choose_word(file_path, index):
    file_txt = open(file_path, "r")
    words_in_list = []
    for line in file_txt:
        current_word = (line.split(" "))
        words_in_list = current_word
    words_in_list_without_dupplicate = []
    for word in words_in_list:
        if word in words_in_list_without_dupplicate:
            continue
        else:
            words_in_list_without_dupplicate.append(word)
    number_of_elements = len(words_in_list_without_dupplicate)

    if index < len(words_in_list):
        return words_in_list[index - 1], number_of_elements
    elif index > len(words_in_list):
        actual_num = (index % len(words_in_list))
        return words_in_list[actual_num - 1], number_of_elements


def main():
    print(choose_word(r"C:\ptxt\hangman words.txt", 3))
    print(choose_word(r"C:\ptxt\hangman words.txt", 15))


if __name__ == '__main__':
    main()
