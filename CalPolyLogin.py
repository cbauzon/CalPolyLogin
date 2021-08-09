from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

def login_to_cal_poly(usr, passwd):
    browser = webdriver.Firefox()
    browser.get('https://my.calpoly.edu')
    usrfield = browser.find_element_by_id('username')
    usrfield.send_keys(usr)

    psswdfield = browser.find_element_by_id('password')
    psswdfield.send_keys(passwd + Keys.RETURN)

    if browser.title != 'My Cal Poly Portal: Home':
        browser.implicitly_wait(10)
        seq = browser.find_elements_by_tag_name("iframe")
        iframe = seq[0]
        browser.switch_to.frame(iframe)
        browser.implicitly_wait(30)
        buttonnum = browser.find_elements_by_tag_name('button')
        buttonnum[0].click()                                  
        buttonnum[0].click()
        

def get_creds():
    credentials = 'cpLoginCred.txt'
    if os.path.isfile(credentials) == False:
        f = open(credentials, 'x')
        f.write(input('What is your username? ') + '\n')
        f.write(input('What is your password? '))
        f.close()
    f = open(credentials, 'r')
    creds = f.read().splitlines()
    return creds
    

if __name__ == '__main__':
    creds = get_creds()
    login_to_cal_poly(creds[0], creds[1])