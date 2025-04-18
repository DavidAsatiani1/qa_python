Для тестирования выбран класс BooksCollector который работает с книгами

Класс BooksCollector содержит:

    Словарь books_genre Название книги: Жанр книги.
    Список favorites избранные книги.
    Список genre доступные жанры.
    Список genre_age_ratingжанры с возрастным рейтингом.
    Набор методов для работы со словарем books_genre и списком favorites:
        add_new_book — добавляет новую книгу в словарь без указания жанра.
        set_book_genre — устанавливает жанр книги
        get_book_genre— выводит жанр книги по её имени.
        get_books_with_specific_genre— выводит список книг с определённым жанром.
        get_books_genre— выводит текущий словарь books_genre.
        get_books_for_children — возвращает книги, которые подходят детям.
        add_book_in_favorites — добавляет книгу в избранное.
        delete_book_from_favorites — удаляет книгу из избранного.
        get_list_of_favorites_books — получает список избранных книг.
