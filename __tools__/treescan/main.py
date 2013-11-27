#!/usr/bin/python


# core
import collections
import logging
import pprint
import time

# 3rd party
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# local
import login

pp = pprint.PrettyPrinter(indent=4)


base_url = 'https://karatbars.com'
login_url = base_url + '/index.php?page=login_1'
binary_url = base_url + '/members.php?page=binarytree'

driver = webdriver.Firefox()
driver.set_window_size(1200,1100)

driver.get(login_url)

driver.find_element_by_name('username').send_keys(login.username)
driver.find_element_by_name('password').send_keys(login.password)
driver.find_element_by_name('btn_login').click()

def bitcoins_top():
    return float(driver.find_element_by_class_name('balanceraw-BTC').text)

def bitcoins_bottom():
    return float(driver.find_element_by_class_name('symbol2-available').text)

def element_html(elem):
    #return elem.get_attribute('outerHTML')
    return driver.execute_script("return new XMLSerializer().serializeToString(arguments[0]);", elem);

SellOrder = collections.namedtuple('SellOrder', ['ask', 'amount'])

def loop_forever():
    while True: pass

def scroll_down():
    #driver.execute_script("window.scrollTo(0,Math.max(document.documentElement.scrollHeight,document.body.scrollHeight,document.documentElement.clientHeight));");
    driver.execute_script("window.scrollBy(250, 750)");

def search(username):
    driver.get(binary_url)
    wait = WebDriverWait(driver,20)
    search = wait.until(
        lambda driver:  driver.find_element_by_name('srch_name'))
    search.send_keys(username)

    driver.find_element_by_name('binarytreesearch').click()

    divs = wait.until(
        lambda driver: driver.find_elements_by_class_name('binary_text'))
    for div in divs:
        print "a found={0}".format(element_html(div))
        print div.text
    # tmp = a.get_attribute('onmouseover')
    # print tmp
    # return tmp

def main():
    search('bitcoin')
    loop_forever()

if __name__ == '__main__':
    main()
