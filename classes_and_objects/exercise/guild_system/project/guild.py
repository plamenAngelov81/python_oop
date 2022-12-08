class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        # for member in self.players:
        #     if member.name == player.name:
        #         return f"Player {player.name} is already in the guild."
        # if player in self.players:
        #     return f"Player {player.name} is already in the guild."
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_to_remove):
        for member in self.players:
            if member.name == player_to_remove:  # guy's name is in list
                self.players.remove(member)
                member.guild = "Unaffiliated"
                return f"Player {member.name} has been removed from the guild."

        # else -> if not found in names
        return f"Player {player_to_remove} is not in the guild."

    def guild_info(self):
        info = f"Guild: {self.name}"
        for member in self.players:
            info += f"\n{member.player_info()}"
        return info
