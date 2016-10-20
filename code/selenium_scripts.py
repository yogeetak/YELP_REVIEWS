import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
xpaths = {
           'email':     "//form[@id='ajax-login']/input[@id='email']",
           'password':  "//form[@id='ajax-login']/input[@id='password']",
           'submitButton' :   "//form[@id='ajax-login']/button[@type='submit']"
         }

class TestOne(unittest.TestCase):
    def setUp(self):
        os.environ["PATH"] += ":/usr/local/bin"
        desired_capabilities = DesiredCapabilities.FIREFOX.copy()
        desired_capabilities['marionette'] = True
        self.driver = webdriver.Firefox(capabilities=desired_capabilities)
               
    def login_test(self):
        print("hello")
        self.driver.get("https://www.yelp.com/login")
        self.assertIn("Log In to Yelp",self.driver.title)
        #Write Username in Username TextBox
        self.driver.find_element_by_xpath(xpaths['email']).send_keys('john.murrayk98@gmail.com')
        #Write Password in password TextBox
        self.driver.find_element_by_xpath(xpaths['password']).send_keys('@')
        #Click Login button
        self.driver.find_element_by_xpath(xpaths['submitButton']).click()
        time.sleep(2)
        self.assertIn("The email address or password you entered is incorrect.",self.driver.page_source)


    def tearDown(self):
        self.driver.quit()
    
       
if __name__ == '__main__':
    print("hemml")
    unittest.main()
    self= setUp();
    login_test(self);



