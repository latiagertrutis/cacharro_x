# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    cacharro_x.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mrodrigu <mrodrigu@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/24 11:56:09 by mrodrigu          #+#    #+#              #
#    Updated: 2018/06/30 16:10:10 by mrodrigu         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import json
import requests

PAGE_TOKEN = "EAACEdEose0cBAPJFHY4XoJ8RjZAPJ9uKKGZAOtZCFDyl0FSQIql3cHvJ68ysZALzVZBwpZBzId2ZAADYy8ghSNkoTybsqxDl0LZBpibBRWzjY29N2Omph4ibGGmXHEgZBvauuTZB2E00Vs0IarnFjLtiPdtwRQu0vVFZA9rXTZCzfZADtXceHHD8zR4fD02Js0k9ZAPUInsaEs4cZAxcgZDZD"
PAGE_TOKEN_PERMANENT = "EAACmfVZAQJwABAKNWZACWIX1we5sVa0vAmkcKLB6zUulcyqoOk0F7gLnJrXyc1yQtIMtzyft45tjyIUQDvlAHdRm3l0pnQpNI3ybjahzZAbFqVGaoedKX7i49eBtRCNkF43QAZAz48R3KhepGYepuighRPYs459TTtIY9BBnZCAZDZD`1"
USER_TOKEN_SHORT = "EAACmfVZAQJwABANUHIcDWWwdPz3X7kEun2V9uPZBfupOCtYEWLCBZBePlDVX2a1BEj8ZCK0CZBYutERZA7yWi1TxRkKZC0nP2zcKEkY2lj2TmUb8y5RSPNKGbanTAZB86ICBVANWSwDrpFv2EDUO3FBnF8D56LJZBfxsZBT6kkdCZC7e9VC8elYZCAKcGeStZAzRvrZCwsHoTsFyeLXwZDZD"
USER_TOKEN_PERMANENT = "EAACmfVZAQJwABAGMyEquQWk6Hz3G7COhe4cvqobBJreZCZAZAHtY7QK9S8MRXDTqAxOc3psHBSsXg2sxQaufq37az4wD35mjH0nSeCQlad0C2BF6fjueTG0nmCR8oVDr1XaTYkIQ90DjRpw2VnWO3j1c9M7aCHRxQZBt6jgXvvgZDZD"
PAGE_ID = "371121376687075"
APP_ID = "183057249216256"
APP_SECRET = "1be7a9feb2c15b9b4e4c05cdcb51a337"
COMMENT_ID = "371121376687075_424570551342157"

def get_permanent_user_token(app_id = APP_ID, app_secret = APP_SECRET, user_token_short = USER_TOKEN_SHORT):
	url = "https://graph.facebook.com/v3.0/oauth/access_token?grant_type=fb_exchange_token&client_id={}&client_secret={}&fb_exchange_token={}".format(app_id, app_secret, user_token_short)
	return ((json.loads((requests.get(url)).content.decode("utf8")))["access_token"])

def get_user_id(user_token_permanent = USER_TOKEN_PERMANENT):
	url = "https://graph.facebook.com/v3.0/me?access_token={}".format(user_token_permanent)
	return ((json.loads((requests.get(url)).content.decode("utf8")))["id"])

def get_page_permanent_token(user_id, user_token_permanent = USER_TOKEN_PERMANENT):
	url = "https://graph.facebook.com/v3.0/{}/accounts?access_token={}".format(user_id, user_token_permanent)
	return ((json.loads((requests.get(url)).content.decode("utf8"))))

def get_user_page_id(user_id, user_token_permanent = USER_TOKEN_PERMANENT):
	url = "https://graph.facebook.com/v3.0/{}/accounts?access_token={}".format(user_id, user_token_permanent)
	data = (json.loads((requests.get(url)).content.decode("utf8")))
	ids = []
	for i in data["data"]:
		ids.append(i["id"])
	return (ids)

# url = "https://graph.facebook.com/v3.0/{}/feed/?access_token={}".format(PAGE_ID, PAGE_TOKEN)
# peticion de informacion
# url = "https://graph.facebook.com/v3.0/{}/?access_token={}&fields=message".format(COMMENT_ID, PAGE_TOKEN)
# carga en un json
data = get_user_page_id(get_user_id())
for i in data:
	print(i);
# print("Al post:\n" + data["message"] + "\nLe han dado like:")
# url = "https://graph.facebook.com/v3.0/{}/likes/?access_token={}".format(COMMENT_ID, PAGE_TOKEN)
# data = json.loads((requests.get(url)).content.decode("utf8"))
# for name in data["data"]:
# 	print(name["name"])
