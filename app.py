
from flask import Flask, jsonify, request
from flasgger import Swagger
from model.article_model import Article
from controller.article_control import ArticleController


app = Flask(__name__)  # crée une instance de l'application Flask
app.json.sort_keys=False

app.config['SWAGGER'] = {
    "swagger" : "2.0",
    "title": "API de Gestion d'Article de Blog",
    "description": "API simplifiée pour gérer les articles d'un blog",
    "version": "1.0",
    "swagger_ui": True,
    "tags": [
        {
            "name": "Articles",
            "description": "Toutes les opérations sur les articles"
        }
    ],
    "uiversion": 3,
    "defaultModelRendering": "example",
    
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
}
swagger = Swagger(app)


# Gestionnaire d'erreurs global pour les exceptions non prévues
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": "Erreur interne du serveur"}), 500


@app.route('/api/articles', methods=['POST'])
def creer_article():
    """
    Créer un nouvel article
    ---
    summary: "1. Créer un article"
    tags:
      - Articles

    description: >
      Cet endpoint permet de créer un nouvel article dans la base de données.
      L'utilisateur doit fournir les informations sous forme de JSON.

    parameters:
      - name: article
        in: body
        required: true
        description: "Données de l'article à créer"
        schema:
          type: object
          required:
            - id_a
            - titre
            - contenu
            - auteur
          properties:
            id_a:
              type: string
              description: "Identifiant unique de l'article"
              example: "1"
            titre:
              type: string
              description: "Titre de l'article"
              example: "Introduction à Flask"
            contenu:
              type: string
              description: "Contenu principal de l'article"
              example: "Flask est un micro-framework Python..."
            auteur:
              type: string
              description: "Nom de l'auteur"
              example: "Yann"
            date:
              type: string
              description: "Date de publication"
              example: "2026-03-20"
            categorie:
              type: string
              description: "Catégorie de l'article"
              example: "Programmation"
            tags:
              type: string
              description: "Mots-clés associés à l'article"
              example: "Python,Flask,API"

    responses:
      201:
        description: "Article créé avec succès"
        schema:
          type: object
          properties:
            id_a:
              type: string
            titre:
              type: string
            contenu:
              type: string
            auteur:
              type: string
            date:
              type: string
            categorie:
              type: string
            tags:
              type: string
      400:
        description: "Données invalides ou JSON manquant"
      409:
        description: "Conflit : identifiant déjà existant"
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "Json invalide"}), 400

    try:
        article = ArticleController.add_article(data)
        return jsonify(article), 201
    except ValueError as e:
        # 409 Conflict : l'id existe déjà (erreur client, pas serveur)
        return jsonify({"error": str(e)}), 409


@app.route('/api/articles', methods=['GET'])
def afficher_tous_articles():
    """
    Récupère tous les articles
    ---

    summary: "2. Récupérer tous les articles"
    tags:
      - Articles
    responses:
      200:
        description: Liste de tous les articles
        schema:
          type: array
          items:
            type: object
            properties:
              id_a:
                type: string
              titre:
                type: string
              contenu:
                type: string
              auteur:
                type: string
              date:
                type: string
              categorie:
                type: string
              tags:
                type: string
        examples:
          application/json:
            - id_a: "2"
              titre: "java"
              contenu: "Apprendre java"
              auteur: "Yann"
              date: "2026-03-20"
              categorie: "programmation"
              tags: "python,flask,API"
    """
    articles = ArticleController.get_all_articles()
    return jsonify(articles), 200

@app.route('/api/articles/search', methods=['GET'])
def rechercher_article():
    """
    Rechercher des articles par mot-clé
    ---

    summary: "6. Rechercher des articles"
    tags:
      - Articles
    description: >
      Cet endpoint permet de rechercher des articles contenant un mot-clé dans le titre,
      le contenu, la catégorie ou les tags.

    parameters:
      - name: q
        in: query
        type: string
        required: true
        description: Mot-clé à rechercher
        example: "Flask"

    responses:
      200:
        description: >
          Liste des articles correspondant au mot-clé
        schema:
          type: array
          items:
            type: object
            properties:
              id_a:
                type: string
              titre:
                type: string
              contenu:
                type: string
              auteur:
                type: string
              date:
                type: string
              categorie:
                type: string
              tags:
                type: string
      400:
        description: >
          Mot-clé requis
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Mot-clé requis"
    """
    k = request.args.get("q")

    if not k:
        return jsonify({"error": "Mot-clé requis"}), 400

    results = ArticleController.search_article(k)
    return jsonify(results), 200


@app.route('/api/articles/<id_a>', methods=['GET'])
def afficher_un_article(id_a):
    """
    Récupérer un article par son identifiant
    ---

    summary: "3. Récupérer un article"
    tags:
      - Articles

    description: >
      Cet endpoint permet de récupérer un article spécifique à partir de son identifiant unique (id_a).

    parameters:
      - name: id_a
        in: path
        type: string
        required: true
        description: Identifiant unique de l'article
        example: "1"

    responses:
      200:
        description: Article trouvé avec succès
        schema:
          type: object
          properties:
            id_a:
              type: string
            titre:
              type: string
            contenu:
              type: string
            auteur:
              type: string
            date:
              type: string
            categorie:
              type: string
            tags:
              type: string
      404:
        description: >
          Article non trouvé pour cet identifiant
    """
    article = ArticleController.get_one_article(id_a)
    if article:
        return jsonify(article), 200
    return jsonify({"error": "Article non trouvé"}), 404


@app.route('/api/articles/<id_a>', methods=['PUT'])
def modifier_article(id_a):
    """
    Modifier un article existant
    ---

    summary: "4. Modifier un article"
    tags:
      - Articles

    description: >
      Cet endpoint permet de modifier les informations d'un article existant.
      Seuls certains champs peuvent être modifiés (titre, contenu, categorie, tags).

    parameters:
      - name: id_a
        in: path
        type: string
        required: true
        description: Identifiant unique de l'article à modifier
        example: "1"

      - name: body
        in: body
        required: true
        description: Données à mettre à jour
        schema:
          type: object
          properties:
            titre:
              type: string
              description: Nouveau titre de l'article
              example: "Titre modifié"
            contenu:
              type: string
              description: Nouveau contenu
              example: "Contenu mis à jour"
            categorie:
              type: string
              description: Nouvelle catégorie
              example: "Informatique"
            tags:
              type: string
              description: Nouveaux tags
              example: "Python,API"

    responses:
      200:
        description: Article mis à jour avec succès
      404:
        description: Article non trouvé
      400:
        description: Données invalides
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "Json invalide"}), 400

    updated = ArticleController.update_article(id_a, data)
    if updated:
        return jsonify({"message": "Article mis à jour"}), 200
    return jsonify({"error": "Article non trouvé"}), 404


@app.route('/api/articles/<id_a>', methods=['DELETE'])
def supprimer_article(id_a):
    """
    Supprimer un article existant
    ---

    summary: "5. Supprimer un article"
    tags:
      - Articles
    description: >
      Cet endpoint permet de supprimer un article spécifique à partir de son identifiant unique (id_a).

    parameters:
      - name: id_a
        in: path
        type: string
        required: true
        description: Identifiant unique de l'article à supprimer
        example: "2"

    responses:
      200:
        description: >
          Article supprimé avec succès
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Article supprimé"
      404:
        description: >
          Article non trouvé pour cet identifiant
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Article non trouvé"
    """
    article = ArticleController.delete_article(id_a)
    if article:
        return jsonify({"message": "Article supprimé"}), 200
    return jsonify({"error": "Article non trouvé"}), 404


if __name__ == "__main__":
    Article.create_table()
    
    #debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug= True)
    
    
    
    
    
