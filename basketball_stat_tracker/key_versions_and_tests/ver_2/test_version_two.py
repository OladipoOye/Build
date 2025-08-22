import pytest
from game import Game
from home_away_varsity_game import HomeGame, AwayGame, VarsityGame
from season_player import SeasonPlayer
from team import Team


# ---------- Fixture for the game
@pytest.fixture
def sample_game():
    """Basic valid game object."""
    return Game(
        game_id=1, opposition_="Oxford", minutes_played_=30,
        steals_=2, blocks_=1, turnovers_=3, assists_=5, rebounds_=8,
        fouls_=2, TwoPM_=4, TwoPA_=7, ThreePM_=2, ThreePA_=5, FTM_=3, FTA_=4
    )


# ---------- Initialization test
def test_valid_game_creation(sample_game):
    assert sample_game.opps == "Oxford"
    assert sample_game.points == (4*2 + 2*3 + 3)  # 17 points


@pytest.mark.parametrize("minutes", [-1, 45])
def test_invalid_minutes(minutes):
    with pytest.raises(ValueError):
        Game(1, "Oxford", minutes)


@pytest.mark.parametrize("twopm, twopa", [(3, 2), (-1, 2), (2, -1)])
def test_invalid_two_point_values(twopm, twopa):
    with pytest.raises(ValueError):
        Game(1, "Oxford", 20, TwoPM_=twopm, TwoPA_=twopa)


def test_invalid_types():
    with pytest.raises(TypeError):
        Game("not_int", "Oxford", 20)  # game_id not int
    with pytest.raises(TypeError):
        Game(1, 123, 20)  # opposition not str


# ---------- Property tests
def test_property_setters(sample_game):
    sample_game.steals = 5
    assert sample_game.steals == 5

    with pytest.raises(ValueError):
        sample_game.blocks = -2

    with pytest.raises(TypeError):
        sample_game.turnovers = 2.5


def test_two_pointer_property(sample_game):
    sample_game.two_pointers = 3, 6
    assert sample_game.two_pointers == [3, 6]


def test_free_throw_property(sample_game):
    sample_game.free_throws = 5, 6
    assert sample_game.free_throws == [5, 6]


def test_points_property(sample_game):
    assert sample_game.points == 17
    with pytest.raises(AttributeError):
        sample_game.points = 30  # Cannot set directly


# ---------- Stats tests
def test_triple_double_and_double_double():
    g = Game(2, "Oxford", 35, assists_=10, rebounds_=12, steals_=11)
    assert g.triple_double() is True
    assert g.double_double() is False  # triple double takes precedence

    g2 = Game(3, "Oxford", 35, assists_=10, rebounds_=12)
    assert g2.double_double() is True
    assert g2.triple_double() is False


def test_percentages(sample_game):
    assert pytest.approx(sample_game.three_point_percentage(), 0.01) == 2/5
    assert pytest.approx(sample_game.ts_percentage(), 0.01) == sample_game.points / (
        2 * (sample_game.fga() + 0.44 * sample_game._fta)
    )


# ---------- Derived class testing
@pytest.mark.parametrize("cls", [HomeGame, AwayGame, VarsityGame])
def test_subclasses_repr(cls):
    g = cls(10, "Oxford", 30, TwoPM_=3, TwoPA_=6, ThreePM_=1, ThreePA_=3, FTM_=2, FTA_=2)
    text = g.__repr__()
    assert isinstance(text, str)
    assert g.opps == "Oxford"
    assert str(g.game_id) in text


def test_homegame_repr_modes():
    g = HomeGame(20, "Oxford", 30, TwoPM_=2, TwoPA_=5)
    assert "Key stats" in g.__repr__("standard")
    assert "Offensive stats" in g.__repr__("offensive")
    assert "Defensive stats" in g.__repr__("defensive")
    assert "Shooting percentages" in g.__repr__("percentages")


