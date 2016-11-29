import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
xpaths = {
           'email':     "//form[@id='ajax-login']/input[@id='email']",
           'password':  "//form[@id='ajax-login']/input[@id='password']",
           'submitButton' :   "//form[@id='ajax-login']/button[@type='submit']",
           'writereviewButton':  "//div[@class='main-content-wrap main-content-wrap--full']/div[@class='top-shelf']/div[@class='content-container']/div[@class='biz-page-header clearfix']/div[@class='biz-page-header-right u-relative']/div[@class='biz-page-actions nowrap']",
           'postreviewbutton' : "//form[@id='review_rate_form']/div[@class='js-war-compose_survey-section ysection']/div/div/div[@class='arrange_unit nowrap']/p/button[@type='submit']"
         }
#john.murrayk98@gmail.com @quickeasy01
#murray.ptr12@gmail.com   @quickeasy02
class TestOne(unittest.TestCase):
    def setUp(self):
        os.environ["PATH"] += ":/usr/local/bin"
        desired_capabilities = DesiredCapabilities.FIREFOX.copy()
        desired_capabilities['marionette'] = True
        self.driver = webdriver.Firefox(capabilities=desired_capabilities)
        ##driver = webdriver.PhantomJS()
        ##driver.set_window_size(1120, 550)
               
    ###TestCase- 1 (Logging In to YELP with UserName and Password)
    def test_login(self):
        self.driver.get("https://www.yelp.com/login")
        try:
            self.assertTrue('Log In - Yelp',self.driver.title)

            #Write Username & Password in Username TextBox
            self.driver.find_element_by_xpath(xpaths['email']).send_keys('john.murrayk98@gmail.com')
            self.driver.find_element_by_xpath(xpaths['password']).send_keys('@quickeasy01')
            #Click Login button
            self.driver.find_element_by_xpath(xpaths['submitButton']).click()
            
            ##wait for the log in page to load
            element = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, 'home-link')))
   
            ##Load Business URL
            self.driver.get("https://www.yelp.com/biz/girl-and-the-goat-chicago")
            write_box=self.driver.find_element_by_xpath(xpaths['writereviewButton'])
            write_box.find_element_by_link_text("Write a Review").click()
            ##wait for the write review page to load
            element = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, 'review_rate_form')))

            self.driver.find_element_by_id('rating-2').click()
            text_area_box=self.driver.find_element_by_id('review-text').send_keys("The food is great here and we have a lovely time. If you are visitng chicago this place is an absolute must to try!")
            self.driver.find_element_by_xpath(xpaths['postreviewbutton']).click()
            time.sleep(5)
            self.driver.assertIn('is now live!',self.driver.page_source)

        finally:
            if(self.driver.find_element_by_id('recaptcha-anchor-label')):
                print("Faced With a Captcha for User Login")
            else:
                print("Issue in writing review for business")
            #self.driver.quit()
            
    def tearDown(self):
        time.sleep(10)
        #self.driver.quit()
    
       
if __name__ == '__main__':
    unittest.main()



