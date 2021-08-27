def load_words():
    with open('/home/pi/projects/spellingbee/words.txt', 'r') as words:
        the_words = set(words.read().split())
    return the_words


def letters_list(letters):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    for letter in letters:
        try:
            alpha.remove(letter)
        except:
            print("Error!")
            alpha=['b', 'r', 'o', 'k', 'e', 'n']
            return alpha
    return alpha


def split_the_letters(the_l):
    return list(the_l)


def solve(game_letters):
    dictionary = load_words()
    given_letters = split_the_letters(str(game_letters).lower())
    l = letters_list(given_letters)
    good_words = []
    for word in dictionary:
        bad_word = False
        if len(word) <= 3 or (given_letters[3] not in word) or word.islower() is False or ('\'' in word):
            continue
        for letter in l:
            if letter in word:
                bad_word = True
                break
        if bad_word:
            continue
        else:
            good_words.append(word)
    return sorted(good_words)
