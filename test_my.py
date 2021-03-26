# __**__ coding=utf-8 __**__
# 作者：calm_zn
# 日期：2021/3/25 17:14
# 工具：PyCharm
# Python版本：3.7

from selenium import webdriver
from options.options import Options

driver = webdriver.Chrome(options=Options().chrome_options())
driver.get('https://www.100.nxdev.cn/')
driver.implicitly_wait(10)
driver.find_element('xpath', '/html/body/div/div[1]/div/div[2]').click()
driver.find_element()
