import requests
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent
import os

from script.han import read_first_character


def get_chaopin(chinese_character):
    base_url = "https://www.mogher.com/"
    full_url = base_url + chinese_character
    if full_url.strip() == base_url:
        return None

    # 检查文件是否存在
    file_path = f"source/{chinese_character}.html"
    if os.path.exists(file_path):
        # 读取文件内容
        with open(file_path, 'r') as file:
            file_contents = file.read()
            return extract_pinyin_list(file_contents)
    else:
        # 创建一个 UserAgent 对象
        ua = UserAgent()
        # 发送请求时设置随机 User-Agent
        headers = {'User-Agent': ua.random}
        response = requests.get(full_url, headers=headers)
        if response.status_code == 200:
            save_html(file_path, response.text)
            return extract_pinyin_list(response.text)
        else:
            print(f"Failed to query for {chinese_character}. Status code: {response.status_code}")
            return None


def extract_pinyin_list(text):
    pinyin_list = []
    soup = BeautifulSoup(text, 'html.parser')
    matching_trs = soup.find_all('tr', class_='region_pinyin_row')
    for tr in matching_trs:
        td_content = tr.find('td').text.strip()
        if td_content == "潮州":
            a_tags = tr.find_all('a', href=True, class_='round')
            for a_tag in a_tags:
                pinyin = a_tag.text.strip() \
                    .replace("文", "").replace("白", "").replace("姓", "") \
                    .replace("俗", "").replace("拟", "").replace("训", "").replace("又", "") \
                    .replace(" ", "").replace("\n", "")

                if pinyin != '':
                    pinyin_list.append(pinyin)
    return pinyin_list


def save_html(path, text):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)


def query_chaopyin(input_file_path, output_file_path):
    chinese_characters = read_first_character(input_file_path)
    count = 0
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for char in chinese_characters:
            if char.strip().isspace() == "" or len(char.strip()) == 0 or char == "":
                continue
            pinyin_list = get_chaopin(char)
            if pinyin_list:
                pinyin_str = ' '.join(pinyin_list)
                result = f"{char} {pinyin_str}\n"
                output_file.write(result)
                output_file.flush()
                print(result)
                time.sleep(0.01)
            if count % 200 == 0:
                time.sleep(1)
            count = count + 1
