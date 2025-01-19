import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


# Тестирование на возрастной ценз у детей
def test_get_books_for_children(collector):
    books_for_children = collector.get_books_for_children()
    assert "451 по Фаренгейту" in books_for_children
    assert "1984" in books_for_children
    assert "Маленький принц" in books_for_children
    assert "Гарри Поттер и Философский камень" in books_for_children
    assert "Зелёная миля" not in books_for_children