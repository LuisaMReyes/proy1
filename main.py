from library.helpers.error import ErrorManager, ErrorType
from library.items.article import Article
from datetime import date
from library.helpers.status import Status
from library.people.author import Author


def main():
    # Crear un autor de ejemplo
    # Creamos a Ada Lovelace
    Author.create(
        author_id="AL123",
        name="Ada Lovelace",
        nationality="Británica",
        birth_date=date(1815, 12, 10),
    )

    # Creamos a Grace Hopper
    Author.create(
        author_id="GH456",
        name="Grace Hopper",
        nationality="Estadounidense",
        birth_date=date(1906, 12, 9),
    )

    if not Author.patch_author("GH456", name="Grace Murray Hopper"):
        ErrorManager(ErrorType.AUTHOR_NOT_FOUND)
        return

    # Creamos a Alan Turing
    Author.create(
        author_id="AT789",
        name="Alan Turing",
        nationality="Británico",
        birth_date=date(1912, 6, 23),
    )

    # Recuperamos los autores
    author1 = Author.get_author_by_id("AL123")
    author2 = Author.get_author_by_id("GH456")
    author3 = Author.get_author_by_id("AT789")

    # Verificamos que todos los autores existan
    if None in (author1, author2, author3):
        ErrorManager(ErrorType.AUTHOR_NOT_FOUND)
        return

    # Como ya verificamos que ninguno es None, podemos hacer el cast seguro
    authors: list[Author] = [author1, author2, author3]  # type: ignore

    # Crear un artículo de ejemplo
    articulo_ejemplo = Article(
        title="La Programación Orientada a Objetos en Python",
        doi="10.1234/poo.2025.123",
        authors=authors,
        publisher_name="Editorial Tech",
        publication_date=date(2025, 4, 17),
        journal="Revista de Ciencias de la Computación",
        periodicity="Mensual",
        volume="Vol. 3",
        field="Ciencias de la Computación",
        status=Status.AVAILABLE,
    )

    print(articulo_ejemplo)


if __name__ == "__main__":
    main()
