# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    cacharro_x.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mrodrigu <mrodrigu@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/24 11:56:09 by mrodrigu          #+#    #+#              #
#    Updated: 2018/06/24 13:47:24 by mrodrigu         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import facebook
import json
import requests

PAGE_TOKEN = "EAACEdEose0cBAPJFHY4XoJ8RjZAPJ9uKKGZAOtZCFDyl0FSQIql3cHvJ68ysZALzVZBwpZBzId2ZAADYy8ghSNkoTybsqxDl0LZBpibBRWzjY29N2Omph4ibGGmXHEgZBvauuTZB2E00Vs0IarnFjLtiPdtwRQu0vVFZA9rXTZCzfZADtXceHHD8zR4fD02Js0k9ZAPUInsaEs4cZAxcgZDZD"
USER_TOKEN = "EAACEdEose0cBAG94NQGPZBPTApYTc32z59XEY2P4MzVgZCSjQtZAXmIQWSzo03ZAhujGi7ycxn30AFZBgq05lpZCxMHB6l18f2V8FMICEejOrUqqZAlsga89qmTC9jfnzAap0dr8SCw7kC3lLgVPF19BAPjWKphUD987AsEw5NuYak5nZBjD0yztsEZCROwJYNyQ8OWCbHe0h1AZDZD"
PAGE_ID = "371121376687075"
COMMENT_ID = "371121376687075_424570551342157"

# url = "https://graph.facebook.com/v3.0/{}/feed/?access_token={}".format(PAGE_ID, PAGE_TOKEN)
# peticion de informacion
url = "https://graph.facebook.com/v3.0/{}/?access_token={}&fields=message".format(COMMENT_ID, PAGE_TOKEN)
# carga en un json
data = json.loads((requests.get(url)).content.decode("utf8"))
print("Al post:\n" + data["message"] + "\nLe han dado like:")
url = "https://graph.facebook.com/v3.0/{}/likes/?access_token={}".format(COMMENT_ID, PAGE_TOKEN)
data = json.loads((requests.get(url)).content.decode("utf8"))
for name in data["data"]:
	print(name["name"])