# ---------- Deletion tests
def test_game_del_prints(capsys):
    g = Game(99, "Oxford", 20)
    del g
    out, _ = capsys.readouterr()
    assert "Game 99 against Oxford has been deleted." in out


@pytest.mark.parametrize("cls, label", [
    (HomeGame, "Home game"),
    (AwayGame, "Away game"),
    (VarsityGame, "Varsity game"),
])
def test_child_del_prints(capsys, cls, label):
    g = cls(101, "Oxford", 25)
    del g
    out, _ = capsys.readouterr()
    assert label in out
    assert "Oxford" in out

# ---------- Testing reassignments

def test_deleting_stats_affects_double_double():
    g = Game(200, "Oxford", 35, assists_=10, rebounds_=12)
    assert g.double_double() is True

    del g.rebounds  # remove rebounds entirely
    # With rebounds gone, only assists remain ≥10
    assert g.double_double() is False
    assert g.triple_double() is False


def test_deleting_stats_affects_triple_double():
    g = Game(201, "Oxford", 35, assists_=10, rebounds_=11, steals_=10)
    assert g.triple_double() is True

    del g.steals  # remove steals entirely
    # Now only assists + rebounds remain ≥10
    assert g.triple_double() is False
    assert g.double_double() is True

def test_reassign_after_deletion():
    g = Game(300, "Oxford", 30, assists_=12, rebounds_=11)
    assert g.double_double() is True

    # Delete assists and confirm it's no longer double double
    del g.assists
    assert g.double_double() is False

    # Reassign assists to 15 and confirm double double returns
    g.assists = 15
    assert g.double_double() is True


def test_reassign_shooting_stats_after_deletion():
    g = Game(301, "Oxford", 25, TwoPM_=5, TwoPA_=10)
    assert g.two_pointers == [5, 10]

    # Delete shooting stats
    del g.two_pointers
    assert g._two_pm == 0
    assert g._two_pa == 0

    # Reassign shooting stats and confirm consistency
    g.two_pointers = (7, 12)
    assert g.two_pointers == [7, 12]
    assert g._two_pm == 7
    assert g._two_pa == 12


def test_reassign_free_throws_after_deletion():
    g = Game(302, "Oxford", 28, FTM_=4, FTA_=5)
    assert g.free_throws == [4, 5]

    del g.free_throws
    assert g._ftm == 0
    assert g._fta == 0

    # Reset to valid numbers
    g.free_throws = (6, 8)
    assert g.free_throws == [6, 8]
    assert g._ftm == 6
    assert g._fta == 8


# Take-aways
# Deleting stats should be set to zero instead of removing them entirely
# My init method had error handling with invalid data
# The shot making setters expected 2 input arguments, not tuples, so it has now been adapted.
# The print statements have been updated to reflect the changes in the property names.

# ---------- Creation tests
@pytest.fixture
def season_player():
    return SeasonPlayer.from_games("John Doe", [
        Game(1, "Oxford", 30, assists_=10, rebounds_=5, steals_=2, TwoPM_=5, TwoPA_=10, ThreePM_=2, ThreePA_=5, FTM_=3, FTA_=4),
        Game(2, "Oxford", 25, assists_=8, rebounds_=7, steals_=1, TwoPM_=4, TwoPA_=9, ThreePM_=1, ThreePA_=4, FTM_=2, FTA_=3),
        Game(3, "Oxford", 35, assists_=12, rebounds_=6, steals_=3, TwoPM_=6, TwoPA_=11, ThreePM_=3, ThreePA_=6, FTM_=4, FTA_=5),
    ])

def test_season_player_creation(season_player):
    assert season_player.name == "John Doe"
    assert season_player.games_played() == 3
    assert season_player.total_points() == 57


# ---------- Method tests
def test_avg_points_per_game(season_player):
    assert season_player.points_per_game() == pytest.approx(19.0, 0.1)

