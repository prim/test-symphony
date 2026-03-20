from __future__ import annotations

from collections import Counter


PUNCTUATION_TO_REMOVE = ",.!?;:'\""


def count_words(text: str) -> dict[str, int]:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text == "":
        return {}

    normalized_text = text.lower().translate(
        str.maketrans("", "", PUNCTUATION_TO_REMOVE)
    )
    words = normalized_text.split()

    if not words:
        return {}

    return dict(Counter(words))
