# 📘 API de Gestion d'Articles de Blog

## 📖 Description

Cette API REST permet de gérer des articles de blog de manière simple et efficace.
Elle permet de créer, lire, modifier, supprimer et rechercher des articles.

Le projet est développé en **Python avec Flask** et utilise **SQLite** comme base de données.

---

## 🚀 Fonctionnalités

* ✅ Création d’un article
* 📄 Récupération de tous les articles
* 🔍 Recherche d’articles par mot-clé
* 📌 Récupération d’un article spécifique
* ✏️ Modification d’un article
* ❌ Suppression d’un article
* 📚 Documentation interactive avec Swagger

---

## 🛠️ Technologies utilisées

* Python 3
* Flask
* SQLite
* Flasgger (Swagger UI)

---

## ⚙️ Installation

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/ton-username/api_backend.git
cd api_backend
```

---

### 2️⃣ Créer un environnement virtuel (recommandé)

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

---

### 3️⃣ Installer les dépendances

```bash
pip install flask flasgger
```

---

### 4️⃣ Lancer le serveur

```bash
python app.py
```

---

### 5️⃣ Accéder à l’API

* API :

```
http://127.0.0.1:5000
```

* Documentation Swagger :

```
http://127.0.0.1:5000/apidocs
```

---

## 📡 Endpoints disponibles

### ➤ 🔹 Créer un article

**POST** `/api/articles`

#### Body JSON :

```json
{
  "id_a": "1",
  "titre": "Introduction à Flask",
  "contenu": "Flask est un micro-framework Python...",
  "auteur": "Yann",
  "date": "2026-03-20",
  "categorie": "Programmation",
  "tags": "Python,Flask,API"
}
```

---

### ➤ 🔹 Récupérer tous les articles

**GET** `/api/articles`

👉 Avec pagination :

```
/api/articles?page=1&limit=10
```

---

### ➤ 🔹 Récupérer un article

**GET** `/api/articles/<id_a>`

Exemple :

```
/api/articles/1
```

---

### ➤ 🔹 Modifier un article

**PUT** `/api/articles/<id_a>`

#### Body JSON :

```json
{
  "titre": "Nouveau titre",
  "contenu": "Contenu mis à jour"
}
```

---

### ➤ 🔹 Supprimer un article

**DELETE** `/api/articles/<id_a>`

---

### ➤ 🔹 Rechercher des articles

**GET** `/api/articles/search?q=mot_cle`

Exemple :

```
/api/articles/search?q=flask
```

---

## 🧪 Exemples d’utilisation

### Avec Python (requests)

```python
import requests

url = "http://127.0.0.1:5000/api/articles"

data = {
    "id_a": "2",
    "titre": "Flask API",
    "contenu": "Créer une API REST",
    "auteur": "Yann"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
```

---

## ⚠️ Gestion des erreurs

| Code | Description                |
| ---- | -------------------------- |
| 200  | Succès                     |
| 201  | Ressource créée            |
| 400  | Requête invalide           |
| 404  | Ressource non trouvée      |
| 409  | Conflit (ID déjà existant) |
| 500  | Erreur interne             |

---

## 📌 Structure du projet

```
api_backend/
│
├── app.py
├── database.py
├── model/
│   └── article_model.py
├── controller/
│   └── article_control.py
└── README.md
```

---

## 🔒 Sécurité

* Utilisation de requêtes paramétrées → protection contre les injections SQL
* Validation des données côté serveur

---

## ✨ Améliorations futures

* Authentification (JWT)
* Pagination avancée
* Upload d’images
* Déploiement en ligne

---

## 👨‍💻 Auteur

Projet réalisé par **Yann Wandji** dans le cadre d’un apprentissage du développement backend avec Flask.

---

## 📄 Licence

Ce projet est libre d’utilisation à des fins éducatives.
