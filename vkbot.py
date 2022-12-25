from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import user_token, comm_token, offset, line
import requests
import datetime
from 1 import *


session = vk_api.VkApi(token=comm_token)



def send_message(user_id, message):
    session.method("message_send",{
        "user_id": user_id,
        "message": message,
        "random_id": 0

    })

for event in VkLongPoll(session).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text.lower()
        user_id = event.user_id
        if text == "hello":
            send_message(user_id, "something text")
            find_user(user_id)
            write_msg(event.user_id, f'Нашёл для тебя пару, жми на кнопку "Вперёд"')