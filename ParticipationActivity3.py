'''Participation Activity 3
Darian Marie Bruce
02/01/2026'''

import random

descriptive_words = ['cutie', 'bubbly', 'sweet', 'little', 'snuggle', 'honey', 'chunky',
                     'cuddle', 'angel', 'sleepy', 'bouncy', 'soft', 'sugar', 'cheeky',
                     'funny', 'tiny', 'googly', 'squishy', 'baby', 'jiggly', 'pretty',
                     'joy', 'mini', 'huggy', 'lovey', 'pumpkin', 'snicker', 'bunny',
                     'milky', 'delightful', 'dreamy', 'starry', 'sweet']
nouns = ['pie', 'pudding', 'muffin', 'cupcake', 'dumpling', 'bear', 'buttercup',
         'bean', 'bug', 'sprout', 'cake', 'face', 'button', 'doll', 'kitten',
         'berry', '']

descriptive_word_choice = random.choice(descriptive_words).title()

noun_choice = random.choice(nouns).title()

print(f"Your generated cute name is: {descriptive_word_choice} {noun_choice}")