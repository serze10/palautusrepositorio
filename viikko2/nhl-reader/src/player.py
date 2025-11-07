class Player:
    def __init__(self, data: dict):
        self.name = data['name']
        self.nationality = data['nationality']
        self.team = data['team']
        self.goals = data['goals']
        self.assists = data['assists']

    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} team {self.team:15}  goals {self.goals} assists {self.assists}"
