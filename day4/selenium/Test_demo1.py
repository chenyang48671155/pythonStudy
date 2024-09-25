from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://www.pinterest.com/")
browser.maximize_window()

title = browser.title

print(title)

browser.close()