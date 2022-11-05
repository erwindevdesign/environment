def run():
    # for count in range(1001):
    #     if count % 2 != 0:
    #         continue
    #     print(count)

    # for i in range(10001):
    #     print(i)
    #     if i == 5678:
    #         break

    text = input('Escribe un texto: ')
    for letter in text:
        if letter == 'o':
            break
        print(letter)

if __name__ == '__main__':
    run()