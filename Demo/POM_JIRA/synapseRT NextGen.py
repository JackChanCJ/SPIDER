# coding=utf-8
__author__ = 'JACK_CHAN'

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
    fours = r"C:\Users\40846\Desktop\自动化数据\车主APP.xlsx"
    data = xlrd.open_workbook(fours)
    table = data.sheets()
    for i in data.get_sheet_names():
        print (i)










def main():
    open_jira()
    read_excel()
    pass


if __name__ == '__main__':
    main()