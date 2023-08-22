from src.leader import Leader

class Player:
    STARTING_TROOPS = 3
    def __init__(self):
        self.leader = None # use assign_leader() to assign

        # Turn
        self.revealed = False

        # Game Trackers
        self.victory_points = 0

        # Faction Influence
        self.faction_influence = {
            "Fremen": 0,
            "Bene Gesserit": 0,
            "Spacing Guild": 0,
            "Emperor": 0
        }

        # Intrigue Cards
        self.intrigues = []

        # Resources
        self.resources = {
            "solaris": 0,
            "spice": 0,
            "water": 0
        }

        # Conflict / Troops
        self.troops = {
            "garrison": Player.STARTING_TROOPS,
            "conflict": 0
        }

    def assign_leader(self, leader):
        self.leader = leader
    
    def play_card(self):
        pass

    def reveal_hand(self):
        pass

    # ... and much more