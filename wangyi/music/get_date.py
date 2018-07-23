# coding=utf-8
__author__ = 'JACK_CHAN'

import csv
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=1'
# 设置谷歌浏览器的无头模式
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(chrome_options=chrome_options)
# 打开一个csv文件并一行一行的写，建议使用编辑器或文本格式打开
# 默认win10系统下文件的编码格式为GB2312，用excel打开会乱码，这里编码格式为utf-8
csv_file = open("playlist.csv", "w+", newline='', encoding='utf-8')
writer = csv.writer(csv_file)
writer.writerow([str(datetime.datetime.now())])
writer.writerow(['标题', '播放数', '链接'])
# 解析每一页，直到下一页为空
while url != 'javascript:void(0)':
    driver.get(url)
    driver.switch_to.frame("contentFrame")
    # 找出所有包含歌单信息的元素存入data并进行遍历，找到nb（number boardcast）
    data = driver.find_element_by_id("m-pl-container").find_elements_by_tag_name("li")
    for i in range(len(data)):
        nb = data[i].find_element_by_class_name("nb").text
        if '万' in nb and int(nb.split("万")[0]) > 500:
            # 封面有title和url（href）
            msk = data[i].find_element_by_css_selector("a.msk")
            writer.writerow([msk.get_attribute('title'), nb, msk.get_attribute('href')])
    url = driver.find_element_by_css_selector("a.zbtn.znxt").get_attribute('href')
csv_file.close()



def main():
    pass

if __name__ == '__main__':
    main()