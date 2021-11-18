import requests
import time
import json
import os
import random

url = 'http://api.bilibili.com/x/emote/package?business=reply&ids={}'
jiaran_list = [221, 245, 288, 237]


if __name__ == "__main__":
    for pid in jiaran_list:
        r = requests.get(url.format(pid))
        data = json.loads(r.text)['data']['packages'][0]
        emoji_list = data['emote']
        items = []
        assets_dir = data['text']
        for emoji in emoji_list:
            emoji_name = emoji['meta']['alias']
            filename = '{}.png'.format(os.path.join(
                assets_dir, "{}_{}".format(assets_dir, emoji_name)))
            if not os.path.exists(assets_dir):
                os.makedirs(assets_dir)
            if not os.path.exists(filename):
                try:
                    res = requests.get(emoji['url'])
                    img = res.content
                    with open(filename, 'wb') as f:
                        f.write(img)
                    items.append(emoji_name)
                    print("{} Done".format(emoji_name))
                except Exception as e:
                    print("{} error!".format(emoji_name))

                time.sleep(0.12)
            else:
                items.append(emoji_name)

        info = {
            "name": assets_dir,
            "prefix": assets_dir + '_',
            "type": "png",
            "icon": random.choice(items),
            "items": items
        }
        with open(os.path.join(assets_dir, "info.json"), 'w') as f:
            f.write(json.dumps(info, ensure_ascii=False))
