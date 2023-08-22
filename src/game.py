import random
from src.card import ImperiumDeck, Reserve
from src.conflict import ConflictDeck
from src.intrigue import IntrigueDeck
from src.space import Board

class Game:
    # This class will contain the imperium row, non imperium row cards, intrigue deck
    # board spaces, conflict zone.
    def __init__(self, players) -> None:
        # Players and Turns
        self.players = players
        self.first_player_token_index = 0
        self.players_revealed = 0
        self.round = 0

        # Board
        self.board = Board()

        # Factions
        self.alliances = {
            "Fremen": None,
            "Bene Gesserit": None,
            "Spacing Guild": None,
            "Emperor": None
        }

        # Cards
        self.reserve = Reserve()
        self.imperium_deck = ImperiumDeck()
        self.imperium_row = self.imperium_deck.draw(5)

        # Conflicts
        self.conflict_deck = ConflictDeck()
        self.current_conflict = None

        # Intrigues
        self.intrigue_deck = IntrigueDeck()

    def start(self):
        # Create player orders
        random.shuffle(self.players)
        self.display_player_orders()
        # Make players choose leaders
        for player in reversed(self.players):
            player.leader = self.prompt_leader(player)
        
        # Play Game
        while True: # CHANGE CONDITION LATER
            self.start_round()
            self.start_combat()
            self.resolve_combat()
            self.recall()

        # APPLY BONUSES/ENDGAME INTRIGUES

        # DETERMINE WINNER
    
    def start_round(self):
        self.players_revealed = 0 # reset
        self.round += 1
        turn_number = 0
        while not self.all_players_revealed():
            current_player = self.get_current_player(turn_number)
            self.start_turn(current_player)
            turn_number += 1
    
    def start_turn(self, player):
        # MANAGE PLAYER MECHANICS
        self.prompt_player_turn(player) 

    def start_combat(self):
        # Players play combat intrigues
        turn_number = 0
        num_players_passed = 0
        while num_players_passed < len(self.players):
            # not all players have passed
            current_player = self.get_current_player(turn_number)
            player_passed = self.prompt_combat_intrigues(current_player)
            if player_passed:
                num_players_passed += 1
            else:
                # everyone else except current player can play any intrigues
                num_players_passed = 1
        
    def resolve_combat(self):
        # Give combat rewards to players
        # Remove conflict troops and combat strengths
        pass

    def recall(self):
        pass



    def all_players_revealed(self):
        return self.players_revealed < len(self.players)

    def get_current_player(self, turn_number):
        curr_player_ind = (self.first_player_token_index + turn_number) % len(self.players)
        current_player = self.players[curr_player_ind]
        return current_player

    # UNIMPLEMENTED USER INTERFACE METHODS BELOW


    # Game Start - Leader and Player Order
    def display_player_orders(self):
        pass

    def prompt_player_leaders(self, player):
        pass

    # Player Turns
    def prompt_player_turn(self, player):
        pass

    # Combat