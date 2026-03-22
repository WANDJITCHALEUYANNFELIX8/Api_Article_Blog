
import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        
    def get_connection(self):    #flask est en multi-thread et sqlLite refuse de partager la connexion entre thread alors il faut la regénérer à chaque requete
        return sqlite3.connect(self.db_name)

    def create_table(self, table_name, schema):
        """Créer une table si elle n'existe pas."""
        conn=self.get_connection()
        cur=conn.cursor()
         
        cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({schema})")
        conn.commit()
        conn.close()

    def insert(self, table_name, columns, values):
        """Ajouter une ligne."""
        conn=self.get_connection()
        cur=conn.cursor()
        
        placeholders = ','.join(['?'] * len(values))
        cur.execute(
            f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({placeholders})",
            values
        )
        conn.commit()
        conn.close()

    def update(self, table_name, set_clause, condition, values):
        """Mettre à jour des lignes."""
        
        conn=self.get_connection()
        cur=conn.cursor()
        
        cur.execute(
            f"UPDATE {table_name} SET {set_clause} WHERE {condition}",
            values
        )
        conn.commit()
        conn.close()

    def delete(self, table_name, condition, values):
        """Supprimer des lignes."""
        conn=self.get_connection()
        cur=conn.cursor()
        
        cur.execute(f"DELETE FROM {table_name} WHERE {condition}", values)
        conn.commit()
        conn.close()

    def select(self, table_name, columns='*', condition=None, values=()):
        """Sélectionner des lignes."""
        
        conn=self.get_connection()
        cur=conn.cursor()
        
        query = f"SELECT {columns} FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
            
        cur.execute(query, values)
        results= cur.fetchall()
        conn.close()
        
        return results


