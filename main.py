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


class Library:
    def __init__(self):
        self.books: List[Book] = []
        self.users: List[User] = []

    def add_user(self, name: str, surname: str, age: int):
        """
        Добавление пользователя в бд

        :param name: имя
        :param surname: фамилия
        :param age: возраст
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

    def get_books_of_user(self, user_id: int):
        """
        Эта функция возвращает список книг, находящихся у пользователя
        """
        user = self.get_user_with_id(user_id)
        if user is None:
            return []
        result = []
        for book in self.books:
            if book.owner == user:
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

    def show_all_books(self):
        """
        Эта функция показывает все свободные книги
        """
        for book in self.books:
            if book.owner is None:
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
            if book.owner is None:
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
            book.owner = user

    def get_book(self, book_name: str, user_id: int):
        """
        Имитация ситуации, когда пользователь возвращает книгу
        """
        books = self.get_books_of_user(user_id)
        for book in books:
            if book.name == book_name:
                book.owner = None


def main():
    book = Book(0, 'a', 12, 'a')
    print(book.id)


