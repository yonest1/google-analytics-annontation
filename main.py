from selenium import webdriver
from time import sleep

from selenium.webdriver import DesiredCapabilities

from cred import theuser, thepassword

class Google:

    def __init__(self, username, password):

        self.driver = webdriver.Chrome()
        print("opening stackoverflow")
        self.driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
        #self.driver.get('https://www.evernote.com/Registration.action?referralSpecifier=mktgnwp_en_en_web_hpg_V00&offer=perm_mktgweb_cp_basic')
        sleep(8)
        self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        #self.driver.find_element_by_xpath('//*[@id="googleOauthButton"]/div/div').click()
        print("login with user/pw")
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(8)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(4)
        print("switching to analytics")
        self.driver.get('https://analytics.google.com/analytics/web/provision/#/report-home/a179551378w248167090p230262745/')
        sleep(8)
        self.driver.find_element_by_xpath(
            '//*[@id="reporting"]/div/div/div/ga-nav-link[3]/div/a/div/span/span').click()
        sleep(4)
        self.driver.find_element_by_xpath('//*[@id="reporting"]/div/div/div/ga-nav-link[3]/div[2]/div/div/ga-nav-link[2]/div/a/div/span/span').click()
        sleep(4)
        self.driver.find_element_by_xpath(
            '//*[@id="reporting"]/div/div/div/ga-nav-link[3]/div[2]/div/div/ga-nav-link[2]/div[2]/div/div/ga-nav-link[1]/div/report-link/a/div/span/span').click()
        sleep(5)
        print("opening iframe")
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
        print("done")
        #self.driver.close()

Google(theuser, thepassword)
