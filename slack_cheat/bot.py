from datetime import datetime
from time import time, sleep

import slack

from .commands import Commands


def prepare_slack_message(*, title, message):
    title_text = {"type": "mrkdwn", "text": f"{title}"}
    title_block = {"type": "section", "text": title_text}
    message_text = {"type": "mrkdwn", "text": f"```{message}```"}
    message_block = {"type": "section", "text": message_text}

    return [title_block, message_block]


def parse_payload(payload):
    data = payload.get("data")
    web_client = payload.get("web_client")
    rtm_client = payload.get("rtm_client")

    channel = data.get("channel")
    user = data.get("user")
    text = data.get("text")

    return web_client, rtm_client, channel, user, text


def create_bot(token):
    @slack.RTMClient.run_on(event="message")
    def respond(**payload):
        web_client, rtm_client, channel, user, text = parse_payload(payload)

    #        web_client.chat_postMessage(channel=channel, message=text)

    return slack.RTMClient(token=token)
