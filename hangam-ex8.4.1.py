def print_hangman(num_of_tries):
    return HANGMAN_PHOTOS[str(num_of_tries)]


HANGMAN_PHOTOS = {"1": "x-------x", "2": """ 
        x-------x
        |
        |
        |
        |
        |
        """, "3": """ 
        x-------x
        |       |
        |       0
        |
        |
        |
    """, "4": """ 
        picture 4:
        x-------x
        |       |
        |       0
        |       |
        |
        |

        """, "5": """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |
        """, "6": """ 
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |

    """, "7": """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |

        """}


def main():
    print(print_hangman(7))


if __name__ == '__main__':
    main()
