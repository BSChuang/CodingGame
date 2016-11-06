import random
prevEatery = 'Golden Dragon'

foods = ['Bagel Place', 'Golden Dragon', "Sam's", 'Diner', 'Dawg House']
#foods.remove(prevEatery)
for i in range(len(foods)):
    whereToGo = foods[random.randint(0, len(foods) - 1)] 
    print(whereToGo)
    foods.remove(whereToGo)