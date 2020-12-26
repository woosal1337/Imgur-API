import os
import imgurpython

f = open("user.token", "r")
client_id, client_secret = f.readline().split(";")
f.close()

client = imgurpython.ImgurClient(client_id, client_secret)
items = client.gallery()

max_item = ""
max_views = 0
for item in items:
    if item.views > max_views:
        max_views = item.views

print(max_views)