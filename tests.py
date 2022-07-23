from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test


class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_rating_0(self):  # рейтинг меньше 1 присвоить нельзя
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 0)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') != 0

    def test_set_book_rating_12(self):  # рейтинг больше 11 присвоить нельзя
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 12)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') != 12

    def test_set_book_raiting_11(self):  # можно присваивать рейтинг меньше 10 и больше 1
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 9)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 9

    def test_set_book_rating_book_not_in_list(self):  # нельзя присвоить рейтинг книги , которая не в списке книиг
        collector = BooksCollector()
        collector.set_book_rating('Гордость и предубеждение и зомби', 2)
        assert len(collector.books_rating) == 0

    def test_get_book_rating_by_name(self):  # получаем рейтинг книги по ее имени
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    def test_get_book_rating_withour_rating(self):#нет рейтинга у книги , которая еще не добавлена
        collector = BooksCollector()
        assert collector.get_book_rating('Гордость и предубеждение и зомби') is None

    def test_get_books_with_specific_rating_1(self): # выводим список книг с определенным рейтингом
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_books_with_specific_rating(1)

