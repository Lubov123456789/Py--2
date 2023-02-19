# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union


class Headphones:
    def __init__(self, db: Union[int, float], wireless: bool, color: str):
        """
        Инициализация класса Наушники
        :param db: громкость наушников
        :param wireless: проводные/беспроводные
        :param color: выбор цвета наушников
        """
        self._db = db
        if not isinstance(wireless, bool):
            raise TypeError
        self._wireless = wireless
        self._color = color

    @property
    def db(self)-> Union[int,float]:
        return self._db

    @db.setter
    def db(self, new_db) -> None:
        if not isinstance(new_db, Union[int,float]):
            raise TypeError
        elif 0 > new_db > 999999:
            raise ValueError
        self._db = new_db

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, new_color):
        if not isinstance(new_color, str):
            raise TypeError
        self._color = new_color

    def choose_jack(self, cable: str):
        """
        Выбор кабеля если наушники проводные
        :param cable: формат кабеля
        :return: требуемый кабель
        """
        if self._wireless is False:
            self._cable = cable
            ...

    def studio_or_home(self):
        """
        метод для уточнения области использования наушников
        :return: область использования наушников
        """
        ...


class Online_cinema:
    def __init__(self, name: str, audience: int):
        """
        Инициализация класса Онлайн кинотеатр
        :param name: название онлайн кинотеатра
        :param audience: аудитория онлайн кинотеатра
        """
        self._name = name
        self._audience = audience

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError
        self._name = new_name

    @property
    def audience(self) -> int:
        return self._audience

    @audience.setter
    def audience(self, new_audience):
        if not isinstance(new_audience, int):
            raise TypeError
        elif 0 > new_audience > 8_000_000_000:
            raise ValueError

    def list_of_films(self):
        """

        :return: список фильмов в онлайн кинотеатре
        """
        ...

    def subscription_price(self):
        """

        :return: цена подписки для выбранного онлайн кинотеатра
        """
        ...


class Text:
    def __init__(self, language: str, pt: Union[int, float]):
        """
        Инициализуруем текст
        :param language: язык текста
        :param pt: размер шрифта
        """
        self._language = language
        self._pt = pt

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, name_of_lan):
        if not isinstance(name_of_lan, str):
            raise TypeError
        self._language = name_of_lan

    @property
    def pt(self):
        return self._pt

    @pt.setter
    def pt(self, size):
        if not isinstance(size, Union[int, float]):
            raise TypeError
        elif 0 >= size:
            raise ValueError
        self._pt = size

    def translate(self):
        """
        Перевод текста с одного языка на другой
        :return: переведенный текст
        """
        ...

    def change_font(self, font: str):
        """
        Меняет шрифт текста
        :param font: требуемый шрифт
        :return: текст в новом шрифте
        """
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    headphones = Headphones(120, True, 'Red')
    print(headphones.color)
    word = Text('eng', 24)
    print(word.language)
    cinema = Online_cinema('Kinopoisk', 20_000_000)
    print(cinema.audience)
    pass
