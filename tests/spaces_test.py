# Tests the Spaces classes and json
from src.space import Space

for space in Space.all:
    print(space.name)