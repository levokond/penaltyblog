import pandas as pd
import pytest

import penaltyblog as pb


@pytest.mark.local
def test_clubelo_by_date():
    ce = pb.scrapers.ClubElo()
    df = ce.get_elo_by_date()
    assert type(df) == pd.DataFrame


@pytest.mark.local
def test_clubelo_by_team():
    ce = pb.scrapers.ClubElo()
    df = ce.get_elo_by_team("Barcelona")
    assert type(df) == pd.DataFrame


@pytest.mark.local
def test_clubelo_team_names():
    ce = pb.scrapers.ClubElo()
    df = ce.get_team_names()
    assert type(df) == pd.DataFrame


@pytest.mark.local
def test_clubelo_team_mappings():
    team_mappings = pb.scrapers.get_example_team_name_mappings()
    ce = pb.scrapers.ClubElo(team_mappings)
    df = ce.get_elo_by_date()
    assert "Paris SG" in df.index.unique()
