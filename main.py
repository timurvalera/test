import os.path
import pickle
from typing import List


class Book:
    def __init__(self, id: int, name: str, pages: int, author: str):
        self.id = id
        self.name = name
        self.pages = pages
        self.author = author
        self.owner = ''

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


class Library:
    def __init__(self):
        self.books: List[Book] = []
        self.users: List[User] = []

    def add_user(self, name: str, surname: str, age: int):
        """
        Добавление пользователя в бд
        """
        id = 1
        if self.users:
            id = self.users[-1].id + 1
        self.users.append(User(id, name, surname, age))

    def get_user_with_id(self, id: int):
        """
        Эта функция возвращает пользователя

        :param id: ID пользователя, которого нужно получить
        :return: `User` or `None`
        """
        if 1 <= id <= len(self.users):
            return self.users[id - 1]
        print('Такого id нет')
        return None

    def load_users(self, users: List[User]):
        """
        Загрузка пользователей
        """
        self.users = users

    def get_books_of_user(self, user_id: int):
        """
        Эта функция возвращает список книг, находящихся у пользователя
        """
        user = self.get_user_with_id(user_id)
        if user is None:
            return []
        result = []
        for book in self.books:
            if book.owner == user.name:
                result.append(book)
        return result

    def add_book(self, name: str, pages: int, author: str):
        """
        Функция добавления книги в бд

        :param name: название
        :param pages: кол-во страниц
        :param author: автор
        """
        id = 1
        if self.books:
            id = self.books[-1].id + 1
        self.books.append(Book(id, name, pages, author))

    def load_books(self, books: List[Book]):
        """
        Загрузка книг
        """
        self.books = books

    def show_all_books(self):
        """
        Эта функция показывает все свободные книги
        """
        for book in self.books:
            if book.owner == '':
                print(book)

    def get_small_book(self):
        """
        Эта функция находит книгу с минимальным кол-вом страниц
        """
        min_pages = self.books[0].pages
        result_book = self.books[0]
        for i in range(len(self.books)):
            if self.books[i].pages < min_pages:
                min_pages = self.books[i].pages
                result_book = self.books[i]
        return result_book

    def get_big_book(self):
        """
        Эта функция находит книгу с максимальным код-вом страниц
        """
        max_pages = self.books[0].pages
        result_book = self.books[0]
        for i in range(len(self.books)):
            if self.books[i].pages > max_pages:
                max_pages = self.books[i].pages
                result_book = self.books[i]
        return result_book

    def get_book_with_id(self, id: int):
        """
        Получение книги по id
        """
        if 1 <= id <= len(self.books):
            return self.books[id - 1]
        else:
            print('Такого id нет')
            return None

    def get_book_with_name(self, name: str):
        """
        Получение книги по названию
        """
        for book in self.books:
            if book.owner == '':
                if book.name == name:
                    return book
        print('Книги с таким названием нет')
        return None

    def give_book(self, book_name: str, user_id: int):
        """
        Имитация ситуации, когда пользователь берёт себе книгу
        """
        book = self.get_book_with_name(book_name)
        user = self.get_user_with_id(user_id)
        if book and user:
            book.owner = user.name

    def get_book(self, book_name: str, user_id: int):
        """
        Имитация ситуации, когда пользователь возвращает книгу
        """
        books = self.get_books_of_user(user_id)
        for book in books:
            if book.name == book_name:
                book.owner = ''


def load_data(library: Library):
    if os.path.exists('database_users.dat'):
        with open('database_users.dat', 'rb') as f:
            size = pickle.load(f)
            users = []
            for i in range(size):
                users.append(pickle.load(f))
            library.load_users(users)
    else:
        with open('database_users.dat', 'wb') as f:
            pickle.dump(0, f)

    if os.path.exists('database_books.dat'):
        with open('database_books.dat', 'rb') as f:
            size = pickle.load(f)
            books = []
            for i in range(size):
                books.append(pickle.load(f))
            library.load_books(books)
    else:
        with open('database_books.dat', 'wb') as f:
            pickle.dump(0, f)
    return library


def save(file_name: str, data: List):
    """
    Сохранение каких-либо данных
    """
    with open(file_name, 'wb') as f:
        pickle.dump(len(data), f)
        for item in data:
            pickle.dump(item, f)


def main():
    library = load_data(Library())
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
                save('database_books.dat', library.books)
            except ValueError:
                print('Количество страниц должно быть числом')
        elif cmd == '2':
            try:
                name = input('Имя пользователя: ')
                surname = input('Фамилия пользователя: ')
                age = int(input('Возраст пользователя: '))
                library.add_user(name, surname, age)
                save('database_users.dat', library.users)
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
                save('database_books.dat', library.books)
            except ValueError:
                print('ID должен быть числом')
        elif cmd == '7':
            try:
                name = input('Название книги: ')
                user_id = int(input('ID пользователя: '))
                library.get_book(name, user_id)
                save('database_books.dat', library.books)
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


if __name__ == '__main__':
    main()
