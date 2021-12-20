from list_items import list_items

ITEMS_FILES = [
    './data/cloth.csv'
    './data/drug.csv'
    './data/food.csv'
    './data/movie.csv'
]
CUSTOMER_FILE = './data/customer.csv'

def menu():
    print(
        'Please press the number to select the option:\n',
        '[1] List all items\n',
        '[2] List all info of a specific item\n',
        '[3] Search item by name\n',
        '[4] Search item by item id\n',
        '[5] List all info of a specific customer\n',
        '[6] Placing orders',
    )
    user_input = input('Your choice: ')
    if user_input == '1':
        print('Process...')
        list_items()
    elif user_input == '2':
        print('Process...')
    elif user_input == '3':
        print('Process...')
    elif user_input == '4':
        print('Process...')
    elif user_input == '5':
        print('Process...')
    elif user_input == '6':
        print('Process...')
    else:
        pass


def import_file():
    pass


if __name__ == '__main__':
    import_file()
    menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
