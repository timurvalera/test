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