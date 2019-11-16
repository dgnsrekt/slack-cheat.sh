"""Provides utility functions that help clean, parse, and prepare web requests reponses."""
import string

from typing import Optional as Opt

from requests import codes
from requests_html import HTMLResponse, HTMLSession


def remove_puctuation(text: str) -> str:
    """Remove punctuation from given text.

    :param text: The text to be formatted.
    :returns: Text with all punctuation removed.
    """
    return text.translate(str.maketrans("", "", string.punctuation))


def replace_spaces(text: str) -> str:
    """Replaces spaces with '+' in given text.

    :param text: The text to be formatted.
    :returns: Text with spaces replaced with '+'.
    """
    return text.replace(" ", "+")


def clean_text(text: str) -> str:
    """Cleans text for request.

    Removes punctuation, replaces spaces with '+', and
    converts text to lowercase.
    :param text: The text to be cleaned.
    :returns: Cleaned lowercase text.
    """
    text = remove_puctuation(text)
    text = replace_spaces(text)
    return text.lower()


def prepare_question_request(topic: str, sub: str, index: Opt[int], options: str) -> str:
    """Prepares a clean url with topic and subtopic.

    :param topic: The topic to be searched. Example: python
    :param sub: A subtopic in the topic. Example: print+statement
    :param index:
    :param options:
    :returns: A formatted url.
    """
    url = "http://cheat.sh"
    subtopic = clean_text(sub)

    if index:
        return f"{url}/{topic}/{subtopic}/{index}/{options}"  # noqa: WPS221 WPS226

    return f"{url}/{topic}/{subtopic}/{options}"  # noqa: WPS221 WPS226


def parse_response(response: str) -> Opt[str]:
    """If the repsonse has a 200 status code returns the parsed text from the html.

    :param response:
    :returns: parse reponse.
    """
    if response.status_code == codes["ok"]:
        text = response.html.find("pre", first=True).full_text
        if len(text) > 6:
            return text
    return "Not Found"


def get_request(url: str) -> HTMLResponse:
    """Makes a http requests to the server.

    :param url: The url to send the get requests.
    :returns: The html response from the server.
    """
    session = HTMLSession()
    return session.get(url)


def format_message_pagination(text, max_characters=1500):
    """Splits text with lines > the max_characters length into chunks.

    :param text:
    :returns:
    """
    chunks = str()
    messages = []

    def is_newline_character(char):  # noqa: WPS430
        if char == "\n":
            return True
        return False

    for char in text:
        chunks += char
        if len(chunks) > max_characters:
            if is_newline_character(char):
                messages.append(chunks)
                chunks = str()

    messages.append(chunks)

    return messages
