import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()

# Тест на удаление книги из избранного
def test_delete_book_from_favorites(collector):
    collector.add_book_in_favorites("Новая книга")
    collector.delete_book_from_favorites("Новая книга")
    assert "Новая книга" not in collector.get_list_of_favorites_books()