import random


def run():
    aleatory_number = random.randint(1, 100)
    ingres_number = int(input('Ingres a number between 1 and 100: '))
    while ingres_number != aleatory_number:
        if ingres_number < aleatory_number:
            print('Enter a larger number!')
        else:
            print('Enter a lower number!')
        ingres_number = int(input('Choose a diferent number please.'))
    print('Congratulations, You WIN !!')



if __name__ == '__main__':
    run()