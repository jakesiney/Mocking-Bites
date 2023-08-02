from unittest.mock import Mock
from lib.diary_entry_formatter import DiaryEntryFormatter
from lib.diary_entry import DiaryEntry
import pytest


# @pytest.mark.skip
def test_format_diary_entry():
    entry = DiaryEntry("Title", "Some contents")
    formatter = DiaryEntryFormatter(entry)
    assert formatter.format() == "Title, 2 Some contents"