from requests_oauthlib import OAuth2Session
from requests import get, post, put, delete

# Получение access_token
# client_id = "ваш клиент ID"
# client_secret = "ваш client_secret"
# auth_url = "https://oauth.yandex.ru/authorize"
# token_url = "https://oauth.yandex.ru/token"
# oauth = OAuth2Session(client_id=client_id)
# authorization_url, state = oauth.authorization_url(auth_url, force_confirm="true")
# print("Перейдите по ссылке, авторизуйтесь и скопируйте код:", authorization_url)
# code = input("Вставьте одноразовый код: ")
# token = oauth.fetch_token(token_url=token_url,
#                           code=code,
#                           client_secret=client_secret)
# access_token = token["access_token"]
# print(access_token)
# https://profi.ifmo.ru/?state=KcFwRXziBfgdyXH90SkJOb7P4C7DkF&code=6344583&cid=pehzbv0gk3aa5wmpb076fpy3rm

# Тест API
# access_token = ''
# headers = {"Authorization": f"OAuth {access_token}"}
# r = get("https://cloud-api.yandex.net/v1/disk", headers=headers)
# print(r.json())

yp = 'ваш токен'
headers = {"Authorization": f"OAuth {yp}"}
# params = {"path": "Тест API"}
# r = put("https://cloud-api.yandex.net/v1/disk/resources", headers=headers, params=params)
# print(r)

params = {"path": "Тест API/mapp.txt"}
r = get("https://cloud-api.yandex.net/v1/disk/resources/upload",
        headers=headers, params=params)
href = r.json()["href"]
files = {"file": open("mapp.txt", "rt")}
r = put(href, files=files)
print(r)
