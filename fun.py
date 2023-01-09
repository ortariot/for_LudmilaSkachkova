import vk_api
from config import user_token, comm_token, offset, line
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
    if sex != 'None':
        for i in sex:
            if i.get('sex') == 2:
                find_sex = 1
                return find_sex
            elif i.get('sex') == 1:
                find_sex = 2
                return find_sex
    else:
        write_msg(user_id, 'Бот не может определить вашу половую принадлежность, заполните профиль')
    

def get_city(user_id):
    city = session.method("users.get",{"user_id" : user_id, "fields" : "city"})
    if city != 'None':
        for i in city:
            city = i.get('city')
            id_city = str(city.get('id'))
            return id_city
    else:
        write_msg(user_id, 'Бот не может определить ваш город, заполните профиль')

def search_users(sex, age_at, age_to, city_id):
    all_persons = []
    response = session.method("users.search",  {'sort': 1,
                           'sex': get_sex(user_id),
                           'status': 1,
                           'age_from': age_at,
                           'age_to': age_to,
                           'has_photo': 1,
                           'count': 25,
                           'online': 1,
                           'city_id': get_city(user_id)
                           })

    for element in response['items']:
        person = [
            element['first_name'],
            element['last_name'],
            element['id']
        ]
        all_persons.append(person)
    return all_persons
    
def get_photo(user_owner_id):
    try:
        response = session.method('photos.get',
                              {
                                  'owner_id': user_owner_id,
                                  'album_id': 'profile',
                                  'count': 10,
                                  'extended': 1,
                                  'photo_sizes': 1,
                              })
    except ApiError:
        return 'нет доступа к фото'
    users_photos = []
    for i in range(10):
        try:
            users_photos.append(
                [response['items'][i]['likes']['count'],
                 'photo' + str(response['items'][i]['owner_id']) + '_' + str(response['items'][i]['id'])])
        except IndexError:
            users_photos.append(['нет фото.'])
    return users_photos

def sort_likes(photos):
    result = []
    for element in photos:
        if element != ['нет фото.'] and photos != 'нет доступа к фото':
            result.append(element)
    return sorted(result)


def get_link(sex, age_at, age_to, city):
    all_persons = []
    response = session.method("users.search",  {'sort': 1,
                           'sex': sex,
                           'status': 1,
                           'age_from': age_at,
                           'age_to': age_to,
                           'has_photo': 1,
                           'count': 25,
                           'online': 1,
                           'hometown': city
                           })
    list_1 = response['items']
    for person_dict in list_1:
        if person_dict.get('is_closed') == False:
            vk_link = 'vk.com/id' + str(person_dict.get('id'))
            return vk_link
    
        




