
from model.article_model import Article
from collections import OrderedDict

class ArticleController:

	@staticmethod
	def validate_article(data):
		required_fields=["id_a","titre","contenu","auteur"]
		
		for field in required_fields:
			if field not in data or not data[field]:
				raise ValueError(f"{field} est obligatoire et ne doit etre absent")
				
		if not isinstance (data["titre"],str):
			raise ValueError("Le titre doit etre une chaine de caractère")		
		
		if not isinstance (data["auteur"],str):
			raise ValueError("L' auteur doit etre une chaine de caractère")

		if not isinstance (data["contenu"],str):
			raise ValueError("Le contenu doit etre une chaine de caractère")
		

	@staticmethod
	def get_all_articles():
		articles=Article.get_all()
		
		result=[]
		for a in articles:
			result.append(OrderedDict([
				("id_a",a[0]),
				("titre",a[1]),
				("contenu",a[2]),
				("auteur",a[3]),
				("date",a[4]),
				("categorie",a[5]),
				("tags",a[6])
			]))
			 
		return result
			           
	@staticmethod
	def get_one_article(id_a):
		a=Article.get_one(id_a)
		
		if a:
			return OrderedDict([
	
				("id_a",a[0]),
				("titre",a[1]),
				("contenu",a[2]),
				("auteur",a[3]),
				("date",a[4]),
				("categorie",a[5]),
				("tags",a[6])
			])
		return None
		
	@staticmethod
	def add_article(data):
	
		ArticleController.validate_article(data)	
		
		if Article.get_one(data["id_a"]):
			raise ValueError("Un article avec cet id existe déjà")
		
		Article.add(
			data["id_a"],
			data["titre"],
			data.get("contenu"),
			data["auteur"],
			data.get("date"),
			data.get("categorie"),
			data.get("tags")
		)
		
		return ArticleController.get_one_article(data["id_a"])
		
	@staticmethod
	def update_article(id_a,data):				
		allowed_fields=["titre","contenu","categorie", "tags"]
		article=Article.get_one(id_a)
		
		if not article:
			return False
		
		for k,value in data.items():
			if k in allowed_fields:
				Article.update(id_a,k,value)
				
		return True						
		
	@staticmethod     
	def delete_article(id_a):
		a=Article.get_one(id_a)
    	
		if a:
			Article.delete(id_a)
			return True
		return False
		
	@staticmethod     
	def search_article(k):	
		results = Article.search(k)
	
		return [
    		OrderedDict([
	
				("id_a",a[0]),
				("titre",a[1]),
				("contenu",a[2]),
				("auteur",a[3]),
				("date",a[4]),
				("categorie",a[5]),
				("tags",a[6])
			])
			for a in results
		]	
    
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
