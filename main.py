# Telegram API: https://core.telegram.org/bots/api
# Telepot module documentation: https://telepot.readthedocs.io/en/latest/
# All documents using Do What The F*ck You Want To Public License
# Running on https://t.me/CyprinusCarpioHaematopterusBot

import sys
import time
import telepot
import pprint
import chat
from telepot.loop import MessageLoop
from telepot.helper import ChatHandler
from telepot.delegate import per_chat_id, per_inline_from_id, create_open, pave_event_space


class MessageCounter(ChatHandler):
    def __init__(self, *args, **kwargs):
        super(MessageCounter, self).__init__(*args, **kwargs)

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg, flavor='chat')
        print(content_type, chat_type, chat_id)
        with open('work.log','a') as log:
            pprint(msg, stream=log)
        chat.Analysis(msg, content_type, chat_type, chat_id)

TOKEN = sys.argv[1]
admin = sys.argv[2]

global bot

bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, MessageCounter, timeout=10),
])


print("Listening")
MessageLoop(bot).run_as_thread()

while 1:
    time.sleep(10)
    