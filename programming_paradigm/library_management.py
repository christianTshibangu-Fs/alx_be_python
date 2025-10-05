class Book:
    """
    Représente un livre dans la bibliothèque.
    Les attributs privés (_is_checked_out) sont utilisés pour suivre la disponibilité.
    """
    def __init__(self, title, author):
        # Attributs publics
        self.title = title
        self.author = author
        # Attribut privé (convention Python avec underscore)
        self._is_checked_out = False
        
    def check_out(self):
        """Marque le livre comme étant emprunté."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Succès
        return False # Déjà emprunté

    def return_book(self):
        """Marque le livre comme étant disponible."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True # Succès
        return False # Déjà disponible

    def is_available(self):
        """Retourne True si le livre est disponible (non emprunté)."""
        return not self._is_checked_out


class Library:
    """
    Gère une collection d'objets Book.
    """
    def __init__(self):
        # Liste privée pour stocker les instances de Book
        self._books = []

    def add_book(self, book):
        """Ajoute une instance de Book à la collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Recherche et emprunte un livre par son titre."""
        for book in self._books:
            if book.title == title:
                # Appelle la méthode de l'objet Book
                if book.check_out():
                    print(f"'{title}' a été emprunté avec succès.")
                    return True
                else:
                    print(f"Erreur : '{title}' est déjà emprunté.")
                    return False
        print(f"Erreur : Livre '{title}' non trouvé.")
        return False

    def return_book(self, title):
        """Recherche et retourne un livre par son titre."""
        for book in self._books:
            if book.title == title:
                # Appelle la méthode de l'objet Book
                if book.return_book():
                    print(f"'{title}' a été retourné avec succès.")
                    return True
                else:
                    print(f"Erreur : '{title}' n'était pas emprunté.")
                    return False
        print(f"Erreur : Livre '{title}' non trouvé.")
        return False

    def list_available_books(self):
        """Affiche la liste de tous les livres actuellement disponibles."""
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
                available_count += 1
        
        if available_count == 0:
            print("Aucun livre n'est actuellement disponible.")