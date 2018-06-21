# coding=utf-8
__author__ = 'JACK_CHAN'

import os
import openpyxl
from time import sleep
from selenium import webdriver

class jira:
    def __init__(self):
        pwd = os.getcwd()
        chromedriver_dir = pwd + '\环境\chromedriver.exe'
        chromedriver = r"C:\Users\40846\AppData\Local\Google\Chrome\Application\chromedriver.exe"
        self.driver = webdriver.Chrome(chromedriver_dir)
        self.driver.implicitly_wait(30)
        # os.environ["webdriver.chrome.driver"] = chromedriver
        jira_url = "jira.incardata.com.cn:8080/secure/Dashboard.jspa"
        self.driver.get(jira_url)
        self.driver.maximize_window()

    def open_jira(self):
        self.driver.find_element_by_xpath('//*[@id="login-form-username"]').send_keys('jchen@incarcloud.com')
        self.driver.find_element_by_xpath('//*[@id="login-form-password"]').send_keys('000000')
        self.driver.find_element_by_xpath('//*[@id="login"]').click()

    # def open_needs(self):
    #     self.driver.find_element_by_xpath('//a[@id="browse_link"]').click()
    #     self.driver.find_element_by_xpath('//a[@id="admin_main_proj_link_lnk"]').click()
    #     self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div[1]/nav/div/div[2]/ul/li[9]/a').click()



    def create_needs(self, needs, module, remarks):
        # 新建需求
        self.needs = needs
        self.module = module
        self.remarks = remarks

        self.driver.find_element_by_xpath('//a[@id="create_link"]').click()
        self.driver.find_element_by_xpath('//input[@id="issuetype-field"]').clear()
        self.driver.find_element_by_xpath('//input[@id="issuetype-field"]').send_keys('需求')
        self.driver.find_element_by_xpath('//input[@id="summary"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//input[@id="summary"]').send_keys(self.needs)        # 概要 = needs
        self.driver.find_element_by_xpath('//textarea[@id="versions-textarea"]').click()

        self.driver.find_element_by_xpath('//textarea[@id="versions-textarea"]').send_keys('App 1.0')       # 影响版本
        self.driver.find_element_by_xpath('//*[@id="components-textarea"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="components-textarea"]').send_keys(self.module)       # 模块 = module
        self.driver.find_element_by_xpath('//*[@id="tinymce"]/p').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="tinymce"]/p').send_keys(self.remarks)        # 描述 = remarks
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="create-issue-dialog"]/div[2]/div[1]/div/form/div[2]/div/a').click()




def read_excel():
    fours = r"C:\Users\40846\Desktop\自动化数据\车主APP.xlsx"
    wb = openpyxl.load_workbook(fours)
    sheet = wb['手机APP']
    for row in sheet.rows:
        return row[1].value, row[2].value, row[3].value, row[4].value










def main():

    J = jira()
    read_excel()
    J.open_jira()
    J.create_needs()

    pass


if __name__ == '__main__':
    main()