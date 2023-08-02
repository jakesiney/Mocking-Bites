from unittest.mock import Mock
from lib.diary_entry_formatter import DiaryEntryFormatter


def test_format_diary_entry():
    entry = Mock()
    entry.title = "Title"
    entry.contents = "Some contents"
    entry.word_count.return_value = 2
    formatter = DiaryEntryFormatter(entry)
    assert formatter.format() == "Title, 2 Some contents"




