from lib.diary import Diary

def test_entry():
    diary = Diary("Words")
    assert diary.read() == "Words"
