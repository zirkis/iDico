import sqlite3

# -------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                           Modele
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
class Modele:
	# ---------------------------------------------------------------------------------------------------------------------------------------------------
	# Constructeur du modèle
	# ---------------------------------------------------------------------------------------------------------------------------------------------------
	def __init__(self):
		self.conn = sqlite3.connect('ma_base.db')
		self.cursor = self.conn.cursor()
		self.langue = "Fr"
		self.traduction = ["anglais", "espagnol", "italien"]
		self.defaut()

	# ---------------------------------------------------------------------------------------------------------------------------------------------------
	# Affichage par défaut de la table contenant la langue sélectionnée
	# ---------------------------------------------------------------------------------------------------------------------------------------------------
	def defaut(self):
		self.req = self.cursor.execute("""SELECT * FROM dico{} ORDER BY nom ASC""".format(self.langue)).fetchall()		
		self.reqNom = self.cursor.execute("""SELECT nom FROM dico{} ORDER BY nom ASC""".format(self.langue)).fetchall()
		self.reqNat = self.cursor.execute("""SELECT nature FROM dico{} ORDER BY nom ASC""".format(self.langue)).fetchall()
		self.reqDef = self.cursor.execute("""SELECT definition FROM dico{} ORDER BY nom ASC""".format(self.langue)).fetchall()
		self.reqSyn = self.cursor.execute("""SELECT synonyme FROM dico{} ORDER BY nom ASC""".format(self.langue)).fetchall()
		self.reqLang1 = self.cursor.execute("""SELECT {} FROM dico{} ORDER BY nom ASC""".format(self.traduction[0],self.langue)).fetchall()
		self.reqLang2 = self.cursor.execute("""SELECT {} FROM dico{} ORDER BY nom ASC""".format(self.traduction[1],self.langue)).fetchall()
		self.reqLang3 = self.cursor.execute("""SELECT {} FROM dico{} ORDER BY nom ASC""".format(self.traduction[2],self.langue)).fetchall()

	# ---------------------------------------------------------------------------------------------------------------------------------------------------
	# Affichage des résultats en fonction d'une recherche dans l'ordre alphabétique
	# ---------------------------------------------------------------------------------------------------------------------------------------------------
	def requeteur(self, recherche):
		self.req = self.cursor.execute("""SELECT * FROM dico{} WHERE nom LIKE "{}%" ORDER BY nom ASC""".format(self.langue,recherche)).fetchall()
		self.reqNom = self.cursor.execute("""SELECT nom FROM dico{} WHERE nom LIKE "{}%" ORDER BY nom ASC""".format(self.langue,recherche)).fetchall()
		self.reqNat = self.cursor.execute("""SELECT nature FROM dico{} WHERE nom LIKE "{}%" ORDER BY nom ASC""".format(self.langue,recherche)).fetchall()
		self.reqDef = self.cursor.execute("""SELECT definition FROM dico{} WHERE nom LIKE "{}%" ORDER BY nom ASC""".format(self.langue,recherche)).fetchall()
		self.reqSyn = self.cursor.execute("""SELECT synonyme FROM dico{} WHERE nom LIKE "{}%" ORDER BY nom ASC""".format(self.langue,recherche)).fetchall()
		self.reqLang1 = self.cursor.execute("""SELECT {} FROM dico{} WHERE nom LIKE "{}%" ORDER BY nom ASC""".format(self.traduction[0],self.langue,recherche)).fetchall()
		self.reqLang2 = self.cursor.execute("""SELECT {} FROM dico{} WHERE nom LIKE "{}%" ORDER BY nom ASC""".format(self.traduction[1],self.langue,recherche)).fetchall()
		self.reqLang3 = self.cursor.execute("""SELECT {} FROM dico{} WHERE nom LIKE "{}%" ORDER BY nom ASC""".format(self.traduction[2],self.langue,recherche)).fetchall()
	
	# ---------------------------------------------------------------------------------------------------------------------------------------------------
	# Affichage des résultats en fonction d'une recherche dans l'ordre alphabétique inverse
	# ---------------------------------------------------------------------------------------------------------------------------------------------------
	def affichageDecroissant(self, recherche):
		self.req = self.cursor.execute("""SELECT * FROM dico{} WHERE nom LIKE "{}%" ORDER BY nom DESC""".format(self.langue,recherche)).fetchall()
		self.reqNom = self.cursor.execute("""SELECT nom FROM dico{} WHERE nom LIKE "{}%" ORDER BY nom DESC""".format(self.langue,recherche)).fetchall()
		self.reqNat = self.cursor.execute("""SELECT nature FROM dico{} WHERE nom LIKE "{}%" ORDER BY nom DESC""".format(self.langue,recherche)).fetchall()
		self.reqDef = self.cursor.execute("""SELECT definition FROM dico{} WHERE nom LIKE "{}%" ORDER BY nom DESC""".format(self.langue,recherche)).fetchall()
		self.reqSyn = self.cursor.execute("""SELECT synonyme FROM dico{} WHERE nom LIKE "{}%" ORDER BY nom DESC""".format(self.langue,recherche)).fetchall()
		self.reqLang1 = self.cursor.execute("""SELECT {} FROM dico{} WHERE nom LIKE "{}%" ORDER BY nom DESC""".format(self.traduction[0],self.langue,recherche)).fetchall()
		self.reqLang2 = self.cursor.execute("""SELECT {} FROM dico{} WHERE nom LIKE "{}%" ORDER BY nom DESC""".format(self.traduction[1],self.langue,recherche)).fetchall()
		self.reqLang3 = self.cursor.execute("""SELECT {} FROM dico{} WHERE nom LIKE "{}%" ORDER BY nom DESC""".format(self.traduction[2],self.langue,recherche)).fetchall()

	# ---------------------------------------------------------------------------------------------------------------------------------------------------
	# Ajout d'une entrée à BDD via un formulaire, et retour à l'affichage par défaut
	# ---------------------------------------------------------------------------------------------------------------------------------------------------
	def ajouter(self, formulaire):
		self.reqAjouter = self.cursor.execute("""INSERT INTO dico{}(nom, nature, definition, synonyme, {}, {}, {})
			VALUES(?, ?, ?, ?, ?, ?, ?)""".format(self.langue, self.traduction[0], self.traduction[1], self.traduction[2],), ("{}".format(formulaire[0]), "{}".format(formulaire[1]), "{}".format(formulaire[2]), 
			"{}".format(formulaire[3]), "{}".format(formulaire[4]), "{}".format(formulaire[5]), "{}".format(formulaire[6])))
		self.conn.commit()
		self.defaut()

	# ---------------------------------------------------------------------------------------------------------------------------------------------------
	# Suppression d'une entrée de la BDD via un formulaire, et retour à l'affichage par défaut
	# ---------------------------------------------------------------------------------------------------------------------------------------------------
	def supprimer(self, formulaire):
		self.reqSupprimer = self.cursor.execute("""DELETE FROM dico{} WHERE nom = "{}" """.format(self.langue, formulaire))
		self.conn.commit()
		self.defaut()

	# ---------------------------------------------------------------------------------------------------------------------------------------------------
	# Modification d'une entrée de la BDD via un formulaire, et retour à l'affichage par défaut
	# ---------------------------------------------------------------------------------------------------------------------------------------------------
	def modifier(self, formulaire):
		self.reqModifier = self.cursor.execute("""UPDATE dico{} SET {} = ? WHERE nom = "{}" """.format(self.langue, formulaire[0],formulaire[1]),("{}".format(formulaire[2]),))
		self.conn.commit()
		self.defaut()
	
	# ---------------------------------------------------------------------------------------------------------------------------------------------------
	# Affichage les mots se terminant par une chaine de caractères
	# ---------------------------------------------------------------------------------------------------------------------------------------------------
	def terminant(self, recherche):
		self.req = self.cursor.execute("""SELECT * FROM dico{} WHERE nom LIKE "%{}" ORDER BY nom ASC""".format(self.langue,recherche)).fetchall()
		self.reqNom = self.cursor.execute("""SELECT nom FROM dico{} WHERE nom LIKE "%{}" ORDER BY nom ASC""".format(self.langue,recherche)).fetchall()
		self.reqNat = self.cursor.execute("""SELECT nature FROM dico{} WHERE nom LIKE "%{}" ORDER BY nom ASC""".format(self.langue,recherche)).fetchall()
		self.reqDef = self.cursor.execute("""SELECT definition FROM dico{} WHERE nom LIKE "%{}" ORDER BY nom ASC""".format(self.langue,recherche)).fetchall()
		self.reqSyn = self.cursor.execute("""SELECT synonyme FROM dico{} WHERE nom LIKE "%{}" ORDER BY nom ASC""".format(self.langue,recherche)).fetchall()
		self.reqLang1 = self.cursor.execute("""SELECT {} FROM dico{} WHERE nom LIKE "%{}" ORDER BY nom ASC""".format(self.traduction[0],self.langue,recherche)).fetchall()
		self.reqLang2 = self.cursor.execute("""SELECT {} FROM dico{} WHERE nom LIKE "%{}" ORDER BY nom ASC""".format(self.traduction[1],self.langue,recherche)).fetchall()
		self.reqLang3 = self.cursor.execute("""SELECT {} FROM dico{} WHERE nom LIKE "%{}" ORDER BY nom ASC""".format(self.traduction[2],self.langue,recherche)).fetchall()


