import p_20
import re

text = p_20.get_UK_text()

template = re.findall('\|(.+?)\s=\s*(.+)', text)

delete_template = []
for field, value in template:
    cleaned_value = re.sub("''+", "", value)
    #cleaned_value = re.sub("\'{2,}(.+?)\'{2,}", "\\1", value)
    cleaned_value_2 = re.sub("\[\[(.+?)\]\]", "\\1", cleaned_value)
    cleaned_value_3 = re.sub("\[(.+?)\]", "\\1", cleaned_value_2)
    cleaned_value_4 = re.sub("\*+(.+?)", "\\1", cleaned_value_3)
    cleaned_value_5 = re.sub("\:+(.+?)", "\\1", cleaned_value_4)
    cleaned_value_6 = re.sub("\{\{(.+?)\}\}", "\\1", cleaned_value_5)
    delete_template.append((field, cleaned_value_6))

import requests

flag_image_file = None
for field, value in delete_template:
    if field == '国旗画像':
        flag_image_file = value
        break

# MediaWiki APIのエンドポイント
url = "https://commons.wikimedia.org/w/api.php"

# APIに渡すパラメータを設定
params = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": "File:" + flag_image_file,
    "iiprop": "url"
}

# APIを呼び出し
response = requests.get(url, params=params)

# レスポンスから国旗画像のURLを取得
data = response.json()
pages = data["query"]["pages"]
for _, page in pages.items():
    flag_image_url = page["imageinfo"][0]["url"]

print(flag_image_url)

