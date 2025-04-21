from enum import Enum

from library.items.article import Article
from library.items.book import Book
from library.items.thesis import Thesis

class ProductType(Enum):
    BOOK = Book
    THESIS = Thesis
    ARTICLE = Article

    def get_display_name(self) -> str:
        display_names = {
            ProductType.BOOK: "Libro",
            ProductType.THESIS: "Tesis",
            ProductType.ARTICLE: "Artículo Cientifico"
        }
        return display_names[self]
