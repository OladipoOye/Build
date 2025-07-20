# The Team class will contain the team information for a team in a season
# It will include methods to calculate various statistics and track performance, based on the players in the team

from season_player import SeasonPlayer

class Team:
    def __init__(self, team_name, year=None, league=None, scores=[]):
        # Initialize the team with its name
        self.team_name = team_name
        self.players = []
        self.year = year
        self.league = league

        # The scores will be a list of game scores, with the representative team always first, and the opponents second
        # eg, [[28, 12], [40, 35], [22, 30]]
        self.scores = scores

        # Validate the input data
        if self.team_name is None:
            raise ValueError("Team name cannot be None")
        if type(self.team_name) is not str:
            raise TypeError("Team name must be a string")
        if self.year is not None and type(self.year) is not int:
            raise TypeError("Year must be an integer or None")
        if self.league is not None and type(self.league) is not str:
            raise TypeError("League must be a string")
        
    def add_player(self, player):
        # Add a player to the team
        self.players.append(player)
        # Validate that the player is an instance of the SeasonPlayer class
        if not isinstance(player, SeasonPlayer):
            raise TypeError("Player must be an instance of the SeasonPlayer class")
    
    def total_points(self):
        # Calculate the total points scored by all players in the team
        return sum(player.total_points() for player in self.players)
    
    def total_assists(self):
        # Calculate the total assists made by all players in the team
        return sum(player.total_assists() for player in self.players)
    
    def total_rebounds(self):
        # Calculate the total rebounds made by all players in the team
        return sum(player.total_rebounds() for player in self.players)
    
    def total_steals(self):
        # Calculate the total steals made by all players in the team
        return sum(player.total_steals() for player in self.players)
    
    def total_blocks(self):
        # Calculate the total blocks made by all players in the team
        return sum(player.total_blocks() for player in self.players)
    
    def total_turnovers(self):
        # Calculate the total turnovers made by all players in the team
        return sum(player.total_turnovers() for player in self.players)
    
    def total_fouls(self):
        # Calculate the total fouls made by all players in the team
        return sum(player.total_fouls() for player in self.players)
    
    # Calculate the team average metrics per game

    def average_points(self):
        # Calculate the average points scored by the team per game
        if len(self.scores) == 0:
            return 0
        return self.total_points() / len(self.scores)

    def average_assists(self):
        # Calculate the average assists made by the team per game
        if len(self.scores) == 0:
            return 0
        return self.total_assists() / len(self.scores)

    def average_rebounds(self):
        # Calculate the average rebounds made by the team per game
        if len(self.scores) == 0:
            return 0
        return self.total_rebounds() / len(self.scores)

    def average_steals(self):
        # Calculate the average steals made by the team per game
        if len(self.scores) == 0:
            return 0
        return self.total_steals() / len(self.scores)

    def average_blocks(self):
        # Calculate the average blocks made by the team per game
        if len(self.scores) == 0:
            return 0
        return self.total_blocks() / len(self.scores)

    def average_turnovers(self):
        # Calculate the average turnovers made by the team per game
        if len(self.scores) == 0:
            return 0
        return self.total_turnovers() / len(self.scores)

    def average_fouls(self):
        # Calculate the average fouls made by the team per game
        if len(self.scores) == 0:
            return 0
        return self.total_fouls() / len(self.scores)

    def team_field_goal_percentage(self):
        # Calculate the total field goal percentage of the team
        total_fga = sum((player.total_field_goal_attempts() - player.total_three_point_field_goal_attempts()) for player in self.players)
        total_fg_made = sum(player.total_two_point_field_goals() + player.total_three_point_field_goals() for player in self.players)
        if total_fga == 0:
            return 0
        return total_fg_made / total_fga
    
    def team_three_point_percentage(self):
        # Calculate the total 3 point percentage of the team
        total_3pa = sum(player.total_three_point_field_goal_attempts() for player in self.players)
        total_3pm = sum(player.total_three_point_field_goals() for player in self.players)
        if total_3pa == 0:
            return 0
        return total_3pm / total_3pa
    
    def team_free_throw_percentage(self):
        # Calculate the total free throw percentage of the team
        total_fta = sum(player.total_free_throw_attempts() for player in self.players)
        total_ftm = sum(player.total_free_throw_makes() for player in self.players)
        if total_fta == 0:
            return 0
        return total_ftm / total_fta
    
    # Calculate the team's average three point and free throw makes per game

    def average_three_point_makes(self):
        # Calculate the average three-point makes per game for the team
        if len(self.scores) == 0:
            return 0
        total_3pm = sum(player.total_three_point_field_goals() for player in self.players)
        return total_3pm / len(self.scores)
    
    def average_free_throw_makes(self):
        # Calculate the average free throw makes per game for the team
        if len(self.scores) == 0:
            return 0
        total_ftm = sum(player.total_free_throw_makes() for player in self.players)
        return total_ftm / len(self.scores)

    # Calculate the team's average free throw and three point attempts per game

    def average_three_point_attempts(self):
        # Calculate the average three-point attempts per game for the team
        if len(self.scores) == 0:
            return 0
        total_3pa = sum(player.total_three_point_field_goal_attempts() for player in self.players)
        return total_3pa / len(self.scores)

    def average_free_throw_attempts(self):
        # Calculate the average free throw attempts per game for the team
        if len(self.scores) == 0:
            return 0
        total_fta = sum(player.total_free_throw_attempts() for player in self.players)
        return total_fta / len(self.scores)
    
    # Calculate the team's average points scored and condeded per game, along with the win/loss record

    def average_points_scored(self):
        # Calculate the average points scored by the team per game
        if len(self.scores) == 0:
            return 0
        return sum(score[0] for score in self.scores) / len(self.scores)

    def average_points_conceded(self):
        # Calculate the average points conceded by the team per game
        if len(self.scores) == 0:
            return 0
        return sum(score[1] for score in self.scores) / len(self.scores)

    def win_loss_record(self):
        # Calculate the team's win/loss record
        if len(self.scores) == 0:
            return (0, 0)
        wins = sum(1 for score in self.scores if score[0] > score[1])
        losses = sum(1 for score in self.scores if score[0] < score[1])
        return (wins, losses)

    def __str__(self):
        return f"Team {self.name}: {self.win_loss_record()[0]}-{self.win_loss_record()[1]}"