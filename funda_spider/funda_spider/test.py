from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,nl;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.funda.nl',
    'Referer': 'https://www.funda.nl/en/koop/',
    'Upgrade-Insecure-Requests': '1'
}



chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
#chrome_options.add_argument("--proxy-server=http://127.0.0.1:8080")
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
agent = driver.execute_script("return navigator.userAgent")
driver.delete_all_cookies()
start_url = "https://www.funda.nl/en/koop/heel-nederland/"
driver.get(start_url)
time.sleep(60)
print(agent)
'''
time.sleep(5)
cookie_list = driver.get_cookies()
cookie_dict = {}5
for cookie in cookie_list:
    if cookie['name'] != 'Cookie':
        cookie_dict[cookie['name']] = cookie['value']
#driver.quit()

return cookie_dict

#cookie_ = get_cookies()
#print(cookie_)

if __name__ == "__main__":
    cookie_dict = get_cookies()
    print(cookie_dict)
    '''