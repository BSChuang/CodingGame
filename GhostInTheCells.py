import sys
import math
import random

factory_count = int(input())  # the number of factories
link_count = int(input())  # the number of links between factories
for i in range(link_count):
    factory_1, factory_2, distance = [int(j) for j in input().split()]

def Move(source, destination, cyborgCount):
    return "MOVE" + " " + str(source) + " " + str(destination) + " " + str(round(cyborgCount)) + ";"

def Bomb(source, destination):
    return "BOMB" + " " + str(source) + " " + str(destination) + ";"

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
    oppFactCyb = []
    oppFactProd = []
    
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
                oppFactCyb.append(int(arg_2))
                oppFactProd.append(int(arg_3))
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
    if turn == 3 or turn == 13:
        maxOppFact = oppFacts[oppFactCyb.index(max(oppFactCyb))] # Find highest opp factory production
        moveText += Bomb(ownFacts[0], maxOppFact)
    if turn == 1 or turn == 4 or turn == 8:
        maxNeutFact = neutFacts[neutFactProd.index(max(neutFactProd))] # Find highest neut factory production
        ownCybFact = ownFacts[ownFactCyb.index(max(ownFactCyb))] # Find highest own factory cyborgs
        moveText += Move(ownCybFact, maxNeutFact, max(ownFactCyb) / 2) # 
    #elif :
        
    moveText += "WAIT;"
    
    
    # DEFENSE - If factory is being attacked, send equal to help troops
    for i in range(len(ownFacts)):
        if facts[ownFacts[i]][0] == 1 and factCyb[ownFacts[i]] < 1: # If its gone negative and still own factory, send equal troops plus some more, 
            cybsToSend = abs(factCyb[ownFacts[i]]) + 3
            for j in range(len(ownFacts)): # Sending enough cyborgs to necessary factory
                if j != i: # If not the same factory
                    if cybsToSend > facts[ownFacts[j]][1]: # If there are more cybs that need to be sent than cybs available, move all minus 2
                        cybsToSend -= facts[ownFacts[j]][1]
                        moveText += Move(ownFacts[j], ownFacts[i], facts[ownFacts[j]][1] - 2)
                    else:
                        moveText += Move(ownFacts[j], ownFacts[i], cybsToSend) # If there are enough cybs to send, send all necessary
    #print(str(facts[ownFacts[i]][0]) + " " + str(factCyb[ownFacts[i]]), file=sys.stderr)



    print(moveText[:-1])


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