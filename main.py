import random
from datetime import datetime

def days_until_birthday():
    # Get the current date
    current_date = datetime.now()

    # Set the birthday date
    birthday = datetime(current_date.year, 5, 20)

    # Check if the birthday has already passed this year, otherwise adjust for the next year
    if current_date > birthday:
        birthday = datetime(current_date.year + 1, 5, 20)

    # Calculate the days remaining
    days_remaining = (birthday - current_date).days

    # Use the function
    if days_remaining == 0:
        birthday_message = "❤️❤️❤️  It's my birthday! ❤️❤️❤️"
    else:
        birthday_message = f"❤️❤️❤️  There are {days_remaining} days left until my birthday. ❤️❤️❤️"

    return birthday_message

def get_gibot_signing():
    word_list = [
        'hate',
        'wickedness',
        'pleasure',
        'wickedness',
        'cruelty',
        'horror',
        'love'
    ]
    # Choose a random word
    chosen_word = random.choice(word_list)
    # Use the chosen word in the formatting string
    signature = f'🤖 This README.md is updated with {chosen_word}, by Gibot ❤️'
    return signature

birthday_message = days_until_birthday()
print(birthday_message)

# Markdown file variables
md_file_name = "README.md"
signature_result = get_gibot_signing()
md_date = datetime.today().strftime('%d-%m-%Y')
md_content = f"""
About me - Hi there 👋
Why you'd want to hang out with me

My name is The Gibaus. I have the following qualities:

    I rock a great beard
    I’m extremely loyal to my friends
    I like gaming and movies

That rug really tied the room together.
my history

To be honest, I’m having some trouble remembering right now, so why don’t you just watch my movie, and it will answer all your questions.

in professional reskilling

I am looking for new skills to increase my knowledge

open to all who can increase my learning abilities

added on 3 Jan 2024

update on {md_date}

{birthday_message}

{signature_result}
"""

# Writing the Markdown file
with open(md_file_name, "w", encoding="utf-8") as md_file:
    md_file.write(md_content)

print(f"The file {md_file_name} has been successfully created.")
