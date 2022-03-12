from scripts.string_methods import *


def test_capitalize_title():
    assert capitalize_title("my hobbies") == "My Hobbies"


def test_check_sentence_ending():
    sentence = "and read."
    assert check_sentence_ending(sentence) == True


def test_check_sentence_ending_false():
    sentence = "and read"
    assert check_sentence_ending(sentence) == False


def test_clean_up_spacing():
    sentence = " I like to go on hikes with my dog.  "
    assert clean_up_spacing(sentence) == "I like to go on hikes with my dog."
