'''facts = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Factories
cybsToSend = 10
moveText = ""
def Move(source, destination, cybs):
    return "MOVE " +  str(source) + " " + str(destination) + " " + str(cybs) + "; "
for i in range(len(facts)): # Sending enough cyborgs to necessary factory
    if cybsToSend > facts[i][1]:
        cybsToSend -= facts[i][1]
        moveText += Move(1, 2, str(facts[i][1]))
    else:
        moveText += Move(1, 2, str(cybsToSend))
print(moveText)'''

import sys
import math
import random

factory_count = int(input())  # the number of factories
link_count = int(input())  # the number of links between factories
for i in range(link_count):
    factory_1, factory_2, distance = [int(j) for j in input().split()]

def Move(source, destination, cyborgCount):
    return "MOVE" + " " + str(source) + " " + str(destination) + " " + str(cyborgCount) + ";"

turn = 0
while True:
    turn += 1
    moveText = ""
    entity_count = int(input())  # the number of entities (e.g. factories and troops)
    
    facts = [] # [Owner, # of cybs, Factory production]
    troops = [] # [Owner, Fact Depart, Fact Arrive, # of Cybs, Distance]
    
    ownCyb = 0
    ownProd = 0
    
    oppCyb = 0
    oppProd = 0
    
    ownFacts = []
    ownFactCyb = []
    ownFactProd = []
    
    neutFacts = []
    neutCyb = []
    neutFactProd = []
    
    oppFacts = []
    
    factOwner = []
    factCyb = []
    factProd = []
    
    troopOwner = []
    troopDepart = []
    troopTarget = []
    troopCyb = []
    troopDist = []
    
    stillNeut = False;
    stillOpp = False;
    for i in range(entity_count):
        entity_id, entity_type, arg_1, arg_2, arg_3, arg_4, arg_5 = input().split()
        entity_id = int(entity_id)
        
        tempList = []
        if entity_type == "FACTORY":
            factOwner.append(int(arg_1)) # Owner. 1=mine,-1=opponent, 0=neutral
            
            tempList.append(int(arg_1))
            tempList.append(int(arg_2))
            tempList.append(int(arg_3))
            facts.append(tempList)
            
            if int(arg_1) == 0:
                factCyb.append(int(arg_2) * -1) # Number of cyborgs. Number of cyborgs in the factory
            else:
                factCyb.append(int(arg_2) * int(arg_1)) # Number of cyborgs. Number of cyborgs in the fact
                
            factProd.append(int(arg_3)) # Factory Production (0-3)
            if int(arg_1) == 1:
                ownFacts.append(entity_id)
                ownCyb += int(arg_2)
                ownProd += int(arg_3)
                ownFactCyb.append(int(arg_2))
                ownFactProd.append(int(arg_3))
            elif int(arg_1) == 0:
                stillNeut = True
                neutFacts.append(entity_id)
                neutFactProd.append(int(arg_3))
            elif int(arg_1) == -1:
                stillOpp = True
                oppFacts.append(entity_id)
                oppCyb += int(arg_2)
                oppProd += int(arg_3)
        elif entity_type == "TROOP":
            
            tempList.append(int(arg_1))
            tempList.append(int(arg_2))
            tempList.append(int(arg_3))
            tempList.append(int(arg_4))
            tempList.append(int(arg_5))
            troops.append(tempList)
            
            troopOwner.append(int(arg_1)) # 1=mine,-1=opponent
            troopDepart.append(int(arg_2)) # Factory the troop left from
            troopTarget.append(int(arg_3)) # Factory targeted by the troop
            troopCyb.append(int(arg_4)) # number of cyborgs in the troop (positive integer)
            troopDist.append(int(arg_5)) # remaining number of turns before the troop arrives (positive integer)
            factCyb[int(arg_3)] += int(arg_4) * int(arg_1) # Sees where cyborgs are going
            if int(arg_1) == 1:
                ownCyb += int(arg_4)
            if int(arg_1) == -1:
                oppCyb += int(arg_4)
    print("Production: " + str(ownProd) + ", " + str(oppProd),file=sys.stderr)
    print("Cyborgs: " + str(ownCyb) + ", " + str(oppCyb),file=sys.stderr)
    print("Fact Cybs: " + str(factCyb),file=sys.stderr)
    print("Facts: " + str(facts),file=sys.stderr)
    print("Troops: " + str(troops),file=sys.stderr)
    

    # OFFENSE - Attack whatever they attack or claim neutrals. Have enough cyborgs to fend off an attack
    if turn == 1:
        maxNeutFact = neutFacts[neutFactProd.index(max(neutFactProd))] # Find highest factory production
        startFact = ownFacts[0]
        moveText += Move(startFact, maxNeutFact, ownFactCyb[0])#facts[maxNeutFact][1] + 1)
    #elif :
        
    moveText += "WAIT;"
    
    
    # DEFENSE - If factory is being attacked, send equal to help troops
    for i in range(len(ownFacts)):
        if facts[ownFacts[i]][0] == 1 and factCyb[ownFacts[i]] < 1: # If its gone negative and still own factory, send equal troops plus some more, 
           print(str(facts[ownFacts[i]][0]) + " " + str(factCyb[ownFacts[i]]), file=sys.stderr)
       # START HERE: SEND TROOP WHEREVER NEEDED



    print(moveText[:-1])


 
    '''if ownProd <= oppProd:
        if stillNeut:
            maxNeutFact = neutFacts[neutFactProd.index(max(neutFactProd))] # Find highest factory production
        else:
            max
        maxOwnFact = ownFacts[ownFactCyb.index(max(ownFactCyb))] # Find the factory with the highest production
        moveText += Move(maxOwnFact, maxNeutFact, abs(factCyb[maxNeutFact]) + 1) # Move one more cyborg than necessary
    else:
        moveText += "WAIT;"'''
    

    
    
    
    
    

    
    
    '''
import sys
import math
import random

factory_count = int(input())  # the number of factories
link_count = int(input())  # the number of links between factories
for i in range(link_count):
    factory_1, factory_2, distance = [int(j) for j in input().split()]

def Move(source, destination, cyborgCount):
    return "MOVE" + " " + str(source) + " " + str(destination) + " " + str(cyborgCount) + ";"

turn = 0
while True:
    turn += 1
    print(str(turn), file=sys.stderr)
    entity_count = int(input())  # the number of entities (e.g. factories and troops)
    ownedFact = [] # Factory Number
    ownedFactCyb = [] # Factory Cyborgs. In order of owned Factory list
    ownedFactProd = []
    neutFact = []
    neutFactCyb = []
    factFutCyb = []
    neutFactProd = []
    oppFact = []
    oppFactCyb = []
    oppFactProd = []
    
    stillNeut = False;
    stillOpp = False;
    for i in range(entity_count):
        entity_id, entity_type, arg_1, arg_2, arg_3, arg_4, arg_5 = input().split()
        entity_id = int(entity_id)
        if entity_type == "FACTORY":
            owner = int(arg_1) # 1=mine,-1=opponent, 0=neutral
            numCyb = int(arg_2) # Number of cyborgs in the factory
            factProd = int(arg_3) # Factory Production (0-3)
            if owner == 1:
                ownedFact.append(entity_id)
                ownedFactCyb.append(numCyb)
            elif owner == 0 and factProd > 0:
                neutFact.append(entity_id)
                neutFactCyb.append(entity_id)
                neutFactProd.append(factProd)
                stillNeut = True
            elif owner == -1:
                oppFact.append(entity_id)
                oppFactCyb.append(numCyb)
                oppFactProd.append(factProd)
                stillOpp = True
        elif entity_type == "TROOP":
            owner = int(arg_1) # 1=mine,-1=opponent
            factDepart = int(arg_2) # Factory the troop left from
            factTarget = int(arg_3) # Factory targetted by the troop
            CybTroop = int(arg_4) # number of cyborgs in the troop (positive integer)
            arrivalTurns = int(arg_5) # remaining number of turns before the troop arrives (positive integer)
            #if factTarget in ownedFact: # If the target factory is mine, add the troops to it
             #   ownedFactCyb[ownedFact.index(factTarget)] += CybTroop * owner
            #if factTarget in neutFact:
             #   neutFactCyb[neutFact.index(factTarget)] += CybTroop * owner
            #if factTarget in oppFact:
             #   oppFactCyb[oppFact.index(factTarget)] += CybTroop * owner
    
    if stillNeut:
        moveText = ""
        if turn == 10 or turn == 20:
            startFact = ownedFact[random.randint(0, len(ownedFact) - 1)]
            endFact = oppFact[oppFactProd.index(max(oppFactProd))]
            moveText = "BOMB " + str(startFact) + " " + str(endFact) + ";"
            
        for i in range(len(ownedFact)):
            startFact = ownedFact[i]
            
    
    
    
    if stillNeut:
        moveText = ""
        if turn == 10 or turn == 20:
            startFact = ownedFact[random.randint(0, len(ownedFact) - 1)]
            endFact = oppFact[oppFactProd.index(max(oppFactProd))]
            moveText = "BOMB " + str(startFact) + " " + str(endFact) + ";"

        for i in range(len(ownedFact)):
            startFact = ownedFact[i]
            endFact = neutFact[neutFactProd.index(max(neutFactProd))] # Neutral factory with highest production
            moveText += Move(startFact, endFact, int(round(ownedFactCyb[i] / 4)))# int(round(ownedFactCyb[i] / 4))) # Sets one move to factory
            if len(neutFact) > 2:
                neutFactProd.pop(neutFact.index(endFact)) # Removes previous factory production from list
                neutFact.remove(endFact) # Removes previous factory from list
                endFact = neutFact[neutFactProd.index(max(neutFactProd))] # Second highest factory from list
                moveText += Move(startFact, endFact, int(round(ownedFactCyb[i] / 4))) # Sets second move to factory
            if len(neutFact) > 1:
                neutFactProd.pop(neutFact.index(endFact)) # Removes previous factory production from list
                neutFact.remove(endFact) # Removes previous factory from list
                endFact = neutFact[neutFactProd.index(max(neutFactProd))] # Second highest factory from list
                moveText += Move(startFact, endFact, int(round(ownedFactCyb[i] / 4))) # Sets second move to factory
        print(moveText[:-1])
    elif stillOpp:
        moveText = ""
        if turn == 10 or turn == 20:
            startFact = ownedFact[random.randint(0, len(ownedFact) - 1)]
            endFact = oppFact[oppFactProd.index(max(oppFactProd))]
            moveText = "BOMB " + str(startFact) + " " + str(endFact) + ";"
            
        for i in range(len(ownedFact)):
            startFact = ownedFact[i]
            endFact = oppFact[oppFactProd.index(max(oppFactProd))] # Enemy factory with highest production
            moveText += Move(startFact, endFact, int(round(ownedFactCyb[i] / 3))) # Sets one move to factory
            if len(oppFact) > 1:
                oppFactProd.pop(oppFact.index(endFact)) # Removes previous factory production from list
                oppFact.remove(endFact) # Removes previous factory from list
                endFact = oppFact[oppFactProd.index(max(oppFactProd))] # Second highest factory from list
                moveText += Move(startFact, endFact, int(round(ownedFactCyb[i] / 3))) # Sets second move to factory
        print(moveText[:-1])
    else:
        print("WAIT")'''
    
    
''' WOOD 3 LEAGUE
    if stillNeut: #If there are still neutral factories, send half of the factory with the most cyb to neutral factory
        mostOwnCybFact = ownedFact[ownedFactCyb.index(max(ownedFactCyb))] # Finds most cyb, then position in list, then corresponding factory
        startFact = mostOwnCybFact
        
        endFact = neutFact[neutFactProd.index(max(neutFactProd))] # Highest producing factories first
        
        
        #Move(startFact, endFact, neutFactCyb[endFact - 1] + 1)
        Move(startFact, endFact, int(round(max(ownedFactCyb)/2)))
    elif stillOpp:
        mostOwnCybFact = ownedFact[ownedFactCyb.index(max(ownedFactCyb))]
        startFact = mostOwnCybFact
        leastOppCybFact = oppFact[oppFactCyb.index(min(oppFactCyb))]
        endFact = leastOppCybFact
        
        
        Move(startFact, endFact, int(round(max(ownedFactCyb)/2)))
    else:
        print("WAIT")
'''

    # To debug: print("Debug messages...", file=sys.stderr)


