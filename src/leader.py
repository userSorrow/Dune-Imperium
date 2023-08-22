# CURRENTLY NOT USING leaders.json

# Must have to code resource gains, mechanics, etc 
# due to the niche effects of SOME characters

class Ability: 
    def __init__(self, leader, name, desc):
        self.leader = leader
        self.name = name
        self.desc = desc

# LATER
class PassiveAbility:
    def __init__(self) -> None:
        pass

# LATER
class GainAbility(Ability):
    def __init__(self, leader, name, desc, items_gained):
        super().__init__(leader, name, desc)
        self.items_gained = items_gained

class SignetAbility(Ability):
    def __init__(self, leader, name, desc):
        super().__init__(leader, name, desc)
    
    def use(self, player):
        pass

class Leader:
    def __init__(self, name, house, ability, signet_ability):
        self.name = name
        self.house = house
        self.ability = ability
        self.signet_ability = signet_ability

    def on_start(self, player):
        pass

class TheBeast(Leader):
    def __init__(self):
        ability = Ability("Arrakis Fiefdom", "You start the game with additional resources: 1 SPICE and 1 SOLARIS")
        signet_ability = Ability("Brutality", "1 TROOP or 2 TROOPS if you have at least one Faction Alliance")
        super().__init__(
            'Glossu "The Beast" Rabban', 
            "Harkonnen",
            ability,
            signet_ability)
        
    def on_start(self, player):
        player.gain_resources()
    
    def use_signet(self, player):
        if len(player.faction_alliances) >= 1:
            player.gain_troops(2)
        else:
            player.gain_troops(1)
        