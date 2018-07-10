# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    cacharro_x.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mrodrigu <mrodrigu@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/24 11:56:09 by mrodrigu          #+#    #+#              #
#    Updated: 2018/07/10 14:59:13 by mrodrigu         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import json
import requests


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
