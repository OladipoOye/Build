# The second version of the team class
# This will implement a game id list to track all games played by the team
# The team class will now include a dictionary of the players, and their positions

# The Team class will contain the team information for a team in a season
# It will include methods to calculate various statistics and track performance, based on the players in the team

from season_player import SeasonPlayer

class Team:
    def __init__(self, team_name, scores=None, year=2024, league=None):
        # Initialize the team with its name
        self.team_name = team_name
        self._playerseasons = []
        self._game_list = []
        self._players_dict = {}
        self._year = year
        self._league = league

        # The scores will be a list of game scores, with the representative team always first, and the opponents second
        # eg, [[28, 12], [40, 35], [22, 30]]
        self.scores = scores

        # Validate the input data
        if self.team_name is None:
            raise ValueError("Team name cannot be None")
        if type(self.team_name) is not str:
            raise TypeError("Team name must be a string")
        if self._year is not None and type(self._year) is not int:
            raise TypeError("Year must be an integer or None")
        if self._league is not None and type(self._league) is not str:
            raise TypeError("League must be a string")
        
    def add_player(self, player):
        # Validate that the player is an instance of the SeasonPlayer class
        if not isinstance(player, SeasonPlayer):
            raise TypeError("Player must be an instance of the SeasonPlayer class")
        elif player.year != self._year:
            raise ValueError(f"Player's year {player.year} does not match team's year {self._year}")
        
        # Add a player to the team
        self._playerseasons.append(player)
        # Add the player to the players dictionary, if not already present
        if player.name not in self._players_dict:
            self._players_dict[player.name] = player.position
        # Add the player's game IDs to the team's game ID list if not already present
        for game_id in player.game_ids:
            if game_id not in self._game_list:
                self._game_list.append(game_id)

    def total_points(self):
        # Calculate the total points scored by the team
        # Check if the points scored are valid
        players_points = sum(player.total_points() for player in self._playerseasons)
        if self.scores is not None and len(self.scores) > 0:
            score_points = sum(game[0] for game in self.scores)
            if players_points >= score_points:
                raise ValueError("Total points input by players exceeds team scores")
            elif len(self.scores) < len(self._game_list):
                print("Warning: Not all game scores are uploaded, using player scores as a substitute")
                return players_points
            else:
                return score_points
        else:
            return players_points

    def total_assists(self):
        # Calculate the total assists made by all players in the team
        return sum(player.total_assists() for player in self._playerseasons)

    def total_rebounds(self):
        # Calculate the total rebounds made by all players in the team
        return sum(player.total_rebounds() for player in self._playerseasons)

    def total_steals(self):
        # Calculate the total steals made by all players in the team
        return sum(player.total_steals() for player in self._playerseasons)

    def total_blocks(self):
        # Calculate the total blocks made by all players in the team
        return sum(player.total_blocks() for player in self._playerseasons)

    def total_turnovers(self):
        # Calculate the total turnovers made by all players in the team
        return sum(player.total_turnovers() for player in self._playerseasons)

    def total_fouls(self):
        # Calculate the total fouls made by all players in the team
        return sum(player.total_fouls() for player in self._playerseasons)

    # Calculate the team average metrics per game

    def team_points_per_game(self):
        # Calculate the average points scored by the team per game
        if len(self._game_list) == 0:
            return 0
        return self.total_points() / len(self._game_list)

    def team_assists_per_game(self):
        # Calculate the average assists made by the team per game
        if len(self._game_list) == 0:
            return 0
        return self.total_assists() / len(self._game_list)

    def team_rebounds_per_game(self):
        # Calculate the average rebounds made by the team per game
        if len(self._game_list) == 0:
            return 0
        return self.total_rebounds() / len(self._game_list)

    def team_steals_per_game(self):
        # Calculate the average steals made by the team per game
        if len(self._game_list) == 0:
            return 0
        return self.total_steals() / len(self._game_list)

    def team_blocks_per_game(self):
        # Calculate the average blocks made by the team per game
        if len(self._game_list) == 0:
            return 0
        return self.total_blocks() / len(self._game_list)

    def team_turnovers_per_game(self):
        # Calculate the average turnovers made by the team per game
        if len(self._game_list) == 0:
            return 0
        return self.total_turnovers() / len(self._game_list)

    def team_fouls_per_game(self):
        # Calculate the average fouls made by the team per game
        if len(self._game_list) == 0:
            return 0
        return self.total_fouls() / len(self._game_list)

    def team_field_goal_percentage(self):
        # Calculate the total field goal percentage of the team
        total_fga = sum(player.total_field_goal_attempts() for player in self._playerseasons)
        print(f"Total field goal attempts: {total_fga}")
        total_fg_made = sum(player.total_two_point_field_goals() + player.total_three_point_field_goals() for player in self._playerseasons)
        print(f"Total field goals made: {total_fg_made}")
        if total_fga == 0:
            return 0
        return total_fg_made / total_fga
    
    def team_three_point_percentage(self):
        # Calculate the total 3 point percentage of the team
        total_3pa = sum(player.total_three_point_field_goal_attempts() for player in self._playerseasons)
        total_3pm = sum(player.total_three_point_field_goals() for player in self._playerseasons)
        if total_3pa == 0:
            return 0
        return total_3pm / total_3pa
    
    def team_free_throw_percentage(self):
        # Calculate the total free throw percentage of the team
        total_fta = sum(player.total_free_throw_attempts() for player in self._playerseasons)
        total_ftm = sum(player.total_free_throw_makes() for player in self._playerseasons)
        if total_fta == 0:
            return 0
        return total_ftm / total_fta
    
    # Calculate the team's average three point and free throw makes per game

    def team_three_point_makes_per_game(self):
        # Calculate the average three-point makes per game for the team
        if len(self._game_list) == 0:
            return 0
        total_3pm = sum(player.total_three_point_field_goals() for player in self._playerseasons)
        return total_3pm / len(self._game_list)

    def team_free_throw_makes_per_game(self):
        # Calculate the average free throw makes per game for the team
        if len(self._game_list) == 0:
            return 0
        total_ftm = sum(player.total_free_throw_makes() for player in self._playerseasons)
        return total_ftm / len(self._game_list)

    # Calculate the team's average free throw and three point attempts per game

    def three_point_attempts_per_game(self):
        # Calculate the average three-point attempts per game for the team
        if len(self._game_list) == 0:
            return 0
        total_3pa = sum(player.total_three_point_field_goal_attempts() for player in self._playerseasons)
        return total_3pa / len(self._game_list)

    def average_free_throw_attempts(self):
        # Calculate the average free throw attempts per game for the team
        if len(self.scores) == 0:
            return 0
        total_fta = sum(player.total_free_throw_attempts() for player in self._playerseasons)
        return total_fta / len(self._game_list)

    # Calculate the team's average points conceded per game, along with the win/loss record
    def team_points_conceded_per_game(self):
        # Calculate the average points conceded by the team per game
        if len(self._game_list) == 0:
            return 0
        elif len(self.scores) == 0:
            return 0
        else:
            return sum(score[1] for score in self.scores) / len(self._game_list)

    def win_loss_record(self):
        # Calculate the team's win/loss record
        if len(self._game_list) == 0:
            return (0, 0)
        wins = sum(1 for score in self.scores if score[0] > score[1])
        losses = sum(1 for score in self.scores if score[0] < score[1])
        if wins + losses == 0:
            return (0, 0)
        elif wins + losses < len(self._game_list):
            print(f"Warning: Not all games accounted for in win/loss record. Current games are: {self._game_list}")
            return (wins, losses)
        return (wins, losses)

    def __str__(self):
        return f"Team {self.team_name}: {self.win_loss_record()[0]}-{self.win_loss_record()[1]} \n" \
               f"Players and positions: {self._players_dict} \n"
    
    @classmethod
    def from_players(cls, Team_name, Scores, Year, League, players):
        team = cls(team_name=Team_name, scores=Scores, year=Year, league=League)
        for player in players:
            team.add_player(player)
        return team