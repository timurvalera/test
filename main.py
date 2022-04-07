from typing import List

class Book:
    def __init__(self, id: int, name: str, pages: int, author: str):
        self.id = id
        self.name = name
        self.pages = pages
        self.author = author
        self.owner = None

    def __str__(self):
        return f'{self.id} - "{self.name}" ({self.author})'


class User:
    def __init__(self, id: int, name: str, surname: str, age: int):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f'{self.id} - {self.name} {self.surname}'


def main():
    library = Library()
    end = False
    while not end:
        print('''Доступные команды:
        0. Выход
        1. Добавить книгу в библиотеку
        2. Добавить пользователя
        3. Список всех доступных книг
        4. Книга с самым большим количеством страниц
        5. Книга с самым маленьким количеством страниц
        6. Выдать книгу пользователю
        7. Забрать книгу у пользователя
        8. Просмотр всех книг пользователя''')
        cmd = input('Введите номер команды: ')
        if cmd == '0':
            end = True
        elif cmd == '1':
            try:
                name = input('Название книги: ')
                pages = int(input('Количество страниц в книге: '))
                author = input('Автор книги: ')
                library.add_book(name, pages, author)
            except ValueError:
                print('Количество страниц должно быть числом')
        elif cmd == '2':
            try:
                name = input('Имя пользователя: ')
                surname = input('Фамилия пользователя: ')
                age = int(input('Возраст пользователя: '))
                library.add_user(name, surname, age)
            except ValueError:
                print('Возраст пользователя должен быть числом')
        elif cmd == '3':
            library.show_all_books()
        elif cmd == '4':
            print(library.get_big_book())
        elif cmd == '5':
            print(library.get_small_book())
        elif cmd == '6':
            try:
                name = input('Название книги: ')
                user_id = int(input('ID пользователя: '))
                library.give_book(name, user_id)
            except ValueError:
                print('ID должен быть числом')
        elif cmd == '7':
            try:
                name = input('Название книги: ')
                user_id = int(input('ID пользователя: '))
                library.get_book(name, user_id)
            except ValueError:
                print('ID должен быть числом')
        elif cmd == '8':
            try:
                user_id = int(input('ID пользователя: '))
                books = library.get_books_of_user(user_id)
                for book in books:
                    print(book)
            except ValueError:
                print('ID должен быть числом')
        print()

