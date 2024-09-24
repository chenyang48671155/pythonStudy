# /*
# * @Author: UniversalSpaceman-Chenyang 
# * @Date: 2024-09-24 16:43:23 
# * @Last Modified by: UniversalSpaceman-Chenyang
# * @Last Modified time: 2024-09-24 16:49:48
# */

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
print(browser.page_source)
browser.close()