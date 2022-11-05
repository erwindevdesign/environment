import random

def create():
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    simbol = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracter = upper + lower + simbol + number

    password = []
    
    for i in range(8):
        caracter_random = random.choice(caracter)
        password.append(caracter_random)
    password = "".join(password)
    return password
    

def run():
    password = create()
    print('You new password is: ' + password)



if __name__ == '__main__':
    run()