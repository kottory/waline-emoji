import requests
import time
import json

url = 'http://api.bilibili.com/x/emote/package?business=reply&ids={}'

if __name__ == "__main__":
    max_id = 300
    id_list = []
    for id in range(max_id, 0, -1):
        re = requests.get(url.format(id))
        if '向晚' in re.text:
            print("Find! in id: {}", id)
            id_list.append(id)
        time.sleep(0.13)

    print(id_list)
