from modele import *
from vue import *

# -------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                           Controleur
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
class Controleur:
	# ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Constructeur du controleur
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
	def __init__(self, modele):
		self.modele = modele
		self.headers = ["Mot", "Nature", "Définition", "Synonyme", "Anglais", "Espagnol", "Italien", "Recherche"]
		self.titres =["Ajouter un mot", "Ajouter", "Supprimer un mot", "Supprimer", "Modifier un mot", "Modifier", "Champ à modifier :", "Modification :","Rechercher un mot contenant", "Caractère(s) :", "Rechercher un mot se terminant"]
	
	# ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Appel du mode par défaut du modele
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
	def defaut(self):
		self.modele.defaut()

	# ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Appel du mode requêteur du modele en lui passant en argument la recherche demandée par l'utilisateur
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
	def requeteur(self, text):
		self.modele.requeteur(text.lower())

	# ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Appel du mode affichage décroissant du modele en lui passant en argument la recherche demandée par l'utilisateur
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
	def affichageDecroissant(self, text):
		self.modele.affichageDecroissant(text.lower())

	# ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Appel du mode ajouter du modele en lui passant en argument le formulaire rempli par l'utilisateur
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
	def ajouter(self, formulaire):
		self.modele.ajouter(formulaire)

	# ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Appel du mode supprimer du modele en lui passant en argument le formulaire rempli par l'utilisateur
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
	def supprimer(self, formulaire):
		self.modele.supprimer(formulaire)

	# ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Appel du mode modifier du modele en lui passant en argument le formulaire rempli par l'utilisateur
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
	def modifier(self, formulaire):
		self.modele.modifier(formulaire)

	# ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Appel du mode "se terminant par" du modele en lui passant en argument le formulaire rempli par l'utilisateur
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
	def terminant(self, formulaire):
		self.modele.terminant(formulaire)

	# ---------------------------------------------------------------------------------------------------------------------------------------------------
    # FRA : Paramétrage de la langue, et des traductions du modèle ainsi que les headers (tableau) et les titres (formulaires) pour la vue
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
	def trad_francais(self):
		self.modele.langue = "Fr"
		self.modele.traduction = ["anglais", "espagnol", "italien"]
		self.headers = ["Mot", "Nature", "Définition", "Synonyme", "Anglais", "Espagnol", "Italien", "Recherche"]
		self.titres =["Ajouter un mot", "Ajouter", "Supprimer un mot", "Supprimer", "Modifier un mot", "Modifier", "Champ à modifier :", "Modification :","Rechercher un mot contenant", "Caractère(s) :", "Rechercher un mot se terminant"]
	
	# ---------------------------------------------------------------------------------------------------------------------------------------------------
    # ANG : Paramétrage de la langue, et des traductions du modèle ainsi que les headers (tableau) et les titres (formulaires) pour la vue
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
	def trad_anglais(self):
		self.modele.langue = "An"
		self.modele.traduction = ["français", "espagnol", "italien"]
		self.headers = ["Word", "Class", "Definition", "Synonymous", "French", "Spanish", "Italian", "Search"]
		self.titres =["Add a word", "Add", "Delete a word", "Delete", "Edit a word", "Edit", "Field to change :", "Change :", "Search for a word including", "Character(s) :", "Search for a word ending"]

	# ---------------------------------------------------------------------------------------------------------------------------------------------------
    # ESP : Paramétrage de la langue et des traductions du modèle, paramétrage des headers (tableau) et les titres (formulaires) pour la vue
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
	def trad_espagnol(self):
		self.modele.langue = "Es"
		self.modele.traduction = ["français", "anglais", "italien"]
		self.headers = ["Palabra", "Tipo", "Definición", "Sinónimo", "Francés", "Inglés", "Italiano", "Buscar"]
		self.titres =["Añadir una palabra", "Añadir", "Eliminar una palabra", "Eliminar", "Cambiar una palabra", "Cambiar", "Campo para cambiar :", "Cambio :", "Buscar una palabra que contiene","Carácter(es) :", "Buscar una palabra que termina"]

	# ---------------------------------------------------------------------------------------------------------------------------------------------------
    # ITA : Paramétrage de la langue, et des traductions du modèle ainsi que les headers (tableau) et les titres (formulaires) pour la vue
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
	def trad_italien(self):
		self.modele.langue = "It"
		self.modele.traduction = ["français", "espagnol", "anglais"]
		self.headers = ["Parola", "Tipo", "Definizione", "Sinonimo", "Francese", "Spagnolo", "Inglese", "Cerca"]
		self.titres =["Aggiungere una parola", "Aggiungere", "Eliminare una parola", "Eliminare", "Modificare una parola", "Modificare", "Campo per cambiare :","Cambiamento :", "Cercare una parola che contiene", "Carattere(i) :", "Cercare una parola che termina"]
