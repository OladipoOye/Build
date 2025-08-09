from game import Game
from season_player import SeasonPlayer
from team import Team
import pytest

# Unit tests in order to check that the classes work using pytest

# -------------- Fixtures for game class
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



# ------------------- Testing the points, true shooting, field goal attempts and free throw attempts


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

# ------------------- fixture for season player
@pytest.fixture
def my_season_player():
    # Create 2 dummy games
    game1 = Game(1, 'Notts', 10, pace=3, TwoPM=4, assists=11, ThreePM=1, TwoPA=7, ThreePA=2, FTM=1, FTA=2)
    game2 = Game(2, 'NTU', 35, pace=3, steals=2, turnovers=6, assists=11, rebounds=20, fouls=2, TwoPM=7, ThreePM=2, TwoPA=7, ThreePA=2, FTM=1, FTA=2)
    #Create a season player with the games
    my_season_player = SeasonPlayer('Bros', 'Guard', 'Cam')
    my_season_player.add_game(game1)
    my_season_player.add_game(game2)
    return my_season_player

# ------------------- Testing the season player class
def test_season_player(my_season_player):
    assert my_season_player.total_points() == (my_season_player.games[0].calc_points() + my_season_player.games[1].calc_points())
    assert my_season_player.total_field_goal_attempts() == (my_season_player.games[0].FGA() + my_season_player.games[1].FGA())
    assert my_season_player.double_doubles() == 1
    assert my_season_player.triple_doubles() == 1

def test_season_player_percentages(my_season_player):
    game_1 = my_season_player.games[0]
    game_2 = my_season_player.games[1]
    total_three_pointers = (game_1.three_PM + game_2.three_PM)
    total_three_point_attempts = (game_1.three_PA + game_2.three_PA)
    assert my_season_player.average_three_point_percentage() == (total_three_pointers / total_three_point_attempts)

    total_fta = (game_1.FTA + game_2.FTA)
    total_fga = (game_1.FGA() + game_2.FGA())
    total_points = (game_1.calc_points() + game_2.calc_points())
    assert my_season_player.average_true_shooting_percentage() == ((0.5 * total_points) / (total_fga + 0.44 * total_fta))

# ------------------- Testing the team class
import pytest
from game import Game
from season_player import SeasonPlayer
from team import Team

# ---------------- Fixtures ----------------

@pytest.fixture
def sample_players(my_season_player):
    # Player 1
    p1 = SeasonPlayer('Bros', 'Guard', 'Cam')
    g1 = Game(1, 'Notts', 10, TwoPM=4, ThreePM=1, TwoPA=7, ThreePA=2, FTM=1, FTA=2,
              assists=5, rebounds=6, steals=1, blocks=2, turnovers=3, fouls=2)
    g2 = Game(2, 'NTU', 20, TwoPM=7, ThreePM=2, TwoPA=10, ThreePA=5, FTM=4, FTA=6,
              assists=7, rebounds=8, steals=3, blocks=1, turnovers=2, fouls=1)
    p1.add_game(g1)
    p1.add_game(g2)

    return [p1, my_season_player]


@pytest.fixture
def my_team(sample_players):
    scores = [
        [80, 70],  # win
        [75, 90],  # loss
        [95, 95],  # draw (won't count in win/loss)
    ]
    t = Team('My Team', scores=scores, year=2024, league='Test League')
    for p in sample_players:
        t.add_player(p)
    return t


# ---------------- Constructor tests ----------------

def test_team_init_valid():
    t = Team("Test", scores=[[10, 5]], year=2025, league="A")
    assert t.team_name == "Test"
    assert t.year == 2025
    assert t.league == "A"
    assert t.scores == [[10, 5]]

# @pytest.mark.parametrize("bad_name, [[90, 10], [80, 5]]", [None, 123, [], {}])
# def test_team_init_invalid_name(bad_name):
#     if bad_name is None:
#         with pytest.raises(ValueError):
#             Team(bad_name)
#     else:
#         with pytest.raises(TypeError):
#             Team(bad_name)

def test_team_init_invalid_year():
    with pytest.raises(TypeError):
        Team("Test", year="2025")

def test_team_init_invalid_league():
    with pytest.raises(TypeError):
        Team("Test", league=123)


# ---------------- add_player tests ----------------

def test_add_player_valid(sample_players):
    t = Team("T", [])
    t.add_player(sample_players[0])
    assert len(t.players) == 1

def test_add_player_invalid_type():
    t = Team("T", [])
    with pytest.raises(TypeError):
        t.add_player("not a player")


# ---------------- total_* methods ----------------

def test_totals(my_team):
    assert my_team.total_points() == sum(p.total_points() for p in my_team.players)
    assert my_team.total_assists() == sum(p.total_assists() for p in my_team.players)
    assert my_team.total_rebounds() == sum(p.total_rebounds() for p in my_team.players)
    assert my_team.total_steals() == sum(p.total_steals() for p in my_team.players)
    assert my_team.total_blocks() == sum(p.total_blocks() for p in my_team.players)
    assert my_team.total_turnovers() == sum(p.total_turnovers() for p in my_team.players)
    assert my_team.total_fouls() == sum(p.total_fouls() for p in my_team.players)


# ---------------- average_* methods ----------------

def test_averages(my_team):
    num_games = len(my_team.scores)
    assert my_team.average_points() == my_team.total_points() / num_games
    assert my_team.average_assists() == my_team.total_assists() / num_games
    assert my_team.average_rebounds() == my_team.total_rebounds() / num_games
    assert my_team.average_steals() == my_team.total_steals() / num_games
    assert my_team.average_blocks() == my_team.total_blocks() / num_games
    assert my_team.average_turnovers() == my_team.total_turnovers() / num_games
    assert my_team.average_fouls() == my_team.total_fouls() / num_games


# ---------------- shooting percentages ----------------

def test_percentages(my_team):
    fg_pct = my_team.team_field_goal_percentage()
    assert 0 <= fg_pct <= 1
    tp_pct = my_team.team_three_point_percentage()
    assert 0 <= tp_pct <= 1
    ft_pct = my_team.team_free_throw_percentage()
    assert 0 <= ft_pct <= 1


# ---------------- scoring & win/loss ----------------

def test_scoring_and_wins(my_team):
    assert my_team.average_points_scored() == pytest.approx(
        sum(score[0] for score in my_team.scores) / len(my_team.scores)
    )
    assert my_team.average_points_conceded() == pytest.approx(
        sum(score[1] for score in my_team.scores) / len(my_team.scores)
    )
    wins, losses = my_team.win_loss_record()
    assert wins == 1
    assert losses == 1


# ---------------- edge cases ----------------

def test_no_scores():
    t = Team("Empty", scores=[])
    assert t.average_points() == 0
    assert t.win_loss_record() == (0, 0)

def test_no_players():
    t = Team("No Players", scores=[[10, 5]])
    assert t.total_points() == 0
    assert t.team_field_goal_percentage() == 0


# ---------------- string representation ----------------

def test_str_output(my_team):
    s = str(my_team)
    assert "Team" in s
    assert "-" in s


# Takeaways
# The game class contains the game id, which is unique for each game instance.
# In order to accurately count the number of games a team has played, a list of game ids should be maintained within the team class.
# Method of checking if a game is already in a player's game list was incorrect, it should check against the game id instead.
# An inconsistent naming convention was used for field goal attempts, with some being FGA, and others field_goal_attempts
# Double checking on fcn naming is key for integration
# Additional error handling is needed to verify that there aren't more scores for a team than games played