from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def get_cookies():

    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    #chrome_options.add_argument("--proxy-server=http://127.0.0.1:8080")
    #chrome_options.add_argument("--disable-extensions")
    #chrome_options.add_argument("--disable-gpu")
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
    driver.delete_all_cookies()
    #start_url = "https://www.funda.nl/en/koop/heel-nederland/"
    start_url = "https://www.funda.nl/en/koop/maastricht/huis-86655999-gersthegge-34/"
    driver.get(start_url)
    time.sleep(2)
    cookie_list = driver.get_cookies()
    cookie_dict = {}
    for cookie in cookie_list:
        cookie_dict[cookie['name']] = cookie['value']
    #driver.quit()

    return cookie_dict

#cookie_ = get_cookies()
#print(cookie_)

if __name__ == "__main__":
    cookie_dict = get_cookies()
    print(cookie_dict)