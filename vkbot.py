from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import user_token, comm_token, offset, line
import requests
import datetime
from fun import *

session = vk_api.VkApi(token=comm_token)

def send_message(user_id, message):
    session.method("message_send",{
        "user_id": user_id,
        "message": message,
        "random_id": 0})


    
def loop_bot():
    for event in VkLongPoll(session).listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                message_text = event.text
                return message_text, event.user_id

def show_info():
    write_msg(user_id, f'Меню бота - Vkinder')


def menu_bot(id_num):
    write_msg(id_num,
         f"Привет, я бот\n"
         f"\nЕсли вы используете его первый раз - пройдите регистрацию.\n"
        f"Для регистрации введите - Да.\n"
        f"Если вы уже зарегистрированы - начинайте поиск.\n")



def reg_new_user(id_num):
    write_msg(id_num, 'Вы прошли регистрацию.')
    write_msg(id_num, f"Vkinder - для активации бота\n")
    check(user_id)

def questionnaire_search(user_id):
    while True:
        msg_text, user_id = loop_bot()
        if msg_text == "vkinder":
            menu_bot(user_id)
            msg_text, user_id = loop_bot()

            if msg_text.lower() == 'да':
                reg_new_user(user_id)
            sex = get_sex(user_id)
            city = get_city(user_id)
            write_msg(ids, 'Введите нижний порог возраста (min - 18).')
            age_at = msg_text
            if int(age_at) < 18:
                write_msg(user_id, 'введен минимальный возраст - 18 лет.')
                write_msg(ids, 'Введите нижний порог возраста (min - 18).')
            write_msg(ids, 'Введите максимальный порог возраста')
            age_to = msg_text
            result = search_users(sex, int(age_at), int(age_to), city)
            result_link = get_link(sex, int(age_at), int(age_to), city)
            result_id = (result[i][2])
            for i in range(len(result)):
                user_photo = get_photo(result_id)
                write_msg(user_id, f'\n{result_link}  {user_photo} ', )
                if user_photo == 'нет доступа к фото':
                    continue
                sorted_user_photo = sort_likes(user_photo)

                write_msg(user_id, f'\n{result[i][0]}  {result[i][1]}  {result[i][2]}', )
                try:
                    write_msg(user_id, f'фото:',
                          attachment=','.join
                          ([sorted_user_photo[-1][1], sorted_user_photo[-2][1],
                            sorted_user_photo[-3][1]]))
                except IndexError:
                    for photo in range(len(sorted_user_photo)):
                        write_msg(user_id, f'фото:',
                              attachment=sorted_user_photo[photo][1])

                write_msg(user_id, '1 - выбрать,  0 - пропустить, \nq - выход из поиска')
                msg_text, user_id = loop_bot()
                if msg_text == '0':
                    show_info()

                elif msg_text == '1':
                    write_msg(user_id, f'\n{result_link}')
                    break
                elif msg_text.lower() == 'q':
                    write_msg(user_id, 'Введите Vkinder для активации бота')
                    break




