from src.card import StartingDeck, StartingCard, ReserveCard, ImperiumCard
from tests.test_helper import get_names

# Print all cards
print("Starting Cards: " + str(get_names(StartingCard.all)))
print("Reserve Cards: " + str(ReserveCard.all.keys()))
print("Imperium Deck Cards: " + str(get_names(ImperiumCard.all)))

# Check if make_starting() actually creates a copy of the decks
starting1 = StartingDeck()
starting1.draw()
starting1.contents[1].name = "?" # PROBLEM: CHANGING 1 ELEMENT CHANGES ALL ELEMENTS OF SAME NAME
# But it doesn't matter because we aren't changing card properties
print(str(list(map(lambda card : card.name, starting1.contents))))
print(str(get_names(StartingCard.all)))
