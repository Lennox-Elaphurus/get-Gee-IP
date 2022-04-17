# encoding:UTF-8
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Log:
    def __init__(self):
        self.pwd = "password"
        self.gee_version = "system version"
        self.gee_url = "http://192.168.199.1/"

    def login(self):

        option = webdriver.ChromeOptions()
        option.add_argument('--disable-infobars')
        option.add_argument("--disable-extensions")
        option.add_argument("--disable-gpu")
        option.add_argument("--disable-dev-shm-usage")
        option.add_argument("--no-sandbox")
        option.add_argument("--headless")
        wd = webdriver.Chrome(options=option)
        wd.get(self.gee_url)
        wait = WebDriverWait(wd, 300)
        wd.implicitly_wait(30)  # 设置隐式等待
        # print("finish init webdriver")

        wd.find_element(By.XPATH, "//*[@id='bd']/div/div/input[1]").send_keys(self.pwd)
        time.sleep(0.5)

        wait.until(ec.visibility_of(wd.find_element(By.ID, "submit"))).click()
        # print("finish login")

        wait.until(ec.visibility_of(wd.find_element(By.XPATH, "//*[@id='ment_system']"))).click()
        # print("click ment_system")

        wait.until(ec.text_to_be_present_in_element(("id", "current_sys_board_info"), self.gee_version))
        time.sleep(0.5)
        ip = wd.find_element(By.XPATH, "//*[@id='wan_ip_v4']/td[2]/span").text
        ip = ip.split()[0]
        print(ip)

        wd.quit()


if __name__ == "__main__":
    try:
        loging = Log()
        loging.login()
    except Exception as e:
        print(e.args)
