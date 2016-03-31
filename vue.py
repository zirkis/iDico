import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from modele import *
from controleur import *

# -------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                           Vue
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
class vue(QMainWindow):
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Constructeur de la vue
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        # Initialisation de la fenêtre principale
        QMainWindow.__init__(self)

        # Instanciation du modèle et du controleur
        self.modele = Modele()
        self.controleur = Controleur(self.modele)
        
        # Déclaration du layout et de la zone centrale de la fenêtre principale
        self.layoutFenetrePrincipale = QGridLayout()
        self.layoutFenetrePrincipale.setVerticalSpacing(10)
        self.zoneCentrale = QWidget()

        # Déclaration, paramétrage, définition des signaux/slots et insertion dans le layout de la zone de recherche 
        self.recherche = QLineEdit()
        self.recherche.setPlaceholderText(self.controleur.headers[7].capitalize() + "...")
        self.recherche.textChanged.connect(self.controleur.requeteur)
        self.recherche.textChanged.connect(self.dessin)
        self.layoutFenetrePrincipale.addWidget(self.recherche,0,0,1,21)

        # Appel de la fonction de dessin de la vue de la base de données
        self.dessin()

        # Déclaration des tailles utilisées pour les boutons et leurs icones
        self.tailleBouton = QSize(10,30)
        self.tailleIcon = QSize(10,20)
        self.tailleDrapeau = QSize(80,80)

        # Bouton "ajouter une entrée"
        self.boutonAjouter = QPushButton()
        self.boutonAjouter.setMinimumSize(self.tailleBouton)
        self.boutonAjouter.setIcon(QIcon("img/add.png"))
        self.boutonAjouter.setIconSize(self.tailleIcon)
        self.boutonAjouter.clicked.connect(self.ajouter)
        self.layoutFenetrePrincipale.addWidget(self.boutonAjouter,0,21)

        # Bouton "supprimer une entrée"
        self.boutonSupprimer = QPushButton()
        self.boutonSupprimer.setMinimumSize(self.tailleBouton)
        self.boutonSupprimer.setIcon(QIcon("img/remove.png"))
        self.boutonSupprimer.setIconSize(self.tailleIcon)
        self.boutonSupprimer.clicked.connect(self.supprimer) 
        self.layoutFenetrePrincipale.addWidget(self.boutonSupprimer,0,22)

        # Bouton "modifier une entrée"
        self.boutonModifier = QPushButton()
        self.boutonModifier.setMinimumSize(self.tailleBouton)
        self.boutonModifier.setIcon(QIcon("img/edit.png"))
        self.boutonModifier.setIconSize(self.tailleIcon)
        self.boutonModifier.clicked.connect(self.modifier) 
        self.layoutFenetrePrincipale.addWidget(self.boutonModifier,0,23)

        # Bouton "afficher dans l'ordre croissant"
        self.boutonCroissant = QPushButton()
        self.boutonCroissant.setMinimumSize(self.tailleBouton)
        self.boutonCroissant.setIcon(QIcon("img/asc.png"))
        self.boutonCroissant.setIconSize(self.tailleIcon)
        self.boutonCroissant.clicked.connect(self.affichageCroissant)
        self.boutonCroissant.clicked.connect(self.dessin)
        self.layoutFenetrePrincipale.addWidget(self.boutonCroissant,0,24)

        # Bouton "afficher dans l'ordre décroissant"
        self.boutonDecroissant = QPushButton()
        self.boutonDecroissant.setMinimumSize(self.tailleBouton)
        self.boutonDecroissant.setIcon(QIcon("img/des.png"))
        self.boutonDecroissant.setIconSize(self.tailleIcon)
        self.boutonDecroissant.clicked.connect(self.affichageDecroissant)
        self.boutonDecroissant.clicked.connect(self.dessin)
        self.layoutFenetrePrincipale.addWidget(self.boutonDecroissant,0,25)

        # Bouton "rechercher un mot contenant une chaine de caractère(s)"
        self.boutonRechCont = QPushButton()
        self.boutonRechCont.setMinimumSize(self.tailleBouton)
        self.boutonRechCont.setIcon(QIcon("img/middle.png"))
        self.boutonRechCont.setIconSize(self.tailleIcon)
        self.boutonRechCont.clicked.connect(self.affichageContenant)
        self.boutonRechCont.clicked.connect(self.dessin)
        self.layoutFenetrePrincipale.addWidget(self.boutonRechCont,0,26)

        # Bouton "rechercher un mot se terminant par une chaine de caractère(s)"
        self.boutonRechTerm = QPushButton()
        self.boutonRechTerm.setMinimumSize(self.tailleBouton)
        self.boutonRechTerm.setIcon(QIcon("img/end.png"))
        self.boutonRechTerm.setIconSize(self.tailleIcon)
        self.boutonRechTerm.clicked.connect(self.affichageTerminant)
        self.boutonRechTerm.clicked.connect(self.dessin)
        self.layoutFenetrePrincipale.addWidget(self.boutonRechTerm,0,27)

        # Bouton chat
        self.boutonRechTerm = QPushButton()
        self.boutonRechTerm.setMinimumSize(self.tailleBouton)
        self.boutonRechTerm.setIcon(QIcon("img/chat.png"))
        self.boutonRechTerm.setIconSize(self.tailleIcon)
        self.numeroPhoto = -1
        self.boutonRechTerm.clicked.connect(self.chat)
        self.layoutFenetrePrincipale.addWidget(self.boutonRechTerm,0,28)

        # Bouton mode d'emploi
        self.boutonRechTerm = QPushButton()
        self.boutonRechTerm.setMinimumSize(self.tailleBouton)
        self.boutonRechTerm.setIcon(QIcon("img/manual.png"))
        self.boutonRechTerm.setIconSize(self.tailleIcon)
        self.boutonRechTerm.clicked.connect(self.info)
        self.layoutFenetrePrincipale.addWidget(self.boutonRechTerm,0,29)

        # Drapeau FR
        self.boutonFr = QPushButton()
        self.boutonFr.setIcon(QIcon("img/France.png"))
        self.boutonFr.setIconSize(self.tailleDrapeau)
        self.boutonFr.setCheckable(True)
        self.boutonFr.setChecked(True)
        self.boutonFr.clicked.connect(self.controleur.trad_francais)
        self.boutonFr.clicked.connect(self.controleur.defaut)
        self.boutonFr.clicked.connect(self.dessin)
        self.boutonFr.clicked.connect(self.checker)
        self.layoutFenetrePrincipale.addWidget(self.boutonFr,1,36)
        # Drapeau GB
        self.boutonGb = QPushButton()
        self.boutonGb.setIcon(QIcon("img/United-Kingdom.png"))
        self.boutonGb.setIconSize(self.tailleDrapeau)
        self.boutonGb.setCheckable(True)
        self.boutonGb.clicked.connect(self.controleur.trad_anglais)
        self.boutonGb.clicked.connect(self.controleur.defaut)
        self.boutonGb.clicked.connect(self.dessin)       
        self.layoutFenetrePrincipale.addWidget(self.boutonGb,2,36)
        # Drapeau ES
        self.boutonEs = QPushButton()
        self.boutonEs.setIcon(QIcon("img/Spain.png"))
        self.boutonEs.setIconSize(self.tailleDrapeau)
        self.boutonEs.setCheckable(True)
        self.boutonEs.clicked.connect(self.controleur.trad_espagnol)
        self.boutonEs.clicked.connect(self.controleur.defaut)
        self.boutonEs.clicked.connect(self.dessin)
        self.layoutFenetrePrincipale.addWidget(self.boutonEs,3,36)
        # Drapeau IT
        self.boutonIt = QPushButton()
        self.boutonIt.setIcon(QIcon("img/Italy.png"))
        self.boutonIt.setIconSize(self.tailleDrapeau)
        self.boutonIt.setCheckable(True)
        self.boutonIt.clicked.connect(self.controleur.trad_italien)
        self.boutonIt.clicked.connect(self.controleur.defaut)
        self.boutonIt.clicked.connect(self.dessin)
        self.layoutFenetrePrincipale.addWidget(self.boutonIt,4,36)
        # Groupe de boutons afin de récupérer l'information concernant le drapeau sélectionné
        self.groupeDrapeaux = QButtonGroup()
        self.groupeDrapeaux.addButton(self.boutonFr)
        self.groupeDrapeaux.addButton(self.boutonGb)
        self.groupeDrapeaux.addButton(self.boutonEs)
        self.groupeDrapeaux.addButton(self.boutonIt)

        # Paramètrage du layout, et de la zone centrale
        self.zoneCentrale.setLayout(self.layoutFenetrePrincipale)
        self.setCentralWidget(self.zoneCentrale)

        # Donne le focus à la barre de recherche
        self.recherche.setFocus()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Fonction de dessin de la vue
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    def dessin(self):
        # Rafrachissement de l'indication texte de la barre de recherche en fonction de la langue
        self.recherche.setPlaceholderText(self.controleur.headers[7].capitalize() + "...")
        # Déclaration du tableau contenant les données de la BDD
        self.tableau = QTableWidget(len(self.modele.req), 7)

        # Déclaration des headers horizontaux du tableau
        self.tableau.setHorizontalHeaderItem(0, QTableWidgetItem(self.controleur.headers[0]))
        self.tableau.setHorizontalHeaderItem(1, QTableWidgetItem(self.controleur.headers[1]))
        self.tableau.setHorizontalHeaderItem(2, QTableWidgetItem(self.controleur.headers[2]))
        self.tableau.setHorizontalHeaderItem(3, QTableWidgetItem(self.controleur.headers[3]))
        self.tableau.setHorizontalHeaderItem(4, QTableWidgetItem(self.controleur.headers[4]))
        self.tableau.setHorizontalHeaderItem(5, QTableWidgetItem(self.controleur.headers[5]))
        self.tableau.setHorizontalHeaderItem(6, QTableWidgetItem(self.controleur.headers[6]))

        # Déclaration des cases du tableau
        for i in range(len(self.modele.req)):
            # Remplissage des cases du tableau grâce aux requêtes du modèle vers la BDD (avec mise en forme des résultats)
            self.colonne1 = QTableWidgetItem(str(self.modele.reqNom[i])[2:-3].capitalize())
            self.colonne2 = QTableWidgetItem(str(self.modele.reqNat[i])[2:-3].capitalize())
            self.colonne3 = QTableWidgetItem(str(self.modele.reqDef[i])[2:-3].capitalize())
            self.colonne4 = QTableWidgetItem(str(self.modele.reqSyn[i])[2:-3].capitalize())
            self.colonne5 = QTableWidgetItem(str(self.modele.reqLang1[i])[2:-3].capitalize())
            self.colonne6 = QTableWidgetItem(str(self.modele.reqLang2[i])[2:-3].capitalize())
            self.colonne7 = QTableWidgetItem(str(self.modele.reqLang3[i])[2:-3].capitalize())
            # Suppression de la possibilité d'édition des cases du tableau
            self.colonne1.setFlags(self.colonne1.flags() & ~Qt.ItemIsEditable)
            self.colonne2.setFlags(self.colonne2.flags() & ~Qt.ItemIsEditable)
            self.colonne3.setFlags(self.colonne3.flags() & ~Qt.ItemIsEditable)
            self.colonne4.setFlags(self.colonne4.flags() & ~Qt.ItemIsEditable)
            self.colonne5.setFlags(self.colonne5.flags() & ~Qt.ItemIsEditable)
            self.colonne6.setFlags(self.colonne6.flags() & ~Qt.ItemIsEditable)
            self.colonne7.setFlags(self.colonne7.flags() & ~Qt.ItemIsEditable)
            # Insertion des cases dans le tableau
            self.tableau.setItem(i,0,self.colonne1)
            self.tableau.setItem(i,1,self.colonne2)
            self.tableau.setItem(i,2,self.colonne3)
            self.tableau.setItem(i,3,self.colonne4)
            self.tableau.setItem(i,4,self.colonne5)
            self.tableau.setItem(i,5,self.colonne6)
            self.tableau.setItem(i,6,self.colonne7)

        # Déclaration de la largeur des colonnes du tableau
        self.tableau.setColumnWidth(0,100)
        self.tableau.setColumnWidth(1,70)
        self.tableau.setColumnWidth(2,250)
        self.tableau.setColumnWidth(3,110)
        self.tableau.setColumnWidth(4,90)
        self.tableau.setColumnWidth(5,90)
        self.tableau.setColumnWidth(6,90)

        # Ajustement de la hauteur des lignes du tableau en fonction de leur contenu
        self.tableau.resizeRowsToContents()

        # Ajout du tableau dans le layout
        self.layoutFenetrePrincipale.addWidget(self.tableau,1,0,4,35)

    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Fonction d'ajout d'un nouveau mot via un formulaire
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    def ajouter(self):
        # Déclaration et paramétrage du widget accueillant le formulaire
        self.formulaireAjout = QWidget()
        self.formulaireAjout.setWindowTitle(self.controleur.titres[0])
        self.formulaireAjout.resize(500,200)

        # Déclaration du layout du formulaire
        self.layoutAjout = QGridLayout()

        # Déclaration des labels ainsi que des champs du formulaire
        self.labelMot = QLabel(self.controleur.headers[0] + " :")
        self.inputMot = QLineEdit()
        self.labelNature = QLabel(self.controleur.headers[1] + " :")
        self.inputNature = QLineEdit()
        self.labelDefinition = QLabel(self.controleur.headers[2] + " :")
        self.inputDefinition = QLineEdit()
        self.labelSynonyme = QLabel(self.controleur.headers[3] + " :")
        self.inputSynonyme = QLineEdit()
        self.labelAnglais = QLabel(self.controleur.headers[4] + " :")
        self.inputAnglais = QLineEdit()
        self.labelEspagnol = QLabel(self.controleur.headers[5] + " :")
        self.inputEspagnol = QLineEdit()
        self.labelItalien = QLabel(self.controleur.headers[6] + " :")
        self.inputItalien = QLineEdit()
        # Déclaration du bouton permettant l'envoi du formulaire
        self.boutonEnvoyerAjout = QPushButton(self.controleur.titres[1])

        # Connexions des signaux/slots du bouton d'envoi pour envoyer le formulaire, raffraichir la vue et fermer le formulaire
        self.boutonEnvoyerAjout.clicked.connect(self.envoiFormulaireAjout)
        self.boutonEnvoyerAjout.clicked.connect(self.dessin)
        self.boutonEnvoyerAjout.clicked.connect(self.formulaireAjout.close)

        # Ajout des labels, champs et du bouton d'envoi au layout du formulaire
        self.layoutAjout.addWidget(self.labelMot,0,0)
        self.layoutAjout.addWidget(self.inputMot,1,0)
        self.layoutAjout.addWidget(self.labelNature,2,0)
        self.layoutAjout.addWidget(self.inputNature,3,0)
        self.layoutAjout.addWidget(self.labelDefinition,4,0)
        self.layoutAjout.addWidget(self.inputDefinition,5,0)
        self.layoutAjout.addWidget(self.labelSynonyme,6,0)
        self.layoutAjout.addWidget(self.inputSynonyme,7,0)
        self.layoutAjout.addWidget(self.labelAnglais,8,0)
        self.layoutAjout.addWidget(self.inputAnglais,9,0)
        self.layoutAjout.addWidget(self.labelEspagnol,10,0)
        self.layoutAjout.addWidget(self.inputEspagnol,11,0)
        self.layoutAjout.addWidget(self.labelItalien,12,0)
        self.layoutAjout.addWidget(self.inputItalien,13,0)
        self.layoutAjout.addWidget(self.boutonEnvoyerAjout,14,0)

        # Paramétrage du layout du formulaire, et affichage de celui ci
        self.formulaireAjout.setLayout(self.layoutAjout)
        self.formulaireAjout.show()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Fonction de suppression d'un mot via un formulaire
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    def supprimer(self):
        # Déclaration et paramétrage du widget accueillant le formulaire        
        self.formulaireSuppression = QWidget()
        self.formulaireSuppression.setWindowTitle(self.controleur.titres[2])
        self.formulaireSuppression.resize(500,100)

        # Déclaration du layout du formulaire
        self.layoutSuppression = QGridLayout()

        # Déclaration du label ainsi que du champ du formulaire
        self.labelSuppression = QLabel(self.controleur.headers[0] + " :")
        self.inputSuppression = QLineEdit()
       
        # Connexions des signaux/slots du bouton d'envoi pour envoyer le formulaire, raffraichir la vue et fermer le formulaire
        self.boutonEnvoyerSupp = QPushButton(self.controleur.titres[3])
        self.boutonEnvoyerSupp.clicked.connect(self.envoiFormulaireSuppression)
        self.boutonEnvoyerSupp.clicked.connect(self.dessin)
        self.boutonEnvoyerSupp.clicked.connect(self.formulaireSuppression.close)

        # Ajout du label, du champ et du bouton d'envoi au layout du formulaire
        self.layoutSuppression.addWidget(self.labelSuppression,0,0)
        self.layoutSuppression.addWidget(self.inputSuppression,1,0)
        self.layoutSuppression.addWidget(self.boutonEnvoyerSupp,2,0)
       
        # Paramétrage du layout du formulaire, et affichage de celui ci
        self.formulaireSuppression.setLayout(self.layoutSuppression)
        self.formulaireSuppression.show()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Fonction de modification d'un mot via un formulaire
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    def modifier(self):
        # Déclaration et paramétrage du widget accueillant le formulaire
        self.formulaireModif = QWidget()
        self.formulaireModif.setWindowTitle(self.controleur.titres[4])
        self.formulaireModif.resize(500,200)

        # Déclaration du layout du formulaire
        self.layoutModif = QGridLayout()

        # Déclaration des labels, des champs et des boutons radio du formulaire
        self.labelMotModif = QLabel(self.controleur.headers[0] + " :")
        self.inputMotModif = QLineEdit()
        self.labelChampsModif = QLabel(self.controleur.titres[6])
        self.groupeChamps = QButtonGroup()
        self.radioMot = QRadioButton(self.controleur.headers[0])
        self.radioNature = QRadioButton(self.controleur.headers[1])
        self.radioDefinition = QRadioButton(self.controleur.headers[2])
        self.radioSynonyme = QRadioButton(self.controleur.headers[3])
        self.radioTrad1 = QRadioButton(self.controleur.headers[4])
        self.radioTrad2 = QRadioButton(self.controleur.headers[5])
        self.radioTrad3 = QRadioButton(self.controleur.headers[6])
        self.groupeChamps.addButton(self.radioMot)
        self.groupeChamps.addButton(self.radioNature)
        self.groupeChamps.addButton(self.radioDefinition)
        self.groupeChamps.addButton(self.radioSynonyme)
        self.groupeChamps.addButton(self.radioTrad1)
        self.groupeChamps.addButton(self.radioTrad2)
        self.groupeChamps.addButton(self.radioTrad3)
        self.labelModif = QLabel(self.controleur.titres[7])
        self.inputModif = QLineEdit()

        # Déclaration du bouton permettant l'envoi du formulaire
        self.boutonEnvoyerModif = QPushButton(self.controleur.titres[5])

        # Connexions des signaux/slots du bouton d'envoi pour envoyer le formulaire, raffraichir la vue et fermer le formulaire
        self.boutonEnvoyerModif.clicked.connect(self.envoiFormulaireModif)
        self.boutonEnvoyerModif.clicked.connect(self.dessin)
        self.boutonEnvoyerModif.clicked.connect(self.formulaireModif.close)

        # Ajout des labels, champs et du bouton d'envoi au layout du formulaire
        self.layoutModif.addWidget(self.labelMotModif,0,0,1,4)
        self.layoutModif.addWidget(self.inputMotModif,1,0,1,4)
        self.layoutModif.addWidget(self.labelChampsModif,2,0,1,4)
        self.layoutModif.addWidget(self.radioMot,3,0)
        self.layoutModif.addWidget(self.radioNature,3,1)
        self.layoutModif.addWidget(self.radioDefinition,3,2)
        self.layoutModif.addWidget(self.radioSynonyme,3,3)
        self.layoutModif.addWidget(self.radioTrad1,4,0)
        self.layoutModif.addWidget(self.radioTrad2,4,1)
        self.layoutModif.addWidget(self.radioTrad3,4,2)
        self.layoutModif.addWidget(self.labelModif,5,0,1,4)
        self.layoutModif.addWidget(self.inputModif,6,0,1,4)
        self.layoutModif.addWidget(self.boutonEnvoyerModif,7,1,1,2)

        # Paramétrage du layout du formulaire, et affichage de celui ci
        self.formulaireModif.setLayout(self.layoutModif)
        self.formulaireModif.show()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Fonction permettant de rechercher des mots contenant une chaine de caractères
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    def affichageContenant(self):
        # Déclaration et paramétrage du widget accueillant le formulaire        
        self.formulaireContenant = QWidget()
        self.formulaireContenant.setWindowTitle(self.controleur.titres[8])
        self.formulaireContenant.resize(500,100)

        # Déclaration du layout du formulaire
        self.layoutContenant = QGridLayout()

        # Déclaration du label ainsi que du champ du formulaire
        self.labelContenant = QLabel(self.controleur.titres[9].capitalize())
        self.inputContenant = QLineEdit()
       
        # Connexions des signaux/slots du bouton d'envoi pour envoyer le formulaire, raffraichir la vue et fermer le formulaire
        self.boutonEnvoyerCont = QPushButton(self.controleur.headers[7])
        self.boutonEnvoyerCont.clicked.connect(self.envoiFormulaireContenant)
        self.boutonEnvoyerCont.clicked.connect(self.dessin)
        self.boutonEnvoyerCont.clicked.connect(self.formulaireContenant.close)

        # Ajout du label, du champ et du bouton d'envoi au layout du formulaire
        self.layoutContenant.addWidget(self.labelContenant,0,0)
        self.layoutContenant.addWidget(self.inputContenant,1,0)
        self.layoutContenant.addWidget(self.boutonEnvoyerCont,2,0)
       
        # Paramétrage du layout du formulaire, et affichage de celui ci
        self.formulaireContenant.setLayout(self.layoutContenant)
        self.formulaireContenant.show()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Fonction permettant de rechercher des mots se terminant par une chaine de caractères
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    def affichageTerminant(self):
        # Déclaration et paramétrage du widget accueillant le formulaire        
        self.formulaireTerminant = QWidget()
        self.formulaireTerminant.setWindowTitle(self.controleur.titres[10])
        self.formulaireTerminant.resize(500,100)

        # Déclaration du layout du formulaire
        self.layoutTerminant = QGridLayout()

        # Déclaration du label ainsi que du champ du formulaire
        self.labelTerminant = QLabel(self.controleur.titres[9].capitalize())
        self.inputTerminant = QLineEdit()
       
        # Connexions des signaux/slots du bouton d'envoi pour envoyer le formulaire, raffraichir la vue et fermer le formulaire
        self.boutonEnvoyerTerm = QPushButton(self.controleur.headers[7])
        self.boutonEnvoyerTerm.clicked.connect(self.envoiFormulaireTerminant)
        self.boutonEnvoyerTerm.clicked.connect(self.dessin)
        self.boutonEnvoyerTerm.clicked.connect(self.formulaireTerminant.close)

        # Ajout du label, du champ et du bouton d'envoi au layout du formulaire
        self.layoutTerminant.addWidget(self.labelTerminant,0,0)
        self.layoutTerminant.addWidget(self.inputTerminant,1,0)
        self.layoutTerminant.addWidget(self.boutonEnvoyerTerm,2,0)
       
        # Paramétrage du layout du formulaire, et affichage de celui ci
        self.formulaireTerminant.setLayout(self.layoutTerminant)
        self.formulaireTerminant.show()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Fonction permettant d'afficher les résultats dans l'ordre alphabétique inverse
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    def affichageCroissant(self):
        self.controleur.requeteur(self.recherche.text())

    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Fonction permettant d'afficher les résultats dans l'ordre alphabétique
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    def affichageDecroissant(self):
        self.controleur.affichageDecroissant(self.recherche.text())

    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Fonction permettant l'envoi du formulaire afin d'ajouter un nouveau mot à la BDD
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    def envoiFormulaireAjout(self):
        # Déclaration d'une liste contenant tous les champs du formulaire
        self.listeChampsAjout = [self.inputMot.text().lower(), self.inputNature.text().lower(), self.inputDefinition.text().lower(), self.inputSynonyme.text().lower(),
        self.inputAnglais.text().lower(), self.inputEspagnol.text().lower(), self.inputItalien.text().lower()]

        # Appel de la méthode du controleur "ajouter" avec comme argument la liste des champs du formulaire
        self.controleur.ajouter(self.listeChampsAjout)

    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Fonction permettant l'envoi du formulaire afin de supprimer un nouveau mot à la BDD
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    def envoiFormulaireSuppression(self):
        # Appel de la méthode du controleur "supprimer" avec comme argument le champ du formulaire
        self.controleur.supprimer(self.inputSuppression.text().lower())

    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Fonction permettant l'envoi du formulaire afin de modifier un mot de la BDD
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    def envoiFormulaireModif(self):
        self.champSelec = ""
        if self.groupeChamps.checkedId() == -2:
            self.champSelec = "nom"
        elif self.groupeChamps.checkedId() == -3:
            self.champSelec = "nature"
        elif self.groupeChamps.checkedId() == -4:
            self.champSelec = "definition"
        elif self.groupeChamps.checkedId() == -5:
            self.champSelec = "synonyme"
        elif self.groupeChamps.checkedId() == -6:
            self.champSelec = self.modele.traduction[0]
        elif self.groupeChamps.checkedId() == -7:
            self.champSelec = self.modele.traduction[1]
        elif self.groupeChamps.checkedId() == -8:
            self.champSelec = self.modele.traduction[2]

        # Déclaration d'une liste contenant tous les champs du formulaire
        self.listeChampsModif = [self.champSelec, self.inputMotModif.text().lower(), self.inputModif.text().lower()]

        # Appel de la méthode du controleur "modifier" avec comme argument la liste des champs du formulaire
        self.controleur.modifier(self.listeChampsModif)

    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Fonction permettant l'envoi du formulaire afin de rechercher un mot contenant une chaine de caractères
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    def envoiFormulaireContenant(self):
        # Appel de la méthode du controleur "requeteur" avec comme argument le champ du contenant la chaine de caractères
        self.controleur.requeteur("%"+self.inputContenant.text().lower()+"%")

    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Fonction permettant l'envoi du formulaire afin de rechercher un mot se terminant par une chaine de caractère
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    def envoiFormulaireTerminant(self):
        # Appel de la méthode du controleur "terminant" avec comme argument le champ contenant la chaine de caractères
        self.controleur.terminant(self.inputTerminant.text().lower())

    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Fonction permettant de checker le bouton de langue sélectionné et de déselectionner les autres
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    def checker(self):
        # Récupération de l'information au sujet du drapeau sélectionné
        self.drapeauSelec = self.groupeDrapeaux.checkedButton()
        # Désélection de tous les drapeaux
        self.boutonFr.setChecked(False)
        self.boutonGb.setChecked(False)
        self.boutonEs.setChecked(False)
        self.boutonIt.setChecked(False)
        # Sélection du drapeau sélectionné
        self.drapeauSelec.setChecked(True)

    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Fonction permettant d'afficher aléatoirement des chats
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    def chat(self):
        self.fenetreChat = QWidget()
        self.fenetreChat.setWindowTitle("Chat")

        self.listeChat = ["img/chat1.gif", "img/chat2.jpg", "img/chat3.jpg", "img/chat4.jpg", "img/chat5.jpg", "img/chat6.jpg", "img/chat7.jpg"
        , "img/chat8.jpg", "img/chat9.jpg", "img/chat10.jpg"]

        self.labelChat = QLabel()
        if self.numeroPhoto < 9:
            self.numeroPhoto += 1
        else:
            self.numeroPhoto = 0
        self.pix = QPixmap(self.listeChat[self.numeroPhoto])
        self.labelChat.setPixmap(self.pix)

        self.boutonPlusChat = QPushButton("Encore !")
        self.boutonPlusChat.clicked.connect(self.fenetreChat.close)
        self.boutonPlusChat.clicked.connect(self.chat)

        self.fenetreChat.resize(self.pix.size())
        self.layoutChat = QGridLayout()
        self.layoutChat.addWidget(self.labelChat,0,0,)
        self.layoutChat.addWidget(self.boutonPlusChat,1,0)
        self.fenetreChat.setLayout(self.layoutChat)

        self.fenetreChat.show()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Fonction permettant d'afficher les informations à propos du projet
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    def info(self):
        self.fenetreInfo = QWidget()
        self.fenetreInfo.setWindowTitle("À propos...")

        self.labelInfo = QLabel("Benjamin HAOUI, Guillaume DUBOIS & Jocelyne BOUN sont fiers de vous présenter\nleur Dictionnaire Multilingue Intéractif !\n\n"
            "Nous espérons qu'il conviendra parfaitement à votre usage, en répondant à toutes\nvos attentes.\n\n"
            "Liste des fonctionnalités :\n\n"
            "Recherche : Insérer votre recherche dans la barre de recherche, et profitez d'un\naffichage à la volée des résultats ! Bluffant\n\n"
            "Ajouter : Vous avez besoin d'insérer un nouveau mot dans le dictionnaire ? Aucun\nproblème ! Remplissez simplement le formulaire, et le tour est joué. Magique\n\n"
            "Supprimer: Un mot de vous plait pas ? Sa simple vision vous insuporte ?\nAucun problème ! Indiquez simplement son nom, et nous nous occupons de\nlui. À votre service\n\n"
            "Modifier : Vous n'êtes pas d'accord avec la définition d'un mot ? Restez calme !\nRemplissez simplement le formulaire, et votre voeux sera exaucé. Serein\n\n"
            "Croissant : Vous n'avez pas eu le temps de prendre votre p'tit dej' ? Pas de soucis.\nChoisissez l'affichage par ordre alphabétique croissant. Pragmatique\n\n"
            "Décroissant : Ou alors l'ordre alphabétique décroissant. A votre guise.\n\n"
            "Rechercher un mot contenant... : Vous vous êtes toujours demandés quels étaient\nles mots contenant 'chat' ? Cette fonctionnalité est faite pour vous. Dédicasse\n\n"
            "Rechercher un mot se terminant par... : Vous cherchez plutôt les mots finissant\npar 'python' ? Nous avons pensé à vous. Comme toujours.\n\n"
            "Chat : Notre déontologie nous oblige à vous déconseiller d'utiliser cette\nfonctionnalité en public... Intrépide\n\n"
            "Dictionnaire Quadrilingue : Vous n'avez jamais été doué pour les langues\nétrangères ? Cette époque est révolue ! Vous pouvez dorénavant parlez Français,\nAnglais, Espagnol et Italien ! Et switcher de dictionnaire en un clic, en profitant\nde la traduction de tous les menus et formulaires, à la volée. Amazing")
        self.labelInfo.setFont(QFont("Arial", 11, QFont.Bold))
        self.layoutInfo = QGridLayout()
        self.layoutInfo.addWidget(self.labelInfo,0,0)
        self.fenetreInfo.setLayout(self.layoutInfo)

        self.fenetreInfo.show()

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                           Main
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Instanciation de la vue, déclaration de la taille, du titre et affichage de la fenêtre
    fenetrePrincipale = vue()
    fenetrePrincipale.resize(985,400)
    fenetrePrincipale.setWindowTitle("iDictionnaire")
    
    fenetrePrincipale.show()

    sys.exit(app.exec_())
