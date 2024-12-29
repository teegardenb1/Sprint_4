import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

# Тест на получение жанра книги
def test_get_book_genre(collector):
    collector.set_book_genre("Новая книга", "Фантастика")
    assert collector.get_book_genre("Новая книга") == "Фантастика"
