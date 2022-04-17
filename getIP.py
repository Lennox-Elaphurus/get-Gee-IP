# encoding:UTF-8
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Log:
    def __init__(self):
        self.pwd = "password"
        self.gee_version = "system version"

    def login(self):

        option = webdriver.ChromeOptions()
        option.add_argument('--disable-infobars')
        option.add_argument("--disable-extensions")
        option.add_argument("--disable-gpu")
        option.add_argument("--disable-dev-shm-usage")
        option.add_argument("--no-sandbox")
        # option.add_argument("--headless")
        # 如果配置环境变量可以不写绝对路径
        wd = webdriver.Chrome(options=option)
        wd.get("http://192.168.1.1/")
        wait = WebDriverWait(wd, 300)
        wd.implicitly_wait(30)  # 设置隐式等待
        # print("finish init webdriver")

        wd.find_element_by_xpath("//*[@id='bd']/div/div/input[1]").send_keys(self.pwd)
        time.sleep(0.5)
        try:
            wait.until(ec.visibility_of(wd.find_element_by_id("submit"))).click()
        except Exception as e:
            print(e.args)
        # print("finish login")

        wait.until(ec.visibility_of(wd.find_element_by_xpath("//*[@id='ment_system']"))).click()
        # print("click ment_system")

        wait.until(ec.text_to_be_present_in_element(("id", "current_sys_board_info"), self.gee_version))
        time.sleep(0.5)
        ip = wd.find_element_by_xpath("//*[@id='wan_ip_v4']/td[2]/span").text
        ip = ip.split()[0]
        print(ip)

        wd.quit()


if __name__ == "__main__":
    loging = Log()
    loging.login()
