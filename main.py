from customers import list_customer
from items import list_items, get_item_info, order
from searching import search_name, search_id

ITEMS_FILES = [
    './data/cloth.csv'
    './data/drug.csv'
    './data/food.csv'
    './data/movie.csv'
]
CUSTOMER_FILE = './data/customer.csv'


def menu():
    while True:
        print(
            'Please press the number to select the option:\n',
            '[1] List all items\n',
            '[2] List all info of a specific item\n',
            '[3] Search item by name\n',
            '[4] Search item by item id\n',
            '[5] List all info of a specific customer\n',
            '[6] Placing orders\n',
            "[exit] to exit the program"
        )
        user_input = input('Your choice: ')
        if user_input == '1':
            print('Process...')
            list_items()
        elif user_input == '2':
            print('Process...')
            get_item_info()
        elif user_input == '3':
            print('Process...')
            search_name('a')
        elif user_input == '4':
            print('Process...')
            search_id('a')
        elif user_input == '5':
            print('Process...')
            list_customer()
        elif user_input == '6':
            print('Process...')
            order()
        elif user_input.lower() == 'exit':
            break
        else:
            print('Invalid message. Try again!')


if __name__ == '__main__':
    menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
