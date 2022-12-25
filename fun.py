import vk_api
from config import user_token, comm_token
import datetime
from random import randrange
from bd_vkinder import *
session = vk_api.VkApi(token=user_token)
vk = session.get_api()


def write_msg(user_id, message):
    msg = session.method("messages.send",{"user_id" : user_id, 'message': message,'random_id': randrange(10 ** 7) })

def get_name(user_id):
    name = session.method("users.get",{"user_id" : user_id})
    try:
        for i in name:
            first_name = i.get('first_name')
        return first_name
    except KeyError:
        write_msg(user_id, 'Ошибка получения токена, введите токен в переменную - user_token')

def get_sex(user_id):
    sex = session.method("users.get",{"user_id" : user_id, "fields" : "sex"})
    try:
        for i in sex:
            if i.get('sex') == 2:
                find_sex = 1
                return find_sex
            elif i.get('sex') == 1:
                find_sex = 2
                return find_sex
    except KeyError:
        self.write_msg(user_id, 'Ошибка получения токена, введите токен в переменную - user_token')

def get_age_min(user_id):
    age = session.method("users.get",{"user_id" : user_id, "fields" : "bdate"})
    try:
        for i in age:
            date = i.get('bdate')
        date_list = date.split('.')
        if len(date_list) == 3:
            year = int(date_list[2])
            year_now = int(datetime.date.today().year)
            return year_now - year
        elif date not in age:
            write_msg(user_id, 'Введите нижний порог возраста (min - 18): ')
            for event in self.longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    age = event.text
                    return age
    except KeyError:
        write_msg(user_id, 'Ошибка получения токена, введите токен в переменную - user_token')

def get_age_max(user_id):
    age = session.method("users.get", {"user_id": user_id, "fields": "bdate"})
    try:
        for i in age:
            date = i.get('bdate')
        date_list = date.split('.')
        if len(date_list) == 3:
            year = int(date_list[2])
            year_now = int(datetime.date.today().year)
            return year_now - year
        elif date not in age:
            write_msg(user_id, 'Введите верхний порог возраста: ')
            for event in self.longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    age = event.text
                    return age
    except KeyError:
        write_msg(user_id, 'Ошибка получения токена, введите токен в переменную - user_token')



def get_city(user_id):
    city = session.method("users.get",{"user_id" : user_id, "fields" : "city"})
    try:
        for i in city:
            city = i.get('city')
            id_city = str(city.get('id'))
            return id_city
    except KeyError:
        self.write_msg(user_id, 'Ошибка получения токена, введите токен в переменную - user_token')

def find_user(user_id):
    find_users = session.method("users.search", {"sex": get_sex(user_id),
                                                 "city": get_city(user_id),
                                                 "status": '1' or '6',
                                                 'count': 5,
                                                'fields': 'is_closed, id, first_name, last_name',
                                                 'age_from': get_age_min(user_id),
                                                 'age_to': get_age_max(user_id),
                                                 })
    try:
        dict_1 = find_users['response']
        list_1 = dict_1['items']
        for person_dict in list_1:
            if person_dict.get('is_closed') == False:
                first_name = person_dict.get('first_name')
                last_name = person_dict.get('last_name')
                vk_id = str(person_dict.get('id'))
                vk_link = 'vk.com/id' + str(person_dict.get('id'))
                insert_data_users(first_name, last_name, vk_id, vk_link)
            else:
                continue
        return f'Поиск завершён'
    except KeyError:
        write_msg(user_id, 'Ошибка получения токена')


def get_photos_id(user_id):
    resp = session.method("photos.getAll",{ 'access_token': user_token,
                                             'type': 'album',
                                             'owner_id': user_id,
                                             'extended': 1,
                                             'count': 25 })
    resp_items = resp['items']
    dict_photos = dict()
    try:
        for i in resp_items:
            id_photos = i['id']
            like_count_photos = i['likes']
            list_photos = (id_photos, like_count_photos)
            if like_count_photos.get('count'):
                likes = like_count_photos.get('count')
                dict_photos[likes] = id_photos
        list_of_ids = sorted(dict_photos.items(), reverse=True)
        return list_of_ids
    except KeyError:
        self.write_msg(user_id, 'Ошибка получения токена')



def get_photo_1(user_id):
    list = get_photos_id(user_id)
    count = 0
    for i in list:
        count += 1
        print(i)
        if count == 1:
            return i[1]

def get_photo_2(user_id):
    list = get_photos_id(user_id)
    count = 0
    for i in list:
        count += 1
        if count == 2:
            return i[1]

def get_photo_3(user_id):
    list = get_photos_id(user_id)
    count = 0
    for i in list:
        count += 1
        if count == 3:
            return i[1]

def send_photo_1(user_id, message, offset):
    msg = session.method("messages.send",{ 'user_id': user_id,
                                           'access_token': user_token,
                                           'message': message,
                                           'attachment': f'photo{person_id(offset)}_{get_photo_1(person_id(offset))}',
                                           'random_id': 0})

def send_photo_2(user_id, message, offset):
    msg = session.method("messages.send",{ 'user_id': user_id,
                                           'access_token': user_token,
                                           'message': message,
                                           'attachment': f'photo{person_id(offset)}_{get_photo_2(person_id(offset))}',
                                           'random_id': 0})

def send_photo_3(user_id, message, offset):
    msg = session.method("messages.send",{ 'user_id': user_id,
                                           'access_token': user_token,
                                           'message': message,
                                           'attachment': f'photo{person_id(offset)}_{get_photo_3(person_id(offset))}',
                                           'random_id': 0})
    print(msg)


def find_persons(user_id, offset):
    write_msg(user_id, found_person_info(offset))
    person_id(offset)
    insert_data_seen_users(person_id(offset), offset)  # offset
    get_photos_id(person_id(offset))
    send_photo_1(user_id, 'Фото номер 1', offset)
    if get_photo_2(person_id(offset)) != None:
        send_photo_2(user_id, 'Фото номер 2', offset)
        send_photo_3(user_id, 'Фото номер 3', offset)
    else:
        write_msg(user_id, f'Больше фотографий нет')

def found_person_info(offset):
    tuple_person = select(offset)
    list_person = []
    for i in tuple_person:
        list_person.append(i)
    return f'{list_person[0]} {list_person[1]}, ссылка - {list_person[3]}'


def person_id(offset):
    tuple_person = select(offset)
    list_person = []
    for i in tuple_person:
        list_person.append(i)
    return str(list_person[2])




find_persons(68343, "1")


