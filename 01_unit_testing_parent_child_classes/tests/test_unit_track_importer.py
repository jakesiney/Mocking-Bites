from lib.music import TrackImporter


def test_match_title_to_keyword():
    track = TrackImporter("Apple", "Pears")
    assert track.matches("Pears") == True


def test_match_partial_artist():
    track = TrackImporter("Apple Title", "Pears Title")
    assert track.matches("Appl") == True


def test_match_partial_title():
    track = TrackImporter("Apple Title", "Pears Title")
    assert track.matches("Titl") == True
