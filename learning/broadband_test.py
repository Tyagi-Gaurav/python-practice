import time

from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By

PROMISED_DOWN = 300
PROMISED_UP = 250


class InternetSpeedEmailBot:
    def __init__(self):
        # Keep Chrome Browser open
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        try:
            self.driver.get("https://www.speedtest.net/")
            time.sleep(3)

            go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
            go_button.click()

            time.sleep(60)
            self.up = self.driver.find_element(By.XPATH,
                                               value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
            self.down = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

            print (self.up)
            print (self.down)
        except WebDriverException as exception:
            print(exception)


def email(self, download, upload):
    pass


def quit(self):
    self.driver.close()
    self.driver.quit()


bot = InternetSpeedEmailBot()
bot.get_internet_speed()

bot.quit()
