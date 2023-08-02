
class DiaryEntryFormatter:
    def __init__(self, diary_entry):
        self.diary_entry = diary_entry

    def format(self):
        word_count = self.diary_entry.word_count()
        return f"{self.diary_entry.title}, {word_count} {self.diary_entry.contents}"