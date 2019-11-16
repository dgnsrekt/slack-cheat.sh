from datetime import datetime
from time import time, sleep

import slack

from api import question_request, Commands


def prepare_slack_message(*, title, message):
    # TODO: DRY, sep blocks for better readability
    title_block = {"type": "section", "text": {"type": "mrkdwn", "text": f"{title}"}}
    message_block = {"type": "section", "text": {"type": "mrkdwn", "text": f"```{message}```"}}
    return [title_block, message_block]


def parse_payload(payload):  # TODO: rename parse_payload
    data = payload.get("data")
    web_client = payload.get("web_client")
    rtm_client = payload.get("rtm_client")

    channel = data.get("channel")
    user = data.get("user")
    text = data.get("text")

    return web_client, rtm_client, channel, user, text
