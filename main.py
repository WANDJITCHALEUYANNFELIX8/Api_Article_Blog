import requests
import json

BASE_URL = "http://127.0.0.1:5000/api/articles"

def print_response(resp):
    print(f"\nStatus Code: {resp.status_code}")
    try:
        print(json.dumps(resp.json(), indent=4, ensure_ascii=False))
    except:
        print(resp.text)
    print("-" * 50)

def create_article():
    print("\n--- Création d'un article ---")
    id_a = input("ID article: ")
    titre = input("Titre: ")
    contenu = input("Contenu: ")
    auteur = input("Auteur: ")
    date = input("Date (YYYY-MM-DD): ")
    categorie = input("Catégorie: ")
    tags = input("Tags (séparés par des virgules): ")

    article = {
        "id_a": id_a,
        "titre": titre,
        "contenu": contenu,
        "auteur": auteur,
        "date": date,
        "categorie": categorie,
        "tags": tags
    }

    resp = requests.post(BASE_URL, json=article)
    print_response(resp)

def get_all_articles():
    print("\n--- Tous les articles ---")
    resp = requests.get(BASE_URL)
    print_response(resp)

def get_one_article():
    print("\n--- Afficher un article ---")
    id_a = input("ID de l'article: ")
    resp = requests.get(f"{BASE_URL}/{id_a}")
    print_response(resp)

def update_article():
    print("\n--- Mise à jour d'un article ---")
    id_a = input("ID de l'article à modifier: ")
    titre = input("Nouveau titre (laisser vide si pas de changement): ")
    contenu = input("Nouveau contenu: ")
    categorie = input("Nouvelle catégorie: ")
    tags = input("Nouveaux tags: ")

    data = {}
    if titre: data["titre"] = titre
    if contenu: data["contenu"] = contenu
    if categorie: data["categorie"] = categorie
    if tags: data["tags"] = tags

    resp = requests.put(f"{BASE_URL}/{id_a}", json=data)
    print_response(resp)

def delete_article():
    print("\n--- Suppression d'un article ---")
    id_a = input("ID de l'article à supprimer: ")
    resp = requests.delete(f"{BASE_URL}/{id_a}")
    print_response(resp)

def search_article():
    print("\n--- Recherche d'articles ---")
    keyword = input("Mot-clé: ")
    resp = requests.get(f"{BASE_URL}/search?q={keyword}")
    print_response(resp)

def main_menu():
    while True:
        print("""
--- MENU TEST API ---
1. Créer un article
2. Voir tous les articles
3. Voir un article
4. Modifier un article
5. Supprimer un article
6. Rechercher un article
0. Quitter
""")
        choice = input("Choix: ")
        if choice == "1":
            create_article()
        elif choice == "2":
            get_all_articles()
        elif choice == "3":
            get_one_article()
        elif choice == "4":
            update_article()
        elif choice == "5":
            delete_article()
        elif choice == "6":
            search_article()
        elif choice == "0":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Réessayez.")

if __name__ == "__main__":
    main_menu()
