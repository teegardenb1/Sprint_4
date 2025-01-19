import pytest
from main import BooksCollector

@pytest.mark.parametrize("name, genre", [("Новая книга", "Фантастика"), ("Зелёная миля", "Ужасы")])
def test_set_book_genre(name, genre):
    collector = BooksCollector()
    collector.set_book_genre(name, genre)
    assert collector.get_book_genre(name) == genre
