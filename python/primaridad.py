def prime_number(number):
    count = 0

    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False

def run():
    number = int(input('Write a numbre: '))
    if prime_number(number):
        print('Is prime')
    else:
        print('Not is prime')


if __name__ == '__main__':
    run()