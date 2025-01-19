import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


# Тест на получение списка книг с конкретным жанром
def test_get_books_with_specific_genre(collector):
    collector.set_book_genre("Новая книга", "Фантастика")
    collector.set_book_genre("1984", "Фантастика")
    books = collector.get_books_with_specific_genre("Фантастика")
    assert "Новая книга" in books
    assert "1984" in books