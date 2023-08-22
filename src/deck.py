import copy
import random

class Deck:
    def __init__(self, contents) -> None:
        self.contents = copy.copy(contents)
        random.shuffle(self.contents)

    def is_empty(self) -> bool:
        return len(self.contents) == 0
    
    def draw(self) -> object:
        return self.contents.pop() # draw from end
    
    def draw(self, amount) -> list:
        drawn = []
        for count in range(0, amount):
            drawn.append(self.contents.pop())
        
        return drawn
