import random
from datetime import datetime

def obtenir_date_du_jour():
    date_du_jour = datetime.today().strftime('%Y-%m-%d')
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
  
# variable du fichier Markdown
nom_fichier_md = "readme.md"
resultat = getGibotSigning()
date_md = obtenir_date_du_jour()
contenu_md = """
Hi there 👋

in professional reskilling

I am looking for new skills to increase my knowledge

open to all who can increase my learning abilities

added on 3 Jan 2024

update on """

# Écriture du fichier Markdown
with open(nom_fichier_md, "w", encoding="utf-8") as fichier_md:
    fichier_md.write(contenu_md)
    fichier_md.write(date_md + "\n\n")
    fichier_md.write(resultat)

print(f"Le fichier {nom_fichier_md} a été créé avec succès.")
