import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

# Тест на добавление новой книги
def test_add_new_book(collector):
    collector.add_new_book("Новая книга")
    assert "Новая книга" in collector.get_books_genre()
    assert collector.get_books_genre()["Новая книга"] == ''

