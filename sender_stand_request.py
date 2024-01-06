import configuration
import requests
import data

#create order
def post_create_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=body)
response = post_create_orders(data.create_orders_body);

# Getting orders on the track
def get_new_orders_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_PATH)




