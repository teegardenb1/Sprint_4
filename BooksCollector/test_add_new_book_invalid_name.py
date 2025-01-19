import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()

#Тест на невалидное имяэ
def test_add_new_book_invalid_name(collector):
    collector.add_new_book("A"*41)
    collector.add_new_book("")
    assert "A"*41 not in collector.books_genre
    assert "" not in collector.books_genre