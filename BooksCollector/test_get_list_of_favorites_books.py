import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()

# Тест на получение списка избранных книг
def test_get_list_of_favorites_books(collector):
    collector.add_book_in_favorites("Новая книга")
    collector.add_book_in_favorites("1984")
    favorites = collector.get_list_of_favorites_books()
    assert "Новая книга" in favorites
    assert "1984" in favorites