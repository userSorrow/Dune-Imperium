from src.conflict import ConflictDeck, ConflictI, ConflictII, ConflictIII
from tests.test_helper import get_names

print("Conflict Is: " + get_names(ConflictI.all))
print("Conflict IIs: " + get_names(ConflictII.all))
print("Conflict IIIs: " + get_names(ConflictIII.all))

# Make Conflict Deck
conflict_deck = ConflictDeck(1, 0)
print(get_names(conflict_deck.contents))
