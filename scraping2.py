from datetime import datetime
from http import client
from google.cloud import datastore
import requests
from bs4 import BeautifulSoup

# 親データの追加
def insert(target, users):
    client = datastore.Client()
    key = client.key("ScrapingList")
    entity = datastore.Entity(key=key)
    entity["target"] = target
    entity["over_num"] = users
    entity["created"] = datetime.now()
    client.put(entity)
    entity['id'] = entity.key.id

    return entity.key.id

# 子データの追加
def insert_descendant(parent_id, web_array):
    for web in web_array:
        client = datastore.Client()
        parent_key = client.key('ScrapingList', int(parent_id))
        key = client.key('GetScrapingData', parent=parent_key)
        entity = datastore.Entity(key=key)
        entity['title'] = web[0]
        entity['users'] = web[1]
        entity['web_name'] = web[2]
        entity['url'] = web[3]
        client.put(entity)
        entity['id'] = entity.key.id
    return entity


def get_hatebu(users):
    hatebu_array = []

    r = requests.get('http://b.hatena.ne.jp/')
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.select("div.entrylist-contents-main"):
        title = div.h3
        url = div.a
        user = div.span
        user_num = user.getText().split(" ")
        keisai = div.p

        if int(user_num[0]) >= int(users):
            data_list = []
            data_list.append(title.getText())
            data_list.append(user_num[0])
            data_list.append(keisai.getText())
            data_list.append(url.get('href'))
            hatebu_array.append(data_list)
        else:
            next

    return hatebu_array