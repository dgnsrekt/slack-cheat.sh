"""Functions used to send question requested."""
from typing import Optional as Opt

from .api import get_request, parse_response, prepare_question_request


URL = "http://cheat.sh/"


def question_request(
    topic: str, sub: str, index: Opt[int] = None, comments: bool = False
) -> Opt[str]:
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


class Commands:
    """Command list."""

    def __init__(self):

        self.commands = {
            "topics": self.list_topics,
            "learn": self.language_basics,
            "list": self.list_subtopics,
            "hello": self.hello,
            "oneliner": self.one_liners,
            "weird": self.weird,
            "python": self.question,
        }

    def add_topic(self, topic: str):
        self.commands[topic] = self.question

    def list_commands(self):
        return list(self.commands)

    def _basic_command(self, url):  # noqa: WPS602
        """Used to make request. Helper used to reduce repetition."""
        response = get_request(url)
        return parse_response(response)

    def list_topics(self, *args, **kwargs):
        """Gets a list of all cheat sheets topics."""
        url = f"{URL}:list?T"
        parsed_response = self._basic_command(url)
        return clean_commandlist_response(parsed_response)

    def list_subtopics(self, *args, **kwargs):
        """Gets a list of all subtopics."""
        topic = kwargs["topic"]
        url = f"{URL}/{topic}/:list?T"
        parsed_response = self._basic_command(url)
        return clean_commandlist_response(parsed_response)

    def language_basics(self, *args, **kwargs):
        """Gets a snippet for getting started with the language."""
        topic = kwargs["topic"]
        url = f"{URL}/{topic}/:learn?T"
        return self._basic_command(url)

    def hello(self, *args, **kwargs):
        """Get instructions on how to install, build, run, script hello world."""
        topic = kwargs["topic"]
        url = f"{URL}/{topic}/:hello?T"
        return self._basic_command(url)

    def one_liners(self, *args, **kwargs):
        """Gets a list of common oneliners."""
        topic = kwargs["topic"]
        url = f"{URL}/{topic}/1line?T"
        return self._basic_command(url)

    def weird(self, *args, **kwargs):
        """Gets description of weird things in the language."""
        topic = kwargs["topic"]
        url = f"{URL}/{topic}/weird?T"
        return self._basic_command(url)

    def question(self, *args, **kwargs):
        topic = kwargs["command_name"]
        sub = kwargs["sub_topic"]
        return question_request(topic, sub)

    def execute(self, command_name: str, *args, **kwargs):
        assert command_name in self.commands  # fix
        kwargs["command_name"] = command_name
        return self.commands[command_name](*args, **kwargs)

    def __str__(self):
        return "\n".join([f"{key} : {value.__name__}" for key, value in self.commands.items()])
