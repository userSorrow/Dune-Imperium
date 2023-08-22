#!/bin/bash -ex

# Spaces
echo "TESTING space.py"
python3 -m tests.spaces_test
echo

# Conflicts
echo "TESTING conflict.py"
python3 -m tests.conflicts_test
echo

# Cards
echo "TESTING card.py"
python3 -m tests.cards_test
echo

# Intrigues
echo "TESTING intrigue.py"
python3 -m tests.intrigues_test
echo