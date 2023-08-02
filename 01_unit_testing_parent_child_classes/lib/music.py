class TrackImporter:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def matches(self, keyword):
        if keyword in self.title or keyword in self.artist:
            return True



class MusicLibrary:
    def __init__(self):
        self.tracks = []

    def add(self, tracks):
        self.tracks.append(tracks)

    def search(self, keyword):
        return [track for track in self.tracks if track.matches(keyword)]

    def list_all(self):
        return self.tracks
