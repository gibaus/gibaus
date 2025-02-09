import random
import os
from datetime import datetime

# Nom du fichier README.md
md_file_name = "README.md"

# Supprimer le fichier README.md s'il existe déjà
try:
    if os.path.exists(md_file_name):
        os.remove(md_file_name)
        print(f"Le fichier {md_file_name} a été supprimé avec succès.")
except Exception as e:
    print(f"Erreur lors de la suppression du fichier {md_file_name}: {e}")

def days_until_birthday():
    """Retourne un message indiquant le nombre de jours restants avant l'anniversaire."""
    current_date = datetime.now()
    birthday = datetime(current_date.year, 5, 20)

    # Si l'anniversaire est déjà passé cette année, on le calcule pour l'année prochaine
    if current_date > birthday:
        birthday = datetime(current_date.year + 1, 5, 20)

    # Calcul des jours restants
    days_remaining = (birthday - current_date).days

    # Message en fonction de l'anniversaire
    if days_remaining == 0:
        birthday_message = "❤️❤️❤️  C'est mon anniversaire aujourd'hui ! ❤️❤️❤️"
    else:
        birthday_message = f"❤️❤️❤️  Il reste {days_remaining} jours avant mon anniversaire. ❤️❤️❤️"

    return birthday_message

def get_gibot_signing():
    """Retourne une signature aléatoire à partir d'une liste de mots."""
    word_list = [
        'haine',
        'méchanceté',
        'plaisir',
        'cruauté',
        'horreur',
        'amour'
    ]
    # Choisir un mot aléatoire
    chosen_word = random.choice(word_list)
    signature = f'🤖 Ce README.md est mis à jour avec {chosen_word}, par Gibot ❤️'
    return signature

# Calculer le message d'anniversaire
birthday_message = days_until_birthday()
print(birthday_message)

# Variables pour le fichier Markdown
signature_result = get_gibot_signing()
md_date = datetime.today().strftime('%d-%m-%Y')
md_content = f"""
À propos de moi - Salut 👋
Pourquoi vous voudriez passer du temps avec moi

Je m'appelle The GIBAUS. Voici mes qualités :

    J'ai une super barbe
    Je suis extrêmement loyal envers mes amis
    J'aime les jeux vidéo et les films

Ce tapis a vraiment bien harmonisé la pièce.
Mon histoire

Pour être honnête, j'ai un peu de mal à m'en souvenir en ce moment, alors pourquoi ne pas regarder mon film et il répondra à toutes vos questions.

Dans la reconversion professionnelle

Je cherche de nouvelles compétences pour augmenter mes connaissances

Ouvert à tous ceux qui peuvent accroître mes capacités d'apprentissage

Ajouté le 3 janvier 2024

Mise à jour du {md_date}

{birthday_message}

{signature_result}
"""

# Écrire dans le fichier Markdown
try:
    with open(md_file_name, "w", encoding="utf-8") as md_file:
        md_file.write(md_content)
    print(f"Le fichier {md_file_name} a été créé avec succès.")
except Exception as e:
    print(f"Erreur lors de la création du fichier {md_file_name}: {e}")
