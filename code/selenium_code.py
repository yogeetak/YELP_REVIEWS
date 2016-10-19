import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
xpaths = {
           'email':         "//form[@id='ajax-login']/input[@id='email']",
           'password':      "//form[@id='ajax-login']/input[@id='password']",
           'submitButton':  "//form[@id='ajax-login']/button[@type='submit']",
           'writereview' :  "//div[@class='main-content-wrap main-content-wrap--full']/div[@class='top-shelf']/div[@class='content-container']/div[@class='biz-page-header clearfix']/div[@class='biz-page-header-right u-relative']/div[@class='biz-page-actions nowrap']",
            'selectrating':  "//fieldset[@class='star-rating-widget inline-block']/ul[@class='stars-1']/li/input[@id='rating-1']"
         }
#'selectrating':  "//form[@id='review_rate_form']/div[@class='write-review integrated-rating-comment ysection js-war-compose_review-section expanded']/div[@class='js-character-counter']/div[@class='rating-and-comment pseudo-input']/div[@class='arrange arrange--middle']/div[@class='arrange_unit arrange_unit--fill']/div[@class='clearfix']/fieldset[@class='star-rating-widget inline-block']/ul[@class='stars-1']/li/input[@id='rating-1']"

desired_capabilities = DesiredCapabilities.FIREFOX.copy()
os.environ["PATH"] += ":/usr/local/bin"

desired_capabilities['marionette'] = True
driver = webdriver.Firefox(capabilities=desired_capabilities)
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


###TestCase- 2 (Loading the business URL and click on writing a review)
driver.get("https://www.yelp.com/biz/girl-and-the-goat-chicago")
write_box=driver.find_element_by_xpath(xpaths['writereview'])
write_box.find_element_by_link_text("Write a Review").click()
#assert

###TestCase- 3 (Click on a rating)
ratingli=write_box=driver.find_element_by_xpath(xpaths['selectrating']).click()


time.sleep(10)
driver.quit()
