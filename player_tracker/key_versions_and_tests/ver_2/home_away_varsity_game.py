from game import Game

class HomeGame(Game):
    def __init__(self, game_id, opposition, minutes_played, 
                 steals=0, blocks=0, turnovers=0, assists=0, rebounds=0, 
                 fouls=0, TwoPM=0, TwoPA=0, ThreePM=0, 
                 ThreePA=0, FTM=0, FTA=0, pace=120):
        super().__init__(game_id, opposition, minutes_played, 
                         steals, blocks, turnovers, assists, rebounds, 
                         fouls, TwoPM, TwoPA, ThreePM, 
                         ThreePA, FTM, FTA, pace)

        print(f'Home game against {self.opps}')

    def __repr__(self, option='standard'):
        if option == 'standard':
            return f"Home game {self.game_id} away against {self.opps}. Key stats are: {self.points} points, {self.three_point_percentage()*100}% from 3pt range, {self.ts_percentage()*100}% true shooting on {self.mins} minutes played."
        elif option == 'offensive':
            return f"Home game {self.game_id} away against {self.opps}. Offensive stats are: {self.rebounds} rebounds, {self._assists} assists, {self._turnovers} turnovers, {self.calc_points()} points, {self.three_point_percentage()*100}% from 3pt range, {self.ts_percentage()*100}% true shooting"
        elif option == 'defensive':
            return f"Home game {self.game_id} away against {self.opps}. Defensive stats are: {self.steals} steals, {self.blocks} blocks, {self.fouls} fouls"
        elif option == 'percentages':
            return f"Home game {self.game_id} away against {self.opps}. Shooting percentages are: {self.three_point_percentage()*100}% from 3pt range, {self.ts_percentage()*100}% true shooting, {(self.free_throws[0]/self.free_throws[1])*100 if self.free_throws[1] != 0 else 0}% from free throw range"
        
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

        print(f'Away game against {self.opps}')

    def __repr__(self, option='standard'):
        if option == 'standard':
            return f"Away game {self.game_id} against {self.opps}. Key stats are: {self.points} points, {self.three_point_percentage()*100}% from 3pt range, {self.ts_percentage()*100}% true shooting on {self.mins} minutes played."
        elif option == 'offensive':
            return f"Away game {self.game_id} against {self.opps}. Offensive stats are: {self.rebounds} rebounds, {self._assists} assists, {self._turnovers} turnovers, {self.calc_points()} points, {self.three_point_percentage()*100}% from 3pt range, {self.ts_percentage()*100}% true shooting"
        elif option == 'defensive':
            return f"Away game {self.game_id} against {self.opps}. Defensive stats are: {self.steals} steals, {self.blocks} blocks, {self.fouls} fouls"
        elif option == 'percentages':
            return f"Away game {self.game_id} against {self.opps}. Shooting percentages are: {self.three_point_percentage()*100}% from 3pt range, {self.ts_percentage()*100}% true shooting, {(self.free_throws[0]/self.free_throws[1])*100 if self.free_throws[1] != 0 else 0}% from free throw range"

    def __del__(self):
        print(f"Away game {self.game_id} against {self.opps} has been deleted.")

class VarsityGame(Game):
    def __init__(self, game_id, opposition_, minutes_played_,
                 steals_=0, blocks_=0, turnovers_=0, assists_=0, rebounds_=0,
                 fouls_=0, TwoPM_=0, TwoPA_=0, ThreePM_=0,
                 ThreePA_=0, FTM_=0, FTA_=0, pace=120):
        super().__init__(game_id, opposition_, minutes_played_,
                         steals_, blocks_, turnovers_, assists_, rebounds_,
                         fouls_, TwoPM_, TwoPA_, ThreePM_,
                         ThreePA_, FTM_, FTA_, pace)

        print(f'Congrats on making it to the varsity match against {self.opps}! We hope you have enjoyed the journey, and came back satisfied, safe and sound.')

    def __repr__(self, option='standard'):
        if option == 'standard':
            return f"Varsity game {self.game_id} against {self.opps}. Key stats are: {self.points} points, {self.three_point_percentage()*100}% from 3pt range, {self.ts_percentage()*100}% true shooting on {self.mins} minutes played."
        elif option == 'offensive':
            return f"Varsity game {self.game_id} against {self.opps}. Offensive stats are: {self.rebounds} rebounds, {self._assists} assists, {self._turnovers} turnovers, {self.calc_points()} points, {self.three_point_percentage()*100}% from 3pt range, {self.ts_percentage()*100}% true shooting"
        elif option == 'defensive':
            return f"Varsity game {self.game_id} against {self.opps}. Defensive stats are: {self.steals} steals, {self.blocks} blocks, {self.fouls} fouls"
        elif option == 'percentages':
            return f"Varsity game {self.game_id} against {self.opps}. Shooting percentages are: {self.three_point_percentage()*100}% from 3pt range, {self.ts_percentage()*100}% true shooting, {(self.free_throws[0]/self.free_throws[1])*100 if self.free_throws[1] != 0 else 0}% from free throw range"

    def __del__(self):
        print(f"Varsity game {self.game_id} against {self.opps} has been deleted.")