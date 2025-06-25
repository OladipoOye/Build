# This is a project aimed at tracking player performance in a game/season
# The code is structured to allow for easy modification for different players
# There will be a game class, player class and a team class

#import numpy as np

# The game class will contain the game information for a player in a single game

class Game:
    def __init__(self, game_id, away_team, minutes_played, pace=0, 
                 steals=0, blocks=0, turnovers=0, assists=0, rebounds=0, 
                 fouls=0, TwoPM=0, TwoPA=0, ThreePM=0, 
                 ThreePA=0, FTM=0, FTA=0):
        # Initialize the game with its ID, date, and opposing team
        self.game_id = game_id
        self.opps = away_team
        self.mins = minutes_played
        # Initialize the performance stats for the game
        # All stats default to 0 unless specified
        self.steals = steals
        self.BLKS = blocks
        self.TO = turnovers
        self.AST = assists
        self.REB = rebounds
        self.fouls = fouls
        self.two_PM = TwoPM
        self.two_PA = TwoPA
        self.three_PM = ThreePM
        self.three_PA = ThreePA
        self.FTM = FTM
        self.FTA = FTA

        # The pace of the game is not used in calculations but can be used for 
        # This refers to the number of possessions per game, which can be used to adjust stats
        # Each game is 40 minutes long, so the pace is calculated as possessions per 40 minutes
        self.pace = pace

        # Validate the input data
        if self.mins < 0:
            raise ValueError("Minutes played cannot be negative")
        if self.two_PM < 0 or self.two_PA < 0 or self.three_PM < 0 or self.three_PA < 0:
            raise ValueError("Field goal stats cannot be negative")
        if self.FTM < 0 or self.FTA < 0:
            raise ValueError("Free throw stats cannot be negative")
        if self.steals < 0 or self.BLKS < 0 or self.TO < 0 or self.AST < 0 or self.REB < 0:
            raise ValueError("Performance stats cannot be negative")
        if self.fouls < 0:
            raise ValueError("Fouls cannot be negative")
        if self.two_PA < self.two_PM:
            raise ValueError("Two-point field goals made cannot exceed attempts")
        if self.three_PA < self.three_PM:
            raise ValueError("Three-point field goals made cannot exceed attempts")
        if self.FTA < self.FTM:
            raise ValueError("Free throws made cannot exceed attempts")
        if self.game_id is None or self.opps is None:
            raise ValueError("Game ID, date, and opposing team cannot be None")
        if type(self.game_id) is not str:
            raise TypeError("Game ID must be a string")
        if type(self.opps) is not str:
            raise TypeError("Opponent team name must be a string")
        if self.pace < 0:
            raise ValueError("Pace cannot be negative")
        

    def calc_points(self):
        # Calculate the total points scored in the game
        points = (self.two_PM * 2) + (self.three_PM * 3) + self.FTM
        return points

    def triple_double(self):
        # Check if the player achieved a triple-double in the game
        stats = [self.AST, self.REB, self.steals, self.BLKS, self.TO]
        return sum(stat >= 10 for stat in stats) >= 3
    
    def FGA(self):
        # Calculate the total field goal attempts
        return self.two_PA + self.three_PA
    
    def ts_percentage(self):
        # Calculate the true shooting percentage
        points = self.calc_points()
        return points / (2 * (self.FGA() + 0.44*self.FTA))
    
    def three_point_percentage(self):
        # Calculate the three-point shooting percentage
        if self.ThreePA == 0:
            return 0
        return self.three_PM / self.three_PA
    
    def key_stats(self):
        # Return a dictionary of key stats for the game
        # The key stats will be the input used to calculate the player's performance, and Box Plus/Minus
        # The stats will be returned in a dictionary format
        return {
            # The first 10 stats are the key stats used to calculate the player's BPM
            #The next 5 stats are the key stats used to calculate the player's performance
            "Points": self.calc_points(),
            "3PM": self.three_PM,
            "Assists": self.AST,
            "Turnovers": self.TO,
            "Rebounds": self.REB,
            "Steals": self.steals,
            "Blocks": self.BLKS,
            "Fouls": self.fouls,
            "Field Goal Attempts": self.FGA(),
            "Free throw Attempts": self.FTA,
            "Two-Point FG%": self.two_PM / self.two_PA if self.two_PA > 0 else 0,
            "Three-Point FG%": self.three_point_percentage(),
            "Free Throw%": self.FTM / self.FTA if self.FTA > 0 else 0,
            "True Shooting%": self.ts_percentage()
        }

    def __str__(self):
        # String representation of the game stats
        return (f"Game ID: {self.game_id}, Opponent: {self.opps}, Minutes Played: {self.mins}\n"
                f"Points: {self.calc_points()}, Assists: {self.AST}, Rebounds: {self.REB}, "
                f"Steals: {self.steals}, Blocks: {self.BLKS}, Turnovers: {self.TO}, Fouls: {self.fouls}\n"
                f"Two-Point FG%: {self.two_PM}/{self.two_PA}, Three-Point FG%: {self.three_PM}/{self.three_PA}, "
                f"Free Throw%: {self.FTM}/{self.FTA}, True Shooting%: {self.ts_percentage():.2f}")