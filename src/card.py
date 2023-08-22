import copy
from src.deck import Deck

class Card:
    def __init__(self, name, factions, price, icons, on_use, on_reveal):
        self.name = name
        self.factions = factions
        self.price = price
        self.icons = icons

        # Rewards
        self.on_use = on_use
        self.on_reveal = on_reveal

class StartingCard(Card):
    all = []

    def __init__(self, name, icons, on_use, on_reveal, copies = 1):
        super().__init__(name, [], "starter", icons, on_use, on_reveal)
        while copies > 0:
            StartingCard.all.append(self)
            copies -= 1

class ReserveCard(Card):
    all = {}

    def __init__(self, name, factions, price, icons, on_use, on_reveal, copies = 99, on_acquire = {}):
        super().__init__(name, factions, price, icons, on_use, on_reveal)
        self.on_acquire = on_acquire
        ReserveCard.all[name] = copies    

class ImperiumCard(Card):
    all = []

    def __init__(self, name, factions, price, icons, on_use, on_reveal, on_aquire = {}, copies = 1):
        super().__init__(name, factions, price, icons, on_use, on_reveal)
        self.on_aquire = on_aquire
    
# Decks
class StartingDeck(Deck):
    def __init__(self) -> None:
        super().__init__(StartingCard.all[:])

class ImperiumDeck(Deck):
    def __init__(self) -> None:
        super().__init__(ImperiumDeck.all[:])

class Reserve:
    def __init__(self) -> None:
        reserve = copy.deepcopy(ReserveCard.all) # must deep to change amount without changing future game amounts
        for card in reserve:
            self[card] = reserve[card]

# Adding cards.json cards
import json
cards_file = open("assets/cards.json")
all_cards = json.load(cards_file)
for starting_card in all_cards["starting"]:
    StartingCard(**starting_card)

for reserve_card in all_cards["reserve"]:
    ReserveCard(**reserve_card)

for imperium_card in all_cards["imperium"]:
    ImperiumCard(**imperium_card)
