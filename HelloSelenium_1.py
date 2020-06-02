from selenium import webdriver
import time
import re
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

browser = webdriver.Chrome()
url = 'https://wallhaven.cc/'
browser.get(url)

input_ = browser.find_element_by_id('search-text') #获取输入框元素
input_.send_keys('Makise Kurisu') #输入要搜索的名称
time.sleep(2) #睡两秒
button_ = browser.find_element_by_xpath('//*[@id="startpage-search"]/div/button') #获取搜索按钮元素
button_.click() #进行点击

text = browser.page_source # 获取页面信息
pattern = re.compile(r'<a class="preview" href="(.*?)" target="_blank">')
res = re.findall(pattern,text) # 正则表达式匹配
for i in res:
    browser.get(i)
    time.sleep(3)
    pic = browser.find_element_by_xpath('//*[@id="wallpaper"]')
    action = ActionChains(browser).move_to_element(pic)  # 移动到该元素
    action.context_click(pic)  # 右键点击该元素
    action.perform() # 执行
    pyautogui.typewrite(['v']) # 敲击V进行保存
    # 单击图片另存之后等1s敲回车
    time.sleep(1)
    pyautogui.typewrite(['enter'])

time.sleep(10)
browser.close()