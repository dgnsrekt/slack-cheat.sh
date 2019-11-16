from slack_cheat.commands import Commands

commander = Commands()
accepted_topics = [topic.lower() for topic in commander.list_topics().split("\n")]

new_topic = "Rust"
new_topic = new_topic.lower()

if new_topic in accepted_topics:
    commander.add_topic(new_topic)
else:
    raise ValueError
# print(commander)
# commander.execute("rust")
sub = "how to parse a string?"
result = commander.execute("rust", sub_topic=sub)
print(result)

# topic = "python"
# commands.execute("hello", topic="python")
# commands.execute("oneliner", topic="python")
# commands.add_topic("python3")
# commands.execute("python3", sub_topic=sub, index=2, comments=True)
