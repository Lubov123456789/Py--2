class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self.name


    @property
    def author(self) -> str:
        return self.author


    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}," \
              f" author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages_new: int) -> None:
        if not isinstance(pages_new, int):
            raise TypeError
        if pages_new <= 0:
            raise ValueError
        self._pages = pages_new

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}," \
              f" author={self._author!r}, pages = {self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration_new: float) -> None:
        if not isinstance(duration_new, float):
            raise TypeError
        if duration_new <= 0:
            raise ValueError
        self._duration = duration_new

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}," \
               f" author={self._author!r}, pages = {self.duration!r})"


