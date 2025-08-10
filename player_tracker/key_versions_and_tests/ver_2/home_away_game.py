from game import Game

class HomeGame(Game):
    def __init__(self, game_id, opposition_, minutes_played_, 
                 steals_=0, blocks_=0, turnovers_=0, assists_=0, rebounds_=0, 
                 fouls_=0, TwoPM_=0, TwoPA_=0, ThreePM_=0, 
                 ThreePA_=0, FTM_=0, FTA_=0, pace=120):
        super().__init__(game_id, opposition_, minutes_played_, 
                         steals_, blocks_, turnovers_, assists_, rebounds_, 
                         fouls_, TwoPM_, TwoPA_, ThreePM_, 
                         ThreePA_, FTM_, FTA_, pace)
        
        print(
            f"Key stats at home against {self.opps} are: "
            f"{self._stl} steals, {self._blk} blocks, {self._to} turnovers, "
            f"{self._ast} assists, {self._reb} rebounds, {self._fouls} fouls, "
            f"{self._two_pm} two_pointers, {self._three_pm} three_pointers, "
            f"{self._ftm} free_throws, {self._fta} free_throw_attempts, "
            f"{self._three_pa} three_point_attempts, {self._two_pa} two_point_attempts, "
            f"{self.pace} pace (poss per 40 mins)")

    def __repr__(self):
        return f"Game {self.game_id} at home against against {self.opps}. Key stats are: {self.calc_points()} points, {self.three_point_percentage()*100}% from 3pt range, {self.ts_percentage()*100}% true shooting. "

    def __del__(self):
        print(f"Home game {self.game_id} against {self.opps} has been deleted.")

class AwayGame(Game):
    def __init__(self, game_id, opposition_, minutes_played_,
                 steals_=0, blocks_=0, turnovers_=0, assists_=0, rebounds_=0,
                 fouls_=0, TwoPM_=0, TwoPA_=0, ThreePM_=0,
                 ThreePA_=0, FTM_=0, FTA_=0, pace=120):
        super().__init__(game_id, opposition_, minutes_played_,
                         steals_, blocks_, turnovers_, assists_, rebounds_,
                         fouls_, TwoPM_, TwoPA_, ThreePM_,
                         ThreePA_, FTM_, FTA_, pace)

        print(
            f"Key stats at away against {self.opps} are: "
            f"{self._stl} steals, {self._blk} blocks, {self._to} turnovers, "
            f"{self._ast} assists, {self._reb} rebounds, {self._fouls} fouls, "
            f"{self._two_pm} two_pointers, {self._three_pm} three_pointers, "
            f"{self._ftm} free_throws, {self._fta} free_throw_attempts, "
            f"{self._three_pa} three_point_attempts, {self._two_pa} two_point_attempts, "
            f"{self.pace} pace (poss per 40 mins)")

    def __repr__(self):
        return f"Game {self.game_id} away against {self.opps}. Key stats are: {self.calc_points()} points, {self.three_point_percentage()*100}% from 3pt range, {self.ts_percentage()*100}% true shooting. "

    def __del__(self):
        print(f"Away game {self.game_id} against {self.opps} has been deleted.")