def test_assists_per_game(season_player):
    assert season_player.assists_per_game() == 10.0

def test_rebounds_per_game(season_player):
    assert pytest.approx(season_player.rebounds_per_game(), 0.1) == 6.0

def test_avg_methods_zero_games():
    sp = SeasonPlayer("NoGames")
    assert sp.points_per_game() == 0
    assert sp.assists_per_game() == 0
    assert sp.rebounds_per_game() == 0

# Takaways
# Naming for the SeasonPlayer class was a bit confusing initially, so will now implement per a per game naming convention

# ------------------Team class testing
@pytest.fixture
def sample_team():
    p1 = SeasonPlayer.from_games("John Doe", [
        Game(1, "Oxford", 30, assists_=4, rebounds_=5, steals_=2, TwoPM_=5, TwoPA_=10, ThreePM_=2, ThreePA_=5, FTM_=3, FTA_=4),
        Game(2, "Oxford", 25, assists_=4, rebounds_=7, steals_=1, TwoPM_=4, TwoPA_=9, ThreePM_=1, ThreePA_=4, FTM_=2, FTA_=3),
        Game(3, "Oxford", 35, assists_=6, rebounds_=6, steals_=3, TwoPM_=6, TwoPA_=11, ThreePM_=3, ThreePA_=6, FTM_=4, FTA_=5),
    ])

    p2 = SeasonPlayer.from_games("Jane Smith", [
        Game(1, "Oxford", 28, assists_=2, rebounds_=6, steals_=1, TwoPM_=4, TwoPA_=8, ThreePM_=2, ThreePA_=4, FTM_=2, FTA_=3),
        Game(2, "Oxford", 22, assists_=2, rebounds_=5, steals_=0, TwoPM_=3, TwoPA_=7, ThreePM_=1, ThreePA_=3, FTM_=1, FTA_=2),
        Game(3, "Oxford", 30, assists_=5, rebounds_=8, steals_=2, TwoPM_=5, TwoPA_=9, ThreePM_=3, ThreePA_=5, FTM_=4, FTA_=6),
    ])

    p3 = SeasonPlayer.from_games("Alice Johnson", [
        Game(1, "Oxford", 32, assists_=3, rebounds_=7, steals_=2, TwoPM_=6, TwoPA_=12, ThreePM_=4, ThreePA_=8, FTM_=5, FTA_=7),
        Game(2, "Oxford", 29, assists_=1, rebounds_=6, steals_=1, TwoPM_=5, TwoPA_=10, ThreePM_=3, ThreePA_=7, FTM_=4, FTA_=5),
        Game(3, "Oxford", 34, assists_=2, rebounds_=8, steals_=3, TwoPM_=7, TwoPA_=11, ThreePM_=5, ThreePA_=9, FTM_=6, FTA_=8),
    ])

    team1 = Team.from_players("Oxford", Scores=[[54, 43], [90, 45], [80, 90]], Year=2024, League="Division 1", players=[p1, p2, p3])

    return team1

