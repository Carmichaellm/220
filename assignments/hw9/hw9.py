from random import randint

def get_words(file_name):
    words_list = []
    words_file = open(file_name, 'r')
    for line in words_file.readlines():
        words_list.append(line)
    return words_list


def get_random_word(words):
    rand_word = words[randint(0,len(words))]
    return rand_word


def letter_in_secret_word(letter, secret_word):
    for i in secret_word:
        if i == letter:
            return True
    return False


def already_guessed(letter, guesses):
    for i in guesses:
        if i == letter:
            return True
    return False


def make_hidden_secret(secret_word, guesses):
    hidden_secret_word_list = []
    hidden_secret_word = ''
    for i in secret_word:
        for j in guesses:
            if i == j:
                hidden_secret_word_list.append(j + ' ')
            else:
                hidden_secret_word_list.append('_ ')
    for k in hidden_secret_word_list:
        hidden_secret_word = hidden_secret_word + k
    hidden_secret_word = hidden_secret_word.rstrip()
    return hidden_secret_word


def won(guessed):
    for i in guessed:
        if i == '_':
            return False
        return True


def play_graphics(secret_word):
    guessed = []
    guesses = 6
    guess = ''
    hidden = make_hidden_secret(secret_word, guessed)
    while not won(hidden):
        print("already guessed:", guessed)
        print("guesses remaining:", guesses)
        print(hidden)
        guess = input("guess a letter: ")
        if not already_guessed(guess, guessed):
            if letter_in_secret_word(guess, secret_word):
                guessed.append(guess)
                hidden = make_hidden_secret(secret_word, guessed)
            else:
                guessed.append(guess)



def play_command_line(secret_word):
    pass


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
