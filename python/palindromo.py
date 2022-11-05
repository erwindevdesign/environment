def palindromo(word):
    word = word.replace(' ', '')
    word = word.lower()
    word_invert = word[::-1]
    if word == word_invert:
        return True
    else:
        return False


def run():
    word = input('Ingress the word: ')
    is_palindromo = palindromo(word)
    if is_palindromo == True:
        print('Is palindrome')
    else:
        print('Not is palindromo')


if __name__=='__main__':
    run()


