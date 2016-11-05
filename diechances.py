import random

chances = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}
i = 0
while i < 10000:
    i += 1
    chances[random.randint(1, 6)] += 1
print (chances)