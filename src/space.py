class Space:
    all = []

    def __init__(self, name, icon, cost, resources, is_combat = False, has_banner = False) -> None:
        self.name = name
        self.icon = icon
        self.cost = cost
        self.resources = resources
        self.agents = [] # use players as agents
        # Combat
        self.is_combat = is_combat
        self.has_banner = has_banner
        if has_banner:
            self.banner_owner = None
            
        Space.all.append(self)

    def occupy(self, player):
        self.agents.append(player)
    
    def reset(self):
        self.agents = []

class HarvestSpace(Space):
    def __init__(self, name, icon, cost, resources, has_banner = False) -> None:
        super().__init__(name, icon, cost, resources, True, has_banner)
        self.bonus_spice = 0
    
    def reset_bonus(self):
        self.bonus_spice = 0

class FactionSpace(Space):
    def __init__(self, name, icon, cost, resources, is_combat = False) -> None:
        super().__init__(name, icon, cost, resources, is_combat, False)

# Get spaces from json file
import json
spaces_file = open("assets/spaces.json")
all_spaces = json.load(spaces_file)

# Create Spaces
for normal_space in all_spaces["normal_spaces"]:
    Space(normal_space["name"], normal_space["icon"], normal_space["cost"], normal_space["resources"], "is_combat" in normal_space, "has_banner" in normal_space)

for harvest_space in all_spaces["harvest_spaces"]:
    HarvestSpace(harvest_space["name"], harvest_space["icon"], harvest_space["cost"], harvest_space["resources"], harvest_space["has_banner"])

for faction_space in all_spaces["faction_spaces"]:
    FactionSpace(faction_space["name"], faction_space["icon"], faction_space["cost"], faction_space["resources"], "is_combat" in faction_space)



class Board:
    def __init__(self, spaces_list = Space.all) -> None:
        self.spaces_list = spaces_list[:],
        self.spaces = {
            "City": [],
            "Spice Trade": [],
            "Landsraad": [],
            "Fremen": [],
            "Bene Gesserit": [],
            "Spacing Guild": [],
            "Emperor": []
        }

        for board_space in self.spaces_list:
            self.spaces[board_space.icon].append(board_space)
    