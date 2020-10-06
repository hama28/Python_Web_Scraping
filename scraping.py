import requests
from bs4 import BeautifulSoup

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
            data_list.append(url.get('href'))
            data_list.append(user.getText())
            data_list.append(keisai.getText())
            hatebu_array.append(data_list)
        else:
            next

    return hatebu_array