from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
from cred import theuser, thepassword


#chrome_options = Options()
#chrome_options.add_argument("--headless")

class Google:

    def __init__(self, username, password):

        self.driver = webdriver.Chrome()
        self.driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(5)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(4)
        self.driver.get('https://analytics.google.com/analytics/web/#/report-home/a146806591w208716095p201158238')
        sleep(8)
        self.driver.find_element_by_xpath(
            '//*[@id="reporting"]/div/div/div/ga-nav-link[3]/div/a/div/span/span').click()
        sleep(4)
        self.driver.find_element_by_xpath('//*[@id="reporting"]/div/div/div/ga-nav-link[3]/div[2]/div/div/ga-nav-link[2]/div/a/div/span/span').click()
        sleep(4)
        self.driver.find_element_by_xpath(
            '//*[@id="reporting"]/div/div/div/ga-nav-link[3]/div[2]/div/div/ga-nav-link[2]/div[2]/div/div/ga-nav-link[1]/div/report-link/a/div/span/span').click()
        sleep(5)
        self.driver.switch_to_frame('galaxyIframe')
        sleep(5)
        self.driver.find_element_by_id('AnnotationDrawer_drawer_button').click()
        # self.driver.find_element_by_xpath('//*[@id="AnnotationDrawer_drawer_button"]').click()
        sleep(5)
        self.driver.find_element_by_class_name('_GALN').click()
        sleep(4)
        self.driver.find_element_by_css_selector("._GANrb textarea").send_keys("hello world")
        sleep(4)
        self.driver.find_element_by_css_selector("._GAjb._GAWn b").click()
        #self.driver.close()

Google(theuser, thepassword)
