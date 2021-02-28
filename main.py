from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
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
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        def follow(self):
            all_buttons = self.driver.find_elements_by_css_selector("li button")
            for button in all_buttons:
                try:
                    button.click()
                    time.sleep(1)
                except ElementClickInterceptedException:
                    cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                    cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()