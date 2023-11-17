import requests
import configuration
import data

# запрос на создание нового заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)

# запрос на получение данных о заказе по трек-номеру
def get_orders_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_CHECK_PATH + "?t=" + str(track_number))
