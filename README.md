# slack-cheat.sh
cheat.sh bot for slack. http://cheat.sh/
## Config
Evironmental Variables
```
OAUTH_ACCESS_TOKEN
BOT_CHANNEL
BOT_DISPLAY_NAME
TOPICS
TITLE_LINE_NUMBER
```
## Heroku
## Help
```
Usage: /{TOPIC} {SUBTOPIC}
/help - Shows this message
/topics - List all searchable topics.
/add {TOPIC}- Adds topic to list of commands. Must be a searchable topic. 
/python {SUBTOPIC} - Returns a python cheatsheet based on the sub.
/rust {SUBTOPIC} - Returns a rust cheatsheet based on the sub.
/linux {SUBTOPIC} - Returns a linux cheatsheet based on the sub.
/bash {SUBTOPIC} - Returns a bash cheatsheet based on the sub.
/git {SUBTOPIC} - Returns a git cheatsheet based on the sub.

Examples:
  /python How do you reverse a list?
  /add haskell

Everytime you request the same subtopic it will respond with a new unique cheat sheet variation of the requested subtopic.
```
