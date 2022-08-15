from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import requests,uuid,time,random,subprocess,os
from faker import Faker

# 代理IP地址
proxyUrl = ''
url = 'https://www.wjx.cn/vm/mZ6GXCt.aspx'

while True:
    fake = Faker(locale='zh_CN')
    # 随机中文名字
    name = fake.name()
    chromeoption = webdriver.ChromeOptions()
    proxyIp = requests.get(proxyUrl).text
    if '套餐最高调用频率为1秒!' in proxyIp:
        time.sleep(1)
        proxyIp = requests.get(proxyUrl).text

    chromeoption.add_argument('--proxy-server=http://'+proxyIp)
    print(proxyIp)
    driver = webdriver.Chrome()  
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })

    driver.get(url)
    # 等待两秒加载网页
    time.sleep(1)

    driver.find_element_by_name("q1").send_keys("23计" + str(random.randint(1,6)))
    driver.find_element_by_name("q2").send_keys(name)

    radios = driver.find_elements_by_class_name("ui-radio")
    radios[random.randint(0,len(radios)-1)].click()

    file_inputs = driver.find_elements_by_css_selector("input[type='file']")
    file_inputs[0].send_keys("E:\\wenjuan\\start.png")
    # 延迟10ms
    time.sleep(1)
    file_inputs[1].send_keys("E:\\wenjuan\\start.png")
    time.sleep(1)
    # 点击class为ctlNext的按钮
    driver.find_element_by_id("ctlNext").click()
    time.sleep(1)
    # 获取浏览器dom
    try:
        dom = driver.page_source
        if '点击按钮开始智能验证' in dom:
            buttons = driver.find_elements_by_class_name("mainColor")
            buttons[2].click()
            div  = driver.find_element_by_id("SM_TXT_1")
        
            driver.execute_script("arguments[0].click();", div)
            time.sleep(4)
            dom = driver.page_source
            if '请按住滑块，拖动到最右边' in dom:
                btn = driver.find_element_by_id("nc_1_n1z")
                ActionChains(driver).drag_and_drop_by_offset(btn, 400, 0).perform()

                time.sleep(2)
                dom = driver.page_source
                if '哎呀，出错了，点击' in dom:
                    btn = driver.find_element_by_id("nc_1_refresh1")
                    driver.execute_script("arguments[0].click();", btn)
                    btn = driver.find_element_by_id("nc_1_n1z")
                    ActionChains(driver).drag_and_drop_by_offset(btn, 400, 0).perform()
                    time.sleep(2)

    except Exception as e:
        driver.quit()
        print("发生错误")
        pass

    driver.quit()
    print("已完成")