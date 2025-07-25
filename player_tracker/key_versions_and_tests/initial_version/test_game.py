from game import Game
from season_player import SeasonPlayer
from team import Team
import pytest

# Unit tests in order to check that the classes work using pytest

# Generate a dummy game
@pytest.fixture
def my_game():
    notts_away = Game(1, 'Notts', 10, pace=3, TwoPM=4, ThreePM=1, TwoPA=7, ThreePA=2, FTM=1, FTA=2)
    return notts_away

@pytest.fixture
def double_double_game():
    game2 = Game(2, 'NTU', 35, pace=3, steals=2, turnovers=6, assists=11, rebounds=9, fouls=2, TwoPM=7, ThreePM=2, TwoPA=7, ThreePA=2, FTM=1, FTA=2)
    return game2

@pytest.fixture
def triple_double_game():
    game3 = Game(2, 'Lei', 35, pace=3, steals=2, turnovers=6, assists=11, rebounds=13, fouls=2, TwoPM=7, ThreePM=2, TwoPA=7, ThreePA=2, FTM=1, FTA=2)
    return game3



# Test the points, true shooting, field goal attempts and free throw attempts


def test_calc_points_and_attempts(my_game):
    assert my_game.calc_points() == 12
    assert my_game.FGA() == 9

def test_percentages(my_game):
    points = my_game.calc_points()
    FGA = my_game.FGA()
    FTA = my_game.FTA
    assert FTA > 0
    assert FGA > 0
    assert points > 0
    assert my_game.ts_percentage() == ((0.5*points) / (FGA + 0.44*FTA))

    three_PM = my_game.three_PM
    three_PA = my_game.three_PA
    assert three_PA > three_PM
    assert my_game.three_point_percentage() == 1/2

def test_double_double(double_double_game):
    assert double_double_game.double_double() == True
    assert double_double_game.triple_double() == False

def test_triple_double(triple_double_game):
    assert triple_double_game.double_double() == False
    assert triple_double_game.triple_double() == True



# Takeaways 
# Game part works
# Testing the tirple/double doubles allowed me to see that I didn't include the points in the functions for the respective metrics
# Creating a home and an away extension of the game class could add a lot of simplicity
# Using inputs instead of a large intitialisation may help on the user end
# Extend the exceptions for more rigorous cases - Like playing for more than 40 minutes

# Test the game class with a season player
@pytest.fixture
def my_season_player():
    # Creat 2 dummy games
    game1 = Game(1, 'Notts', 10, pace=3, TwoPM=4, assists=11, ThreePM=1, TwoPA=7, ThreePA=2, FTM=1, FTA=2)
    game2 = Game(2, 'NTU', 35, pace=3, steals=2, turnovers=6, assists=11, rebounds=20, fouls=2, TwoPM=7, ThreePM=2, TwoPA=7, ThreePA=2, FTM=1, FTA=2)
    #Create a season player with the games
    my_season_player = SeasonPlayer('Bros', 'Guard', 'Cam')
    my_season_player.add_game(game1)
    my_season_player.add_game(game2)
    return my_season_player

# Test the season player class
def test_season_player(my_season_player):
    assert my_season_player.total_points() == (my_season_player.games[0].calc_points() + my_season_player.games[1].calc_points())
    assert my_season_player.total_FGA() == (my_season_player.games[0].FGA() + my_season_player.games[1].FGA())
    assert my_season_player.total_double_doubles() == 1
    assert my_season_player.total_triple_doubles() == 1

def test_season_player_percentages(my_season_player):
    game_1 = my_season_player.games[0]
    game_2 = my_season_player.games[1]
    total_three_pointers = (game_1.three_PM + game_2.three_PM)
    total_three_point_attempts = (game_1.three_PA + game_2.three_PA)
    assert my_season_player.total_three_point_percentage() == (total_three_pointers / total_three_point_attempts)

    total_fta = (game_1.FTA + game_2.FTA)
    total_fga = (game_1.FGA() + game_2.FGA())
    total_points = (game_1.calc_points() + game_2.calc_points())
    assert my_season_player.total_ts_percentage() == ((0.5 * total_points) / (total_fga + 0.44 * total_fta))

# Test the team class
@pytest.fixture
def my_team():
    # Create a team with 2 players
    player1 = SeasonPlayer('Bros', 'Guard', 'Cam')
    player2 = SeasonPlayer('Dude', 'Forward', 'Cam')
    
    # Create 2 dummy games for each player
    game1 = Game(1, 'Notts', 10, pace=3, TwoPM=4, assists=11, ThreePM=1, TwoPA=7, ThreePA=2, FTM=1, FTA=2)
    game2 = Game(2, 'NTU', 35, pace=3, steals=2, turnovers=6, assists=11, rebounds=20, fouls=2, TwoPM=7, ThreePM=2, TwoPA=7, ThreePA=2, FTM=1, FTA=2)
    game3 = Game(3, 'Lei', 20, pace=3, steals=1, turnovers=2, assists=5, rebounds=10, fouls=1, TwoPM=3, ThreePM=1, TwoPA=5, ThreePA=1, FTM=2, FTA=3)
    game4 = Game(4, 'Shef', 30, pace=3, steals=3, turnovers=4, assists=8, rebounds=15, fouls=3, TwoPM=5, ThreePM=2, TwoPA=6, ThreePA=3, FTM=2, FTA=4)
    
    player1.add_game(game1)
    player2.add_game(game2)
    
    team = Team('My Team',scores=[[], []])
    team.add_player(player1)
    team.add_player(player2)
    
    return team

def test_team(my_team):
    # Test the total points scored by the team, the average free throw attempts, and the win loss record