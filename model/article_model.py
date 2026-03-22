
from database import DatabaseManager

class Article:
    db = DatabaseManager("article.db")

    @classmethod
    def create_table(cls):
        cls.db.create_table("article", "id_a CHAR PRIMARY KEY NOT NULL, titre TEXT NOT NULL, contenu TEXT, auteur TEXT NOT NULL, date DATE, categorie TEXT, tags TEXT")

    @classmethod
    def add(cls, id_a, titre, contenu, auteur, date, categorie, tags):
        cls.db.insert("article", ["id_a", "titre", "contenu", "auteur", "date", "categorie", "tags"], [id_a, titre, contenu, auteur, date, categorie, tags])

    @classmethod
    def get_all(cls):
        return cls.db.select("article")

    @classmethod
    def update(cls, id_a, column, value):
        cls.db.update("article", f"{column} = ?", "id_a = ?", [value, id_a])

    @classmethod
    def delete(cls, id_a):
        cls.db.delete("article", "id_a = ?", [id_a])
    @classmethod
    def get_one(cls, id_a):
        Condition = "id_a = ?"
        result = cls.db.select("article", condition=Condition, values=(id_a,))
        if result:
            return result[0]
        return None
    @classmethod    
    def	search(cls,keyword):
        condition= """
            LOWER(titre) LIKE LOWER(?)
            OR LOWER(contenu) LIKE LOWER(?)
            OR LOWER(categorie) LIKE LOWER(?)
            OR LOWER(tags) LIKE LOWER(?)	        
        """        
        values= (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%", f"%{keyword}%")
        return cls.db.select("article", condition=condition, values=values)




