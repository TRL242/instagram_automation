from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, time

CHROME_DRIVER_PATH = YOUR CHROME DRIVER PATH
SIMILAR_ACCOUNT = INSTAGRAM ACCOUNT YOU WANT TO BECOME
INSTAGRAM_NAME = YOUR INSTAGRAM @
INSTAGRAM_PASSWORD = YOUR INSTAGRAM PASSWORD

chrome_driver_path = "/Users/cabs/Documents/chromedriver-2"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(2)
        username = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input')

        username.send_keys(INSTAGRAM_NAME)
        password.send_keys(INSTAGRAM_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()