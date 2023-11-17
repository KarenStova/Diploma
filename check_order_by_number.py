# Cкоробогатова Карина, 10-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data

# Шаг 1: создаём новый заказ
def post_new_order():
    order_response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                               json=data.order_body,
                               headers=data.headers)
    print(order_response.json())
    return order_response

# Шаг 2: сохраняем трек-номер нового заказа
def get_track(response_post):
    if response_post.status_code == 200:
        track_number = response_post.json().get("track")
        return track_number
    else:
        print(f"Error creating new order. Status code: {response_post.status_code}")
        return None

# Шаг 3: получаем заказ по его трек-номеру
def get_order_by_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_CHECK_PATH + "?t=" + str(track_number))

# Шаг 4: проверяем, что код ответа - 200
def check_response_code(response):
    if response.status_code == 200:
        print("Test passed: Response code is 200.")
    else:
        print(f"Test failed: Wrong status code. Status code: {response.status_code}")

# Cам автотест
first = post_new_order()
track = get_track(first)
order = get_order_by_track(track)
check_response_code(order)