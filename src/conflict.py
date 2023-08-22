from src.deck import Deck

class ConflictDeck(Deck):
    def __init__(self, conflict1_amount = 1, conflict2_amount = 5, conflict3_amount = 4) -> None:
        super().__init__([])
        self.conflicts = (get_random_conflicts_of(ConflictIII, conflict3_amount)
                           + get_random_conflicts_of(ConflictII, conflict2_amount)
                           + get_random_conflicts_of(ConflictI, conflict1_amount))
        self.contents = self.conflicts[:]

class Conflict:
    def __init__(self, name, first_reward, second_reward, third_reward) -> None:
        self.name = name
        self.first_reward = first_reward
        self.second_reward = second_reward
        self.third_reward = third_reward

class ConflictI(Conflict):
    all = []

    def __init__(self, name, first_reward, second_reward, third_reward) -> None:
        super().__init__(name, first_reward, second_reward, third_reward)
        ConflictI.all.append(self)

class ConflictII(Conflict):
    all = []
    
    def __init__(self, name, first_reward, second_reward, third_reward) -> None:
        super().__init__(name, first_reward, second_reward, third_reward)
        ConflictII.all.append(self)

class ConflictIII(Conflict):
    all = []
    
    def __init__(self, name, first_reward, second_reward, third_reward) -> None:
        super().__init__(name, first_reward, second_reward, third_reward)
        ConflictIII.all.append(self)

import random
def get_random_conflicts_of(conflict_class, amount):  
    scrambled_conflicts = conflict_class.all[:]
    random.shuffle(scrambled_conflicts)
    conflicts_of_amount = scrambled_conflicts[0:amount]
    return conflicts_of_amount

import json
conflicts_file = open("assets/conflicts.json")
all_conflicts = json.load(conflicts_file)

for conflictI in all_conflicts["conflictIs"]:
    ConflictI(conflictI["name"], conflictI["first_reward"], conflictI["second_reward"], conflictI["third_reward"])

for conflictII in all_conflicts["conflictIIs"]:
    ConflictII(conflictII["name"], conflictII["first_reward"], conflictII["second_reward"], conflictII["third_reward"])

for conflictIII in all_conflicts["conflictIIIs"]:
    ConflictIII(conflictIII["name"], conflictIII["first_reward"], conflictIII["second_reward"], conflictIII["third_reward"])

# WATCH OUT FOR: Grand Vision (Conflict III) 2 bumps on a faction where you can only gain 1/0
# And choose 2 out of many resources
