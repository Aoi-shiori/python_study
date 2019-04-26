# coding =utf-8
import  time
from selenium import webdriver
browser =webdriver.Chrome()
#browser2=webdriver.android
browser.get("http://www.baidu.com")
browser.find_element_by_xpath("//*[@id='kw']").send_keys("今天天气")
browser.find_element_by_xpath("//*[@id ='su']").click()
input =browser.find_element_by_id("kw")

print(input.tag_name)
print(input.text)
print(input.id)
print(input.size)
print(input.location)
browser.implicitly_wait(3) #隐式等待，需要的元素没有出来，等待的时间

time.sleep(3)
#targe =browser.switch_to_frame()#切换到子元素
#browser.switch_to_parent() #切换到父元素
# browser.back()#后退
# browser.forward() #前进
# browser.close() #关闭
#判断元素中是否有我们需要的值“今天天气”，is.displayed用于判断元素在页面中是否存在，返回的是布尔类型，存在true，否则false
if browser.find_element_by_xpath("// div / h3 / a /../ a / em[text() ='今天天气']").is_displayed():
    print("测试成功，结果和预期结果匹配！")
    browser.quit()
else:
    print("结果不符合预期")

#cookis处理
# browser=webdriver.chrome
# #↓↓↓------获取html----↓↓↓
# browser.get("www.baidu.com")
# #↓↓↓------获取并打印cookis----↓↓↓
# print(browser.get_cookies())
# #↓↓↓------在cookis中添加内容----↓↓↓
# browser.add_cookie('name':'name','domain':'www.baidiu.com','value':'germey')#
# #↓↓↓------打印获取的cookis----↓↓↓
# print(browser.get_cookies())
# #↓↓↓------删除cookis----↓↓↓↓↓↓
# browser.delete_all_cookies()
# #↓↓↓------打印获取的cookis----↓↓↓
# print(browser.get_cookies())

#选项卡管理
# browser=webdriver.chrome
# browser.get("www.baidu.com")
# browser.execute_script('windwos.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# browser.get('www.taobao.com')
# time.sleep(2)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https:/python.org')

#异常处理
# browser=webdriver.chrome()
# browser.get('www.baidu.com')
# browser.find_element_by_id('hello')
# from selenium.common.exceptions import TimeoutException,NoSuchElementException
# browser=webdriver.chrome()
# try:
#     browser.get('www.baidu.com')
# except TimeoutException:
#     print('Time out')
# try:
#     browser.find_element_by_id('hello')
# except NoSuchElementException:
#     print("NO Element")
# finally:
#     browser.close()