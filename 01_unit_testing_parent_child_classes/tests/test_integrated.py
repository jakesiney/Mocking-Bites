from lib.music import *


def test_track_entry_and_list_all():
    library = MusicLibrary()
    track1 = TrackImporter("Artist A", "Track Name A")
    track2 = TrackImporter("Artist B", "Track Name B")
    track3 = TrackImporter("Artist C", "Track Name C")
    library.add(track1)
    library.add(track2)
    library.add(track3)
    assert library.list_all() == [track1, track2, track3]


def test_search():
    library = MusicLibrary()
    track1 = TrackImporter("Jake", "Song")
    library.add(track1)
    assert library.search("Song") == [track1]
    assert library.search("Jake") == [track1]
