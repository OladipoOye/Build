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