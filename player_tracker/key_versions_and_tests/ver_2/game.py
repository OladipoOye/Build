# The second version of the game class
# This will implement python properties in order to manage player statistics more effectively
# The naming convention will also be updated to improve consistency between classes
# The average pace will be set to 120 possessions per 40 minutes, to normalize player stats
# Each game id will be unique, in order to track games played by players/teams

class Game:
    def __init__(self, game_id, opposition_, minutes_played_, 
                 steals_=0, blocks_=0, turnovers_=0, assists_=0, rebounds_=0, 
                 fouls_=0, TwoPM_=0, TwoPA_=0, ThreePM_=0, 
                 ThreePA_=0, FTM_=0, FTA_=0, pace=120):
        # Initialize the game with its ID, date, and opposing team
        self.game_id = game_id
        self.opps = opposition_
        self.mins = minutes_played_
        # Initialize the performance stats for the game
        # All stats default to 0 unless specified
        # Print the stats that need to be defined
        self._stl = steals_
        self._blk = blocks_
        self._to = turnovers_
        self._ast = assists_
        self._reb = rebounds_
        self._fouls = fouls_
        self._two_pm = TwoPM_
        self._two_pa = TwoPA_
        self._three_pm = ThreePM_
        self._three_pa = ThreePA_
        self._ftm = FTM_
        self._fta = FTA_

        # The pace of the game is not used in calculations but can be used for 
        # This refers to the number of possessions per game, which can be used to adjust stats
        # Each game is 40 minutes long, so the pace is calculated as possessions per 40 minutes
        self.pace = pace

        # Validate the input data
        if self.mins < 0:
            raise ValueError("Minutes played cannot be negative")
        elif self.mins > 40:
            raise ValueError("Minutes played cannot exceed 40")
        elif self.two_pm < 0 or self.two_pa < 0 or self.three_pm < 0 or self.three_pa < 0:
            raise ValueError("Field goal stats cannot be negative")
        elif self.ftm < 0 or self.fta < 0:
            raise ValueError("Free throw stats cannot be negative")
        elif self.stl < 0 or self.blk < 0 or self.to < 0 or self.ast < 0 or self.reb < 0:
            raise ValueError("Performance stats cannot be negative")
        elif self.fouls < 0:
            raise ValueError("Fouls cannot be negative")
        elif self.two_pa < self.two_pm:
            raise ValueError("Two-point field goals made cannot exceed attempts")
        elif self.three_pa < self.three_pm:
            raise ValueError("Three-point field goals made cannot exceed attempts")
        elif self.fta < self.ftm:
            raise ValueError("Free throws made cannot exceed attempts")
        elif self.game_id is None or self.opps is None:
            raise ValueError("Game ID, date, and opposing team cannot be None")
        elif type(self.game_id) is not int:
            raise TypeError("Game ID must be an integer")
        elif type(self.opps) is not str:
            raise TypeError("Opponent team name must be a string")
        elif self.pace < 0:
            raise ValueError("Pace cannot be negative")

    # Property for the steals
    @property
    def steals(self):
        return self._stl

    @steals.setter
    def steals(self, value):
        if value < 0:
            raise ValueError("Steals cannot be negative")
        elif not isinstance(value, int):
            raise TypeError("Steals must be a whole number")
        self._stl = value

    @steals.deleter
    def steals(self):
        del self._stl

    # Property for the blocks
    @property
    def blocks(self):
        return self._blk

    @blocks.setter
    def blocks(self, value):
        if value < 0:
            raise ValueError("Blocks cannot be negative")
        elif not isinstance(value, int):
            raise TypeError("Blocks must be a whole number")
        self._blk = value

    @blocks.deleter
    def blocks(self):
        del self._blk

    # Property for the turnovers
    @property
    def turnovers(self):
        return self._to
    
    @turnovers.setter
    def turnovers(self, value):
        if value < 0:
            raise ValueError("Turnovers cannot be negative")
        elif not isinstance(value, int):
            raise TypeError("Turnovers must be a whole number")
        self._to = value

    @turnovers.deleter
    def turnovers(self):
        del self._to

    # Property for the assists
    @property
    def assists(self):
        return self._ast

    @assists.setter
    def assists(self, value):
        if value < 0:
            raise ValueError("Assists cannot be negative")
        elif not isinstance(value, int):
            raise TypeError("Assists must be a whole number")
        self._ast = value

    @assists.deleter
    def assists(self):
        del self._ast

    # Property for the rebounds
    @property
    def rebounds(self):
        return self._reb

    @rebounds.setter
    def rebounds(self, value):
        if value < 0:
            raise ValueError("Rebounds cannot be negative")
        elif not isinstance(value, int):
            raise TypeError("Rebounds must be a whole number")
        self._reb = value

    @rebounds.deleter
    def rebounds(self):
        del self._reb

    # Property for the fouls
    @property
    def fouls(self):
        return self._fouls
    
    @fouls.setter
    def fouls(self, value):
        if value < 0:
            raise ValueError("Fouls cannot be negative")
        elif not isinstance(value, int):
            raise TypeError("Fouls must be a whole number")
        self._fouls = value
    
    @fouls.deleter
    def fouls(self):
        del self._fouls

    # Property for the two pointers
    @property
    def two_pointers(self):
        return [self._two_pm, self._two_pa]
    
    @two_pointers.setter
    def two_pointers(self, makes, attempts):
        if makes < 0 or attempts < 0:
            raise ValueError("Two point makes or attempts cannot be negative")
        elif not isinstance(makes, int):
            raise TypeError("2 point makes must be a whole number")
        elif not isinstance(attempts, int):
            raise TypeError("2 point attempts must be a whole number")
        self._two_pm = makes
        self._two_pa = attempts

    @two_pointers.deleter
    def two_pointers(self):
        del self._two_pm
        del self._two_pa
    
    # Property for the three pointers
    @property
    def three_pointers(self):
        return [self._three_pm, self._three_pa]
    
    @three_pointers.setter
    def two_pointers(self, makes, attempts):
        if makes < 0 or attempts < 0:
            raise ValueError("Three point makes or attempts cannot be negative")
        elif not isinstance(makes, int):
            raise TypeError("3 point makes must be a whole number")
        elif not isinstance(attempts, int):
            raise TypeError("3 point attempts must be a whole number")
        self._three_pm = makes
        self._three_pa = attempts

    @three_pointers.deleter
    def three_pointers(self):
        del self._three_pm
        del self._three_pa

    # Property for the free throws
    @property
    def free_throws(self):
        return [self._ftm, self._fta]
    
    @free_throws.setter
    def free_throws(self, makes, attempts):
        if makes < 0 or attempts < 0:
            raise ValueError("Free throw makes or attempts cannot be negative")
        elif not isinstance(makes, int):
            raise TypeError("Free throw makes must be a whole number")
        elif not isinstance(attempts, int):
            raise TypeError("Free throw attempts must be a whole number")
        self._ftm = makes
        self._fta = attempts

    @free_throws.deleter
    def free_throws(self):
        del self._ftm
        del self._fta
    
    # Property for the points
    @property
    def points(self):
        return self.calc_points()

    @points.setter
    def points(self, value):
        raise AttributeError("Cannot set points directly")


    def calc_points(self):
        # Calculate the total points scored in the game
        points = (self.two_pointers[0] * 2) + (self.three_pointers[0] * 3) + self.free_throws[0]
        return points

    def triple_double(self):
        # Check if the player achieved a triple-double in the game
        stats = [self._ast, self._reb, self._stl, self._blk, self._to, self.points]
        return sum(stat >= 10 for stat in stats) >= 3

    def double_double(self):
        # Check if the player achieved a double-double in the game
        stats = [self._ast, self._reb, self._stl, self._blk, self._to, self.points]
        # Check if the player achieved a triple-double first
        if self.triple_double():
            return False
        return sum(stat >= 10 for stat in stats) >= 2
    
    def fga(self):
        # Calculate the total field goal attempts
        return self._two_pa + self._three_pa

    def ts_percentage(self):
        # Calculate the true shooting percentage
        points = self.calc_points()
        return points / (2 * (self.fga() + 0.44*self._fta))

    def three_point_percentage(self):
        # Calculate the three-point shooting percentage
        if self._three_pa == 0:
            return 0
        return self._three_pm / self._three_pa

    def __repr__(self):
        return f"Game {self.game_id} against {self.opps}. Key stats are: {self.points} points, {self.three_point_percentage()*100}% from 3pt range, {self.ts_percentage()*100}% true shooting. "

    def __del__(self):
        print(f"Game {self.game_id} against {self.opps} has been deleted.")
        del self