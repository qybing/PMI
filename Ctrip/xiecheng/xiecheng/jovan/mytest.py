import re

url = 'http://hotels.ctrip.com/hotel/823876.html&hotel_id=823876&low_price=269'
is_hotel_id = url.find('&hotel_id')
hotel = url[0:is_hotel_id]
print(hotel)
id_price = re.findall(r'&hotel_id=(\d+)&low_price=(\d+)',url)[0]
hotel_id = id_price[0]
low_price = id_price[1]
print(hotel_id,low_price)