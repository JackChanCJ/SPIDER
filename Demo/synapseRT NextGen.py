# coding=utf-8
__author__ = 'JACK_CHAN'

import os
import xlrd
from time import sleep
from selenium import webdriver


def open_jira():
    chromedriver = r"C:\Users\40846\AppData\Local\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver)
    # os.environ["webdriver.chrome.driver"] = chromedriver
    driver.get("jira.incardata.com.cn:8080/secure/Dashboard.jspa")
    driver.maximize_window()
    driver.find_element_by_xpath('//*[@id="login-form-username"]').send_keys('jchen@incarcloud.com')
    driver.find_element_by_xpath('//*[@id="login-form-password"]').send_keys('000000')
    driver.find_element_by_xpath('//*[@id="login"]').click()

    sleep(10)
    driver.close()
    driver.quit()


def read_excel():
    fours = r"C:\Users\40846\Documents\Tencent Files\408467753\FileRecv\测试相关文档\测试案例\广汽三菱4S端系统测试测试用例.xls"
    data = xlrd.open_workbook(fours)
    table = data.sheets()
    for i in data.get_sheet_names():
        print (i)










def main():
    pass


if __name__ == '__main__':
    read_excel()