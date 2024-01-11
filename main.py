import random
from datetime import datetime

def jours_restants_jusqu_a_anniversaire():
    # Obtenir la date actuelle
    date_actuelle = datetime.now()

    # Définir la date de l'anniversaire
    anniversaire = datetime(date_actuelle.year, 5, 20)

    # Vérifier si l'anniversaire est déjà passé cette année, sinon, ajuster pour l'année suivante
    if date_actuelle > anniversaire:
        anniversaire = datetime(date_actuelle.year + 1, 5, 20)

    # Calculer les jours restants
    jours_restants = (anniversaire - date_actuelle).days

    # Utiliser la fonction
    if jours_restants == 0:
        message_anniversaire = "❤️❤️❤️  C'est mon anniversaire. ❤️❤️❤️"
    else:
        message_anniversaire = f"❤️❤️❤️  There are {jours_restants} days left until your birthday. ❤️❤️❤️"

    return message_anniversaire

def obtenir_date_du_jour():
    date_du_jour = datetime.today().strftime('%d-%m-%Y')
    return date_du_jour

def getGibotSigning():
  liste_de_mots = [
      'hate',
      'wickedness',
      'pleasure',
      'wickedness',
      'cruelty',
      'horror',
      'love'
  ]
  # Choisir un mot au hasard
  mot_choisi = random.choice(liste_de_mots)
  # Utiliser le mot choisi dans la chaîne de formatage
  signature = f'🤖 This README.md is updated with {mot_choisi}, by Gibot ❤️'
  return signature

anniv = jours_restants_jusqu_a_anniversaire()
print(anniv)
  
# variable du fichier Markdown
nom_fichier_md = "README.md"
resultat = getGibotSigning()
date_md = obtenir_date_du_jour()
contenu_md = """
About me - Hi there 👋
Why you'd want to hang out with me

My name is The gibaus. I have the following qualities:

    I rock a great beard
    I’m extremely loyal to my friends
    I like gaming and movies

That rug really tied the room together.
my history

To be honest, I’m having some trouble remembering right now, so why don’t you just watch my movie and it will answer all your questions

in professional reskilling

I am looking for new skills to increase my knowledge

open to all who can increase my learning abilities

added on 3 Jan 2024

update on """

# Écriture du fichier Markdown
with open(nom_fichier_md, "w", encoding="utf-8") as fichier_md:
    fichier_md.write(contenu_md)
    fichier_md.write(date_md + "\n\n")
    fichier_md.write(anniv + "\n\n")
    fichier_md.write(resultat)
    
print(f"Le fichier {nom_fichier_md} a été créé avec succès.")
