from datetime import date

from library.helpers.error import ErrorManager, ErrorType
from library.items.article import Article
from library.helpers.status import Status
from library.people.author import Author


def main():
    import data

    print("\n=== SISTEMA DE BIBLIOTECA ===")

    # Mostramos los artículos disponibles
    print("\n=== Artículos Disponibles ===")
    for article in Article._articles:
        print(article)


if __name__ == "__main__":
    main()
