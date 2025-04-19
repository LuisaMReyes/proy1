from enum import Enum

from library.items.article import Article
from library.items.book import Book
from library.items.thesis import Thesis

class ProductType(Enum):
    BOOK = Book
    THESIS = Thesis
    ARTICLE = Article

