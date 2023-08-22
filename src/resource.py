# No need for this file... for now

class Resource:
    def __init__(self, name, symbol) -> None:
        self.name = name
        self.symbol = symbol

class Persuasion(Resource):
    def __init__(self) -> None:
        super().__init__("Persuasion", "◇")

class Solaris(Resource):
    def __init__(self) -> None:
        super().__init__("Solaris", "●")
    
class Spice(Resource):
    def __init__(self) -> None:
        super().__init__("Spice", "⬣")
    
class Water(Resource):
    def __init__(self) -> None:
        super().__init__("Water", "💧")
        