def capitalize_title(title: str) -> str:
    return title.title()


def check_sentence_ending(sentence: str) -> bool:
    return sentence.endswith(".")


def clean_up_spacing(sentence: str) -> str:
    return sentence.strip()
