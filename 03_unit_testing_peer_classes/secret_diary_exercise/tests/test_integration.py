import pytest
from lib.diary import Diary
from lib.secret_diary import SecretDiary


def test_when_locked_cannot_read():
    diary = Diary("contents")
    secret = SecretDiary(diary)
    with pytest.raises(Exception) as err:
        secret.read() == "Go away!"
    assert str(err.value) == "Go away!"



def test_diary_entry_unlocked_int():
    diary = Diary("contents")
    secret = SecretDiary(diary)
    secret.unlock()
    assert secret.read() == "contents"