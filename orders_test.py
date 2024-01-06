# Екатерина Задорина, 12-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request

#getting orders for track number
def positive_assertion():
    response_positive = sender_stand_request.post_create_orders(data.create_orders_body)
    track = response_positive.json()["track"]
    return sender_stand_request.get_new_orders_track(track).status_code

#   Automated assertion of getting an order from its track
def test_get_order_from_track_code_200():
	assert positive_assertion() == 200
