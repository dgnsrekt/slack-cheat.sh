"""Functions used to send question requested."""
from typing import Optional as Opt

from api import (
    get_request,
    parse_response,
    prepare_question_request,
)


URL = "http://cheat.sh/"


def question_request(topic: str, sub: str, index: Opt[int] = None, comments=False) -> Opt[str]:
    """Answer question about .

    :param topic:
    :param subtopic:  A subtopic of bash.
    :param index:
    :param comments:
    :returns: The full text string of the response or None.
    """
    # ?T for text only, ?Q for no comments.
    if comments:
        options = "?T"
    else:
        options = "?T?Q"

    pre_request = prepare_question_request(topic, sub, index, options)
    response = get_request(pre_request)

    return parse_response(response)


def message_debugger(message):
    """Prints paginated messages.

    :param message:
    :returns:
    """
    for index, line in enumerate(message):
        if index > 0:
            repr("=" * 10, f"section {(index) + 1} of {len(message)}", "=" * 10)  # noqa: WPS221
        repr(line)


def clean_commandlist_response(response):
    """Removes un-need words from list type responses.

    :param response:
    :returns:
    """
    clean = []
    for line in response.split("\n"):
        skip_symbols = ["$"]
        skip_words = ["hello", "1line", "weird", ":learn", ":list", "rosetta"]

        if any(symbol in line for symbol in skip_symbols):
            continue

        if any(word in line.lower() for word in skip_words):
            continue

        if line:
            clean.append(line.capitalize())
    return "\n".join(clean)


def basic_command(url):
    """Used to make request. Helper used to reduce repetition."""
    response = get_request(url)
    return parse_response(response)


def list_topics():
    """Gets a list of all cheat sheets topics."""
    url = f"{URL}:list?T"
    parsed_response = basic_command(url)
    return clean_commandlist_response(parsed_response)


def list_common_subs(topic: str):
    """Gets a list of all subtopics."""
    url = f"{URL}/{topic}/:list?T"
    parsed_response = basic_command(url)
    return clean_commandlist_response(parsed_response)


def language_basics(topic: str):
    """Gets a snippet for getting started with the language."""
    url = f"{URL}/{topic}/:learn?T"
    return basic_command(url)


def hello_world(topic: str):
    """Get instructions on how to install, build, run, script hello world."""
    url = f"{URL}/{topic}/:hello?T"
    return basic_command(url)


def common_oneliners(topic: str):
    """Gets a list of common oneliners."""
    url = f"{URL}h/{topic}/1line?T"
    return basic_command(url)


def weird_stuff(topic: str):
    """Gets description of weird things in the language."""
    url = f"{URL}/{topic}/weird?T"
    return basic_command(url)
