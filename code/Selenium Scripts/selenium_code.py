import os
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
xpaths = {
           'email':         "//form[@id='ajax-login']/input[@id='email']",
           'password':      "//form[@id='ajax-login']/input[@id='password']",
           'submitButton':  "//form[@id='ajax-login']/button[@type='submit']",
           'writereviewButton':  "//div[@class='main-content-wrap main-content-wrap--full']/div[@class='top-shelf']/div[@class='content-container']/div[@class='biz-page-header clearfix']/div[@class='biz-page-header-right u-relative']/div[@class='biz-page-actions nowrap']",
           'postreviewbutton' : "//form[@id='review_rate_form']/div[@class='js-war-compose_survey-section ysection']/div/div/div[@class='arrange_unit nowrap']/p/button[@type='submit']"
           }
##desired_capabilities = DesiredCapabilities.FIREFOX.copy()
os.environ["PATH"] += ":/usr/local/bin"

desired_capabilities['marionette'] = True
driver = webdriver.Firefox(capabilities=desired_capabilities)
##driver = webdriver.PhantomJS()
##driver.set_window_size(1120, 550)
driver.get("https://www.yelp.com/login")
#assert "Log In to Yelp" in driver.find_element_by_xpath("//div[@class='login']/div[@class='signup-form-container']/div[@class='header']").get_attribute('innerHTML')


###TestCase- 1 (Logging In to YELP with UserName and Password)

#Write Username in Username TextBox
driver.find_element_by_xpath(xpaths['email']).send_keys('john.murrayk98@gmail.com')
#Write Password in password TextBox
driver.find_element_by_xpath(xpaths['password']).send_keys('@quickeasy01')
#Click Login button
driver.find_element_by_xpath(xpaths['submitButton']).click()
#assert "The email address or password you entered is incorrect." in driver.page_source
time.sleep(5)


###TestCase- 2 (Loading the business URL and click on write a review)
driver.get("https://www.yelp.com/biz/girl-and-the-goat-chicago")
write_box=driver.find_element_by_xpath(xpaths['writereviewButton'])
write_box.find_element_by_link_text("Write a Review").click()
time.sleep(5)
#assert

###TestCase- 3 (Write a Review)
driver.find_element_by_id('rating-2').click()
text_area_box=driver.find_element_by_id('review-text').send_keys("The food is great here and we have a lovely time. If you are visitng chicago this place is an absolute must to try!")
driver.find_element_by_xpath(xpaths['postreviewbutton']).click()
time.sleep(10)
driver.quit()
