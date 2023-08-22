from src.intrigue import IntrigueCard, IntrigueDeck
from tests.test_helper import get_names

# Testing IntrigueCard
print("Intrigues: " + get_names(IntrigueCard.all))

# Check types
card_a = IntrigueCard.all[0]
card_b = IntrigueCard.all[2]
print(f"{card_a.name}: {card_a.types} card")
print(f"{card_b.name}: {card_b.types} card")

# Test IntrigueDeck()
intrigue_deck = IntrigueDeck()
print("Shuffled Intrigue Deck: " + get_names(intrigue_deck.contents))
print("Drawn Card: " + intrigue_deck.draw().name)
