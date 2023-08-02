from unittest.mock import Mock
from lib.music import *


def test_search_function_mock():
    library = MusicLibrary()
    fake_matching = Mock()
    fake_matching.matches.return_value = True
    library.add(fake_matching)
    fake_not_matching = Mock()
    fake_not_matching.matches.return_value = False
    library.add(fake_not_matching)
    assert library.search("hello") == [fake_matching]


def test_tracks_are_added_and_listed():
    library = MusicLibrary()
    track_a = Mock()
    track_b = Mock()
    track_c = Mock()
    library.add(track_a)
    library.add(track_b)
    library.add(track_c)
    assert library.tracks == [track_a, track_b, track_c]
