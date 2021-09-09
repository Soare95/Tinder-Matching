from selenium import webdrive
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time


FACEBOOK_EMAIL = "testpython195@gmail.com"
FACEBOOK_PASS = "Abcd12345678a!"

driver = webdriver.Chrome(r"D:\chromedriver.exe")
driver.get("https://tinder.com/")
driver.maximize_window()

time.sleep(1)
login_button = driver.find_element_by_xpath('//*[@id="u2005023502"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

time.sleep(1)
login_fb = driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div[1]/div/div[3]/span/div[2]/button')
login_fb.click()

time.sleep(1)
tinder_window = driver.window_handles[0]
fb_window = driver.window_handles[1]

time.sleep(3)
driver.switch_to.window(fb_window)
# agree_button = driver.find_element_by_id("u_0_8_IJ")
# agree_button.click()

time.sleep(1)
email_label = driver.find_element_by_id("email")
email_label.send_keys(FACEBOOK_EMAIL)

password_label = driver.find_element_by_id("pass")
password_label.send_keys(FACEBOOK_PASS)

fb_connect = driver.find_element_by_name("login")
fb_connect.click()

time.sleep(2)
driver.switch_to.window(tinder_window)

time.sleep(6)
allow_location = driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div/div/div[3]/button[1]')
allow_location.click()

time.sleep(1)
not_interested = driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div/div/div[3]/button[2]')
not_interested.click()

time.sleep(1)
accept_button = driver.find_element_by_xpath('//*[@id="u2005023502"]/div/div[2]/div/div/div[1]/button')
accept_button.click()

for photo in range(3):
    time.sleep(5)

    try:
        webdriver.ActionChains(driver).send_keys(Keys.RIGHT).perform()
        time.sleep(3)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    except NoSuchElementException:
        time.sleep(2)
