import random
prevEatery = 'Golden Dragon'

foods = ['Bagel Place', 'Golden Dragon', "Sam's", 'Diner', 'Dawg House']
foods.remove(prevEatery)
print(foods[random.randint(0, len(foods) - 1)])