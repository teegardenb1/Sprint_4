import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()

# Тест на добавление книги в избранное, если она уже там есть
def test_add_existing_book_in_favorites(collector):
    collector.add_book_in_favorites("451 по Фаренгейту")
    collector.add_book_in_favorites("451 по Фаренгейту")
    assert collector.get_list_of_favorites_books().count("451 по Фаренгейту") == 1