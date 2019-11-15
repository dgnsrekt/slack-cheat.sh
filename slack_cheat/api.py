"""Provides helper functions that clean, parse, and prepare text for making web requests."""
import string


def remove_puctuation(text: str) -> str:
    """Remove punctuation from given text.

    :param text: The text to be formatted.
        returns: Text with all punctuation removed.
    """
    return text.translate(str.maketrans("", "", string.punctuation))