# -------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                           SQLite
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# Création de table :
# -------------------
# con = sqlite3.connect('ma_base.db')
# cursore = con.cursor()
# cursore.execute("""CREATE TABLE IF NOT EXISTS dicoIt(
#      id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
#      nom TEXT,
#      nature TEXT,
#      definition TEXT,
#      synonyme TEXT,
#      français TEXT,
# 	 anglais TEXT,
# 	 espagnol TEXT)""")
# con.commit()

# Ajouter une entrée à la table :
# -----------------------------
# con = sqlite3.connect('ma_base.db')
# cursore = con.cursor()
# test = cursore.execute("""
# INSERT INTO dicoFr(nom, legme, definition, synonyme, anglais, espagnol, italien)
#  VALUES(?, ?, ?, ?, ?, ?, ?)""", ("question", "nom", "Demande faite pour obtenir une information, vérifier des connaissances",
#  	"interrogation", "question", "pregunta", "questione"))
# con.commit()

# Supprimer une entrée de la table :
# -------------------------------
# con = sqlite3.connect('ma_base.db')
# cursore = con.cursor()
# test = cursore.execute("""
# DELETE FROM dicoFr WHERE nom ="<PyQt5.QtWidgets.QLineEdit object at 0x104de05e8>" """)
# con.commit()

# Modifier une entrée de la table :
# -------------------------------
# con = sqlite3.connect('ma_base.db')
# cursore = con.cursor()
# test = cursore.execute("""UPDATE dictionnaire SET esp = ? WHERE nom = "Bonjour" """, ("Hola",))
# con.commit()

# Ajouter une colonne à la table :
# ---------------------------------
# con = sqlite3.connect('ma_base.db')
# cursore = con.cursor()
# test = cursore.execute("""ALTER TABLE dicoFr ADD COLUMN nature TEXT""")
# con.commit()