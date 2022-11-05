def run():
    dictionary = {
        'key1': 1,
        'key2': 2,
        'key3': 3,
    }
    # print(dictionary)

 
    # print(dictionary['key1'])
    # print(dictionary['key2'])
    # print(dictionary['key3'])

    people = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424,

    } 

    # print(people['Bolivia'])

    # for pais in people.keys():
    #     print(pais)


    # for pais in people.values():
    #     print(pais)

    for pais, poblacion in people.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')

if __name__ == '__main__':
    run()