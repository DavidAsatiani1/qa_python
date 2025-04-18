from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    @pytest.mark.parametrize('book_names', ['', 'Название_книги_на_сорок_один_символ_отриц',
                                            'Название_книги_на_сорок_два_символа_отрица'])
    def test_add_new_book_add_negative_book(self, collect, book_names):
        collect.add_new_book(book_names)
        assert len(collect.get_books_genre()) == 0, 'Проверка условия метода не пройдена, книга добавилась'

    def test_set_book_genre_added_genre_book_positive_result(self, collect):
        collect.add_new_book('Большая маленькая ложь')
        collect.set_book_genre('Большая маленькая ложь', 'Детективы')
        assert collect.books_genre.get('Большая маленькая ложь') == 'Детективы'

    def test_set_book_genre_add_genre_is_not_list(self, collect):
        collect.add_new_book('Большая маленькая ложь')
        collect.set_book_genre('Большая маленькая ложь', 'Жанр_которого_нет')
        assert collect.books_genre.get('Большая маленькая ложь') == '', 'Книге добавился жанр которого нет в допустимых жанрах'

    def test_get_book_genre_for_name_positive_result(self, collect):
        collect.add_new_book('Большая маленькая ложь')
        collect.set_book_genre('Большая маленькая ложь', 'Детективы')
        assert collect.get_book_genre('Большая маленькая ложь') == 'Детективы'

    def test_get_books_with_specific_genre_get_two_books_detectiv(self, collect):
        collect.books_genre = {'Большая маленькая ложь': 'Детективы', 'Большая маленькая ложь_1': 'Детективы', 'Большая маленькая ложь_2': 'Ужасы',
                               'Большая маленькая ложь_3': 'Мультфильмы'}
        assert len(collect.get_books_with_specific_genre('Детективы')) == 2

    def test_get_books_for_children_two_books(self, collect):
        collect.books_genre = {'Большая маленькая ложь': 'Мультфильмы', 'Большая маленькая ложь': 'Детективы', 'Большая маленькая ложь': 'Ужасы',
                               'Большая маленькая ложь': 'Комедии'}
        assert len(collect.get_books_for_children()) == 2

    def test_add_book_in_favorites_add_one_book(self, collect):
        collect.add_new_book('Большая маленькая ложь')
        collect.add_book_in_favorites('Большая маленькая ложь')
        assert len(collect.get_list_of_favorites_books()) == 1 and collect.favorites[0] == 'Большая маленькая ложь'

    def test_add_book_in_favorites_add_two_double_book(self, collect):
        collect.add_new_book('Большая маленькая ложь')
        collect.add_book_in_favorites('Большая маленькая ложь')
        collect.add_book_in_favorites('Большая маленькая ложь')
        assert len(collect.get_list_of_favorites_books()) == 1, 'В избранное добавился дубль книги'

    def test_delete_book_from_favorites(self, collect):
        collect.add_new_book('Большая маленькая ложь')
        collect.add_book_in_favorites('Большая маленькая ложь')
        collect.delete_book_from_favorites('Большая маленькая ложь')
        assert len(collect.favorites) == 0