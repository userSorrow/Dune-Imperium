from src.deck import Deck

class IntrigueDeck(Deck):
    def __init__(self, *list_of_intrigues) -> None:
        # Default list = IntrigueCard.all
        self.intrigues = list_of_intrigues if len(list_of_intrigues) > 0 else IntrigueCard.all
        super().__init__(self.intrigues)

class IntrigueCard:
    all = []

    def __init__(self, **kwargs) -> None:
        self.name = kwargs["name"]
        self.choose = kwargs["CHOOSE"] if "CHOOSE" in kwargs else 1 # change 1 to None to symbolize 1 effect?
        self.effects = [IntrigueEffect(effect["type"], effect["use"]) for effect in kwargs["effects"]]
        self.types = [effect.type for effect in self.effects]
        ### PROBLEM: CORNER THE MARKET IS ENDGAME AND ENDGAME AND ALSO NOT 1 CHOICE
        IntrigueCard.all.append(self)

class IntrigueEffect:
    def __init__(self, type, use) -> None:
        self.type = type
        self.use = use

# Adding intrigues.json cards
import json
intrigues_file = open("assets/intrigues.json")
all_intrigues = json.load(intrigues_file)["intrigues"]
for intrigue in all_intrigues:
    IntrigueCard(**intrigue)