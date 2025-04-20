from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если Ваш кот хочет Вас убить')
        assert len(collector.get_books_rating()) == 2

    @pytest.mark.parametrize('book_names', ['', 'Название_книги_на_сорок_один_символ_отриц',
                                            'Название_книги_на_сорок_два_символа_отрица'])
    def test_add_new_book_add_negative_book(self, book_names):
        collector = BooksCollector()
        collector.add_new_book(book_names)
        assert len(collector.get_books_genre()) == 0, 'Проверка условия метода не пройдена, книга добавилась'

    @pytest.mark.parametrize('name', ['Большая маленькая ложь',
                                      'Мы'])
    def test_add_new_book_add_negative_book(self, book_names):
        collector = BooksCollector()
        collector.add_new_book(book_names)
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre_added_genre_book_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book('Большая маленькая ложь')
        collector.set_book_genre('Большая маленькая ложь', 'Детективы')
        assert collector.books_genre.get('Большая маленькая ложь') == 'Детективы'

    def test_set_book_genre_add_genre_is_not_list(self):
        collector = BooksCollector()
        collector.add_new_book('Большая маленькая ложь')
        collector.set_book_genre('Большая маленькая ложь', 'Жанр_которого_нет')
        assert collector.books_genre.get('Большая маленькая ложь') == '', 'Книге добавился жанр которого нет в допустимых жанрах'

    def test_get_book_genre_for_name_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book('Большая маленькая ложь')
        collector.set_book_genre('Большая маленькая ложь', 'Детективы')
        assert collector.get_book_genre('Большая маленькая ложь') == 'Детективы'

    def test_get_books_with_specific_genre_get_two_books_detectiv(self):
        collector = BooksCollector()
        collector.books_genre = {'Большая маленькая ложь': 'Детективы', 'Большая маленькая ложь_1': 'Детективы', 'Большая маленькая ложь_2': 'Ужасы',
                                 'Большая маленькая ложь_3': 'Мультфильмы'}
        assert len(collector.get_books_with_specific_genre('Детективы')) == 2

    def test_get_books_for_children_two_books(self):
        collector = BooksCollector()
        collector.books_genre = {'Большая маленькая ложь': 'Мультфильмы', 'Большая маленькая ложь_1': 'Детективы', 'Большая маленькая ложь_2': 'Ужасы',
                                 'Большая маленькая ложь_3': 'Комедии'}
        assert len(collector.get_books_for_children()) == 2

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Большая маленькая ложь')
        collector.add_book_in_favorites('Большая маленькая ложь')
        assert len(collector.get_list_of_favorites_books()) == 1 and collector.favorites[0] == 'Большая маленькая ложь'

    def test_add_book_in_favorites_add_two_double_book(self):
        collector = BooksCollector()
        collector.add_new_book('Большая маленькая ложь')
        collector.add_book_in_favorites('Большая маленькая ложь')
        collector.add_book_in_favorites('Большая маленькая ложь')
        assert len(collector.get_list_of_favorites_books()) == 1, 'В избранное добавился дубль книги'

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Большая маленькая ложь')
        collector.add_book_in_favorites('Большая маленькая ложь')
        collector.delete_book_from_favorites('Большая маленькая ложь')
        assert len(collector.favorites) == 0