from scripts.string_methods import *


def test_capitalize_title():
    assert capitalize_title("my hobbies") == "My Hobbies"


def test_check_sentence_ending():
    sentence = "and read."
    assert check_sentence_ending(sentence) == True
