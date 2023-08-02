from lib.diary_entry import DiaryEntry

def test_diary_entry():
    entry = DiaryEntry("Title", "Some contents")
    assert entry.title == "Title"
    assert entry.contents == "Some contents"

def test_count_words_in_content():
    entry = DiaryEntry("Title", "one two three")
    assert entry.word_count() == 3