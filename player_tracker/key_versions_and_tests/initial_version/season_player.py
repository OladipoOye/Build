# The SeasonPlayer class will contain the player information for a player in a season
# It will include methods to calculate various statistics and track performance, based on the games played

from game import Game

class SeasonPlayer:
    def __init__(self, name, position, team):
        # Initialize the player with their name, position, and team
        self.name = name
        self.position = position
        self.team = team
        self.games = []
        self.bpm_list = []

        # Validate the input data
        if self.player_id is None or self.name is None or self.position is None or self.team is None:
            raise ValueError("Player ID, name, position, and team cannot be None")
        if type(self.position) is not str or type(self.team) is not str:
            raise TypeError("Position and team must be strings")
        if self.position not in ["Guard", "Wing", "Big"]:
            raise ValueError("Position must be one of 'Guard', 'Wing', 'Big'")
        
    def add_game(self, game):
        self.games.append(game)
        # Validate that the game is an instance of the Game class
        if not isinstance(game, Game):
            raise TypeError("Game must be an instance of the Game class")
        # Validate that the game is not already in the player's game list
        if game in self.games:
            raise ValueError("Game already exists in the player's game list")

    def total_points(self):
        # Calculate the total points scored by the player in the season
        return sum(game.calc_points() for game in self.games)
    
    def total_assists(self):
        # Calculate the total assists made by the player in the season
        return sum(game.AST for game in self.games)
    
    def total_rebounds(self):
        # Calculate the total rebounds made by the player in the season
        return sum(game.REB for game in self.games)
    
    def total_steals(self):
        # Calculate the total steals made by the player in the season
        return sum(game.STL for game in self.games)
    
    def total_blocks(self):
        # Calculate the total blocks made by the player in the season
        return sum(game.BLK for game in self.games)
    
    def total_turnovers(self):
        # Calculate the total turnovers made by the player in the season
        return sum(game.TO for game in self.games)
    
    def total_fouls(self):
        # Calculate the total fouls made by the player in the season
        return sum(game.fouls for game in self.games)
    
    def total_field_goal_attempts(self):
        # Calculate the total field goal attempts made by the player in the season
        return sum(game.FGA() for game in self.games)
    
    def total_free_throw_attempts(self):
        # Calculate the total free throw attempts made by the player in the season
        return sum(game.FTA for game in self.games)
    
    def total_two_point_field_goals(self):
        # Calculate the total two-point field goals made by the player in the season
        return sum(game.two_PM for game in self.games)
    
    def total_three_point_field_goal_attempts(self):
        # Calculate the total three-point field goal attempts made by the player in the season
        return sum(game.three_PA for game in self.games)
    
    def total_three_point_field_goals(self):
        # Calculate the total three-point field goals made by the player in the season
        return sum(game.three_PM for game in self.games)
    
    def total_free_throw_makes(self):
        # Calculate the total free throws made by the player in the season
        return sum(game.FTM for game in self.games)
    
    def triple_doubles(self):
        # Calculate the total number of triple-doubles achieved by the player in the season
        return sum(1 for game in self.games if game.triple_double())

    def double_doubles(self):
        # Calculate the total number of double-doubles achieved by the player in the season
        return sum(1 for game in self.games if game.double_double())

    def total_games(self):
        # Calculate the total number of games played by the player in the season
        # This is simply the length of the games list unless 0 minutes were played
        return sum(1 for game in self.games if game.mins > 0)
    
    def games_missed(self):
        return sum(1 for game in self.games if game.mins == 0)
    
    # Calculate the player's average metrics per game

    def average_points(self):
        # Calculate the average points scored by the player per game
        if self.total_games() <= 0:
            return 0
        return self.total_points() / self.total_games()
    
    def average_assists(self):
        # Calculate the average assists made by the player per game
        if self.total_games() <= 0:
            return 0
        return self.total_assists() / self.total_games()
    
    def average_rebounds(self):
        # Calculate the average rebounds made by the player per game
        if self.total_games() <= 0:
            return 0
        return self.total_rebounds() / self.total_games()
    
    def average_steals(self):
        # Calculate the average steals made by the player per game
        if self.total_games() <= 0:
            return 0
        return self.total_steals() / self.total_games()
    
    def average_blocks(self):
        # Calculate the average blocks made by the player per game
        if self.total_games() <= 0:
            return 0
        return self.total_blocks() / self.total_games()
    
    def average_turnovers(self):
        # Calculate the average turnovers made by the player per game
        if self.total_games() <= 0:
            return 0
        return self.total_turnovers() / self.total_games()
    
    def average_fouls(self):
        # Calculate the average fouls made by the player per game
        if self.total_games() <= 0:
            return 0
        return self.total_fouls() / self.total_games()
    
    def average_field_goal_attempts(self):
        # Calculate the average field goal attempts made by the player per game
        if self.total_games() <= 0:
            return 0
        return self.total_field_goal_attempts() / self.total_games()
    
    def average_free_throw_attempts(self):
        # Calculate the average free throw attempts made by the player per game
        if self.total_games() <= 0:
            return 0
        return self.total_free_throw_attempts() / self.total_games()
    
    def average_two_point_field_goals(self):
        # Calculate the average two-point field goals made by the player per game
        if self.total_games() <= 0:
            return 0
        return self.total_two_point_field_goals() / self.total_games()
    
    # Define the percentage metrics for the player
    
    def average_three_point_percentage(self):
        # Calculate the average three-point percentage made by the player per game
        if self.total_games() <= 0:
            return 0
        return self.total_three_point_field_goals() / self.total_field_goal_attempts() if self.total_field_goal_attempts() > 0 else 0
    
    def average_free_throw_percentage(self):
        # Calculate the average free throw percentage made by the player per game
        if self.total_games() <= 0:
            return 0
        return self.total_free_throw_makes() / self.total_free_throw_attempts() if self.total_free_throw_attempts() > 0 else 0
    
    def average_true_shooting_percentage(self):
        # Calculate the average true shooting percentage made by the player per game
        if self.total_games() <= 0:
            return 0
        points = self.total_points()
        fga = self.total_field_goal_attempts()
        fta = self.total_free_throw_attempts()
        return points / (2 * (fga + 0.44 * fta)) if (fga + 0.44 * fta) > 0 else 0
    
    # The box plus minus will be modeled based on my tests/analysis of the position dependant variation of key metrics
    # It will first contain a list of the box plus minus values for each game
    # Then it will calculate an average BPM for the player based on the games played

    # This is a simplified version of Box Plus/Minus (BPM) weighting
    # Points, turnovers and fouls are constant across all positions
    # Assists are worth more for bigs and wings, less for guards
    # Rebounds are worth more for guards and wings, less for bigs
    # Steals and blocks are worth more for guards, less for wings and bigs
    # Field goal and free throw attempts are more costly for bigs, then wings, then guards
    
    
    # Hence in the order of importance for BPM:(Pts, 3PM, AST, TO, REB, STL, BLK, PF, FGA, FTA)
    # Guards = [0.8, 0.6, 0.7, -0.5, 0.6, 0.3, 1.3, -0.3, -0.2, -0.1]
    # Wings  = [0.8, 0.6, 0.9, -0.5, 0.3, 0.2, 1.1, -0.3, -0.3, -0.2]
    # Bigs   = [0.8, 0.6, 1.2, -0.5, 0.2, 0.2, 1.0, -0.3, -0.4, -0.2]

    def average_box_plus_minus(self):
        # Calculate the Box Plus/Minus (BPM) for the player
        # BPM is a measure of a player's impact on the game, adjusted for team performance
        # This is a simplified version and can be adjusted based on more complex metrics
        for game in self.games:
            if game.mins > 0:
                if self.position == "Guard":
                    bpm = (game.calc_points() * 0.8 + 
                           game.three_PM * 0.6 + 
                           game.AST * 0.7 - 
                           game.TO * 0.5 + 
                           game.REB * 0.6 + 
                           game.steals * 0.3 + 
                           game.BLKS * 1.3 - 
                           game.fouls * 0.3 - 
                           game.FGA() * 0.2 - 
                           game.FTA * 0.1)
                elif self.position == "Wing":
                    bpm = (game.calc_points() * 0.8 + 
                           game.three_PM * 0.6 + 
                           game.AST * 0.9 - 
                           game.TO * 0.5 + 
                           game.REB * 0.3 + 
                           game.steals * 0.2 + 
                           game.BLKS * 1.1 - 
                           game.fouls * 0.3 - 
                           game.FGA() * 0.3 - 
                           game.FTA * 0.2)
                elif self.position == "Big":
                    bpm = (game.calc_points() * 0.8 + 
                           game.three_PM * 0.6 + 
                           game.AST * 1.2 - 
                           game.TO * 0.5 + 
                           game.REB * 0.2 + 
                           game.steals * 0.2 + 
                           game.BLKS * 1.0 - 
                           game.fouls * 0.3 - 
                           game.FGA() * 0.4 - 
                           game.FTA * 0.2)
                else:
                    raise ValueError("Position must be one of 'Guard', 'Wing', 'Big'")
                
                # The BPM is a per 100 possessions metric, so we need to adjust it based on the pace of the game
                if (game.pace):
                    bpm *= (100 / (game.pace * game.mins))
                else:
                    # assume a standard pace of 80 possessions per game
                    game.pace = 80
                    bpm *= (100 / (game.pace * game.mins))

                # Store the BPM for the current game
                self.bpm_list.append(bpm)

        avg = sum(i for i in self.bpm_list) / len(self.bpm_list) if self.bpm_list else 0
        return avg

    def __str__(self):
        return (f"Player: {self.name}, Position: {self.position}, Team: {self.team}\n"
                f"Total Games: {self.total_games()}, Points: {self.total_points()}, "
                f"Assists: {self.total_assists()}, Rebounds: {self.total_rebounds()}, "
                f"Steals: {self.total_steals()}, Blocks: {self.total_blocks()}, "
                f"Turnovers: {self.total_turnovers()}, Fouls: {self.total_fouls()}\n"
                f"Average Points: {self.average_points():.2f}, Average Assists: {self.average_assists():.2f}, "
                f"Average Rebounds: {self.average_rebounds():.2f}, Average Steals: {self.average_steals():.2f}, "
                f"Average Blocks: {self.average_blocks():.2f}, Average Turnovers: {self.average_turnovers():.2f}, "
                f"Average Fouls: {self.average_fouls():.2f}\n"
                f"True Shooting Percentage: {self.average_true_shooting_percentage():.2f}, "
                f"Three-Point Percentage: {self.average_three_point_percentage():.2f}, "
                f"Free Throw Percentage: {self.average_free_throw_percentage():.2f}, "
                f"Average BPM: {self.average_box_plus_minus():.2f}")