from __future__ import annotations


class Category:
    """
    Clase que representa una categoría en el sistema de biblioteca.
    Puede tener subcategorías formando una estructura jerárquica.
    """

    # Variable de clase para mantener el contador de IDs
    _next_id = 1
    # Lista para almacenar todas las categorías
    _categories = []

    def __init__(self, name: str, description: str, parent_id: int | None = None):
        self.id = Category._next_id
        Category._next_id += 1
        self.name = name
        self.description = description
        self.parent_id = parent_id
        self.subcategories = []
        Category._categories.append(self)

    def __str__(self) -> str:
        return f"ID={self.id}\n name={self.name}\n description={self.description}\n"

    @classmethod
    def create_category(
        cls, name: str, description: str, parent_id: int | None = None
    ) -> Category:
        category = cls(name, description, parent_id)

        if parent_id:
            parent = cls.get_category_by_id(parent_id)
            if parent:
                parent.subcategories.append(category)

        return category

    @classmethod
    def get_category_by_id(cls, category_id: int) -> Category | None:
        for category in cls._categories:
            if category.id == category_id:
                return category
        return None

    @classmethod
    def get_all_categories(cls) -> list:
        return cls._categories

    def get_subcategories(self) -> list:
        return self.subcategories

    @classmethod
    def patch_category(
        cls, category_id: int, name: str | None = None, description: str | None = None
    ) -> bool:
        category = cls.get_category_by_id(category_id)
        if not category:
            return False

        if name is not None:
            category.name = name
        if description is not None:
            category.description = description

        return True

    @classmethod
    def delete_category(cls, category_id: int) -> bool:
        category = cls.get_category_by_id(category_id)
        if not category:
            return False

        # Primero eliminar de la lista de subcategorías del padre si existe
        if category.parent_id:
            parent = cls.get_category_by_id(category.parent_id)
            if parent:
                parent.subcategories = [
                    sub for sub in parent.subcategories if sub.id != category_id
                ]

        # Luego eliminar de la lista principal
        cls._categories = [cat for cat in cls._categories if cat.id != category_id]
        return True

    def add_subcategory(self, subcategory: Category) -> None:
        self.subcategories.append(subcategory)
