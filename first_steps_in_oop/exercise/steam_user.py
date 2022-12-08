class SteamUser:
    def __init__(self, username, games):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, current_game, hours):
        if current_game in self.games:
            self.played_hours += hours
            return f"{self.username} is playing {current_game}"
        else:
            return f"{current_game} is not in library"

    def buy_game(self, add_game):
        if add_game not in self.games:
            self.games.append(add_game)
            return f"{self.username} bought {add_game}"
        else:
            return f"{add_game} is already in your library"

    def status(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"


user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())
