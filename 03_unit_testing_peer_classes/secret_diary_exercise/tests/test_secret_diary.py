from unittest.mock import Mock
from lib.secret_diary import SecretDiary
import pytest

def test_secret_entry_when_locked():
    diary = Mock()
    secret = SecretDiary(diary)
    with pytest.raises(Exception) as err:
        secret.read() == "Go away!"
    assert str(err.value) == "Go away!"

def test_secret_entry_with_unlocked():
    diary = Mock()
    diary.read.return_value = "words"
    secret = SecretDiary(diary)
    secret.unlock()
    assert secret.read() == ("words")

    



