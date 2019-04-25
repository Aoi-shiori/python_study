# coding =utf-8
import  time
from selenium import webdriver
browser =webdriver.Chrome()
browser.get("http://www.baidu.com")
browser.find_element_by_xpath("//*[@id='kw']").send_keys("今天天气")
browser.find_element_by_xpath("//*[@id ='su']").click()
time.sleep(3)

#判断元素中是否有我们需要的值“今天天气”，is.displayed用于判断元素在页面中是否存在，返回的是布尔类型，存在true，否则false
if browser.find_element_by_xpath("// div / h3 / a /../ a / em[text() ='今天天气']").is_displayed():
    print("测试成功，结果和预期结果匹配！")
    browser.quit()
else:
    print("结果不符合预期")