@pytest.fixture
def sample_team_no_scores():
    p1 = SeasonPlayer.from_games("John Doe", [
        Game(1, "Oxford", 30, assists_=4, rebounds_=5, steals_=2, TwoPM_=5, TwoPA_=10, ThreePM_=2, ThreePA_=5, FTM_=3, FTA_=4),
        Game(2, "Oxford", 25, assists_=4, rebounds_=7, steals_=1, TwoPM_=4, TwoPA_=9, ThreePM_=1, ThreePA_=4, FTM_=2, FTA_=3),
        Game(3, "Oxford", 35, assists_=6, rebounds_=6, steals_=3, TwoPM_=6, TwoPA_=11, ThreePM_=3, ThreePA_=6, FTM_=4, FTA_=5),
    ])

    p2 = SeasonPlayer.from_games("Jane Smith", [
        Game(1, "Oxford", 28, assists_=2, rebounds_=6, steals_=1, TwoPM_=4, TwoPA_=8, ThreePM_=2, ThreePA_=4, FTM_=2, FTA_=3),
        Game(2, "Oxford", 22, assists_=2, rebounds_=5, steals_=0, TwoPM_=3, TwoPA_=7, ThreePM_=1, ThreePA_=3, FTM_=1, FTA_=2),
        Game(3, "Oxford", 30, assists_=5, rebounds_=8, steals_=2, TwoPM_=5, TwoPA_=9, ThreePM_=3, ThreePA_=5, FTM_=4, FTA_=6),
    ])

    p3 = SeasonPlayer.from_games("Alice Johnson", [
        Game(1, "Oxford", 32, assists_=3, rebounds_=7, steals_=2, TwoPM_=6, TwoPA_=12, ThreePM_=4, ThreePA_=8, FTM_=5, FTA_=7),
        Game(2, "Oxford", 29, assists_=1, rebounds_=6, steals_=1, TwoPM_=5, TwoPA_=10, ThreePM_=3, ThreePA_=7, FTM_=4, FTA_=5),
        Game(3, "Oxford", 34, assists_=2, rebounds_=8, steals_=3, TwoPM_=7, TwoPA_=11, ThreePM_=5, ThreePA_=9, FTM_=6, FTA_=8),
    ])

    team1 = Team.from_players("Oxford", Scores=None, Year=2024, League="Division 1", players=[p1, p2, p3])

    return team1

# ------------------ Team class tests
def test_team_creation(sample_team):
    assert sample_team.team_name == "Oxford"
    assert sample_team.win_loss_record() == (2, 1)  # Based on scores provided


# ------------------ Testing total methods
def test_totals(sample_team):
    assert sample_team.total_points() == 224  # Sum of all points from players  
    assert sample_team.total_assists() == 29  # Sum of all assists from players
    assert sample_team.total_rebounds() == 58  # Sum of all rebounds from players
    assert sample_team.total_steals() == 15   # Sum of all steals
    assert sample_team.total_blocks() == 0   # No blocks in provided data
    assert sample_team.total_turnovers() == 0 # No turnovers in provided data
    assert sample_team.total_fouls() == 0     # No fouls in provided data
   

def test_totals_no_scores(sample_team_no_scores):
    assert sample_team_no_scores.total_points() == 193 # 31 free throws, 24 3 pointers, 45 two pointers

# ----------------- Testing team average metrics
def test_team_average_metrics(sample_team):
    assert sample_team.team_points_per_game() == pytest.approx(74.67, rel=1e-2)  # 224 / 3
    assert sample_team.team_assists_per_game() == pytest.approx(9.67, rel=1e-2)  # 29 / 3
    assert sample_team.team_rebounds_per_game() == pytest.approx(19.33, rel=1e-2)  # 58 / 3
    assert sample_team.team_steals_per_game() == pytest.approx(5, rel=1e-2)  # 15 / 3
    assert sample_team.team_blocks_per_game() == pytest.approx(0)  # 0 / 3
    assert sample_team.team_turnovers_per_game() == pytest.approx(0)  # 0 / 3
    assert sample_team.team_fouls_per_game() == pytest.approx(0)  # 0 / 3
    assert sample_team.team_points_conceded_per_game() == pytest.approx(59.33, rel=1e-2)  # 178 / 3

# ----------------- Testing team field goal percentages
def test_team_field_goal_percentages(sample_team):
    assert sample_team.team_field_goal_percentage() == pytest.approx((24+45)/(51+87), rel=1e-2)  # Based on provided data
    assert sample_team.team_three_point_percentage() == pytest.approx(24/51, rel=1e-2)  # Based on provided data
    assert sample_team.team_free_throw_percentage() == pytest.approx(31/43, rel=1e-2)  # Based on provided data


# Takeaways
# Always use a calculator for verification