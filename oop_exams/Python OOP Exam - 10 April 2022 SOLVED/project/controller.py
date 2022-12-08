from project.player import Player


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []
        self.drinks_list = []
        self.food_list = []

    def get_player_by_name(self, given_name):
        for current_player in self.players:
            if current_player.name == given_name:
                return current_player

    def find_supply_by_type(self, type_supply):
        for index in range(len(self.supplies) - 1, - 1, - 1):
            supply = self.supplies[index]
            if supply.__class__.__name__ == type_supply:
                return (index, supply)
        return (-1, None)

    def add_player(self, *players):
        add_new_players = []
        for player in players:
            if player in self.players:
                continue
            self.players.append(player)
            add_new_players.append(player.name)
        return f"Successfully added: {', '.join(add_new_players)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.get_player_by_name(player_name)
        index, supply = self.find_supply_by_type(sustenance_type)

        if sustenance_type != "Food" and sustenance_type != "Drink":
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        if supply is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        if player is None:
            return

        player.stamina = min(player.stamina + supply.energy, 100)  # Player.MAX_STAMINA
        self.supplies.pop(index)
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.get_player_by_name(first_player_name)
        second_player = self.get_player_by_name(second_player_name)
        duel_player_list = [first_player, second_player]
        result = ""
        for j in range(len(duel_player_list)):
            if duel_player_list[j].stamina == 0:
                result += f"Player {duel_player_list[j].name} does not have enough stamina.\n"
        if result:
            return result.strip()

        if second_player.stamina < first_player.stamina:
            first_player, second_player = second_player, first_player

        first_player_damage = first_player.stamina / 2
        second_player.stamina = max(second_player.stamina - first_player_damage, 0)
        if second_player.stamina == 0:
            return f"Winner: {first_player.name}"

        second_player_damage = second_player.stamina / 2
        first_player.stamina = max(first_player.stamina - second_player_damage, 0)
        if first_player.stamina == 0:
            return f"Winner: {second_player.name}"

        winner = first_player if first_player.stamina > second_player.stamina else second_player
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ""
        for player in self.players:
            result += str(player) + "\n"

        for supply in self.supplies:
            result += supply.details() + "\n"

        return result.strip()



