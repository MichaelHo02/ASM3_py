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

items = {
    '1': {'qty': 60, 'name': 'They Call Me Bruce?', 'genre': 'Comedy', 'studio': 'Mante Group', 'price': 4.87, 'rating': 2},
    '2': {'qty': 90, 'name': 'I Am Curious', 'genre': 'Documentary|Drama', 'studio': 'Kilback, Olson and Adams', 'price': 5.48, 'rating': 4},
    '3': {'qty': 77, 'name': 'a', 'genre': 'Documentary|Thriller', 'studio': 'Orwin-Wiza', 'price': 1.99, 'rating': 1},
    '4': {'qty': 75, 'name': 'Just the Ticket', 'genre': 'Comedy|Romance', 'studio': 'Senger, King and Schaefer', 'price': 2.33, 'rating': 2},
    '5': {'qty': 23, 'name': 'Arguing the World', 'genre': 'Documentary', 'studio': 'Donnelly-Roob', 'price': 4.99, 'rating': 3},
    '6': {'qty': 87, 'name': 'O Auto da Compadecida', 'genre': 'Adventure|Comedy', 'studio': 'Bins, Predovic and Wiza', 'price': 8.99, 'rating': 5},
    '7': {'qty': 44, 'name': 'Pure Formality', 'genre': 'Crime|Film-Noir|Mystery|Thriller', 'studio': 'Hayes-Hansen', 'price': 6.49, 'rating': 5},
    '8': {'qty': 77, 'name': 'Sublime', 'genre': 'Horror|Thriller', 'studio': 'Swift-Botsford', 'price': 9.99, 'rating': 5},
    '9': {'qty': 69, 'name': 'Direct Action', 'genre': 'Action|Crime|Thriller', 'studio': 'Hudson-Nolan', 'price': 10.99, 'rating': 5},
    '10': {'qty': 59, 'name': 'Devil and Max Devlin', 'genre': 'Comedy|Fantasy', 'studio': 'Swift LLC', 'price': 2.39, 'rating': 4},
    '11': {'qty': 85, 'name': 'Friday After Next', 'genre': 'Comedy', 'stduio': 'Roob LLC', 'price': 4.50, 'rating': 3},
    '12': {'qty': 65, 'name': 'Come On, Rangers', 'genre': 'Romance|Western', 'studio': 'Krajcik-Jacobs', 'price': 6.49, 'rating': 3},
    '13': {'qty': 54, 'name': 'Walk Softly, Stranger', 'genre': 'Crime|Drama|Film-Noir|Romance', 'studio': 'Mante LLC', 'price': 7.99, 'rating': 3},
    '14': {'qty': 64, 'name': 'Michael Collins', 'genre': 'Drama', 'studio': 'Bechtelar, Lindgren and Macejkovic', 'price': 8.99, 'rating': 5},
    '15': {'qty': 44, 'name': 'Convict 13', 'genre': 'Comedy', 'studio': 'Haag, Jast and Towne', 'price': 6.99, 'rating': 4},
    '16': {'qty': 66, 'name': 'Fool There Was, A', 'genre': 'Drama', 'studio': 'Koelpin, Koelpin and Dibbert', 'price': 5.99, 'rating': 3},
    '17': {'qty': 77, 'name': 'Paranormal Activity: The Marked Ones', 'genre': 'Horror|Thriller', 'studio': 'Kuvalis and Sons', 'price': 3.99, 'rating': 3},
    '18': {'qty': 88, 'name': 'We Need to Talk About Kevin', 'genre': 'Drama|Thriller', 'studio': 'McCullough, Swift and Bode','price': 2.99, 'rating': 3},
    '19': {'qty': 92, 'name': 'Star Wars: Episode I - The Phantom Menace', 'genre': 'Action|Adventure|Sci-Fi', 'studio': 'Corwin-Wiza', 'price': 0.99, 'rating': 1},
    '20': {'qty': 23, 'name': 'The Golden Voyage of Sinbad', 'genre': 'Action|Adventure|Fantasy', 'studio': 'Schuster, Schinner and Lynch', 'price': 1.99, 'rating': 2},
}




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
