#!/usr/bin/python


# core
import collections
import logging
import pprint
import re
import sys
import time

# 3rd party
import argh
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# local
sys.path.append('../..')
import email_rst
import login
import myapp


pp = pprint.PrettyPrinter(indent=4)


base_url = 'https://karatbars.com'
login_url = base_url + '/index.php?page=login_1'
binary_url = base_url + '/members.php?page=binarytree'
units_url = base_url + '/members.php?page=binaryunits'

driver = None

def start_browser():
    global driver
    driver = webdriver.Firefox()
    driver.set_window_size(1200,1100)

    driver.get(login_url)

    driver.find_element_by_name('username').send_keys(login.username)
    driver.find_element_by_name('password').send_keys(login.password)
    driver.find_element_by_name('btn_login').click()

def loop_forever():
    while True: pass

def echo_text(data, label):
    print '{0}={1}.'.format(label, data)

def echo_html(elem, label):
    print '{0}={1}.'.format(label, element_html(elem))

def element_html(element):
    return driver.execute_script(
        "return arguments[0].outerHTML || new XMLSerializer().serializeToString(arguments[0]);", element)

def scroll_down():
    #driver.execute_script("window.scrollTo(0,Math.max(document.documentElement.scrollHeight,document.body.scrollHeight,document.documentElement.clientHeight));");
    driver.execute_script("window.scrollBy(250, 750)");

def parse_user(s):
    print "parse-user-input=" + s
    user_re = re.compile(
        '(\w+): ([^<]+)<br>'
        )
    data = user_re.findall(s)
    print "data={0}".format(data)
    return data

def email(username):
    user, sponsor = search(username)
    email_rst.main(
        user['Username'], user['Email'], user['Name'],
        sponsor['Username'], sponsor['Email']
        )

def _search(username):
    driver.get(binary_url)
    wait = WebDriverWait(driver,20)
    search = wait.until(
        lambda driver:  driver.find_element_by_name('srch_name'))
    search.send_keys(username)

    driver.find_element_by_name('binarytreesearch').click()

    divs = wait.until(
        lambda driver: driver.find_elements_by_class_name('binary_text'))
    div = divs[0]
    print "div={0}.".format(element_html(div))
    as_ = div.find_elements_by_xpath('../a')
    for a in as_:
        a_html = element_html(a)
        print "A_HTML=" + a_html
        user = parse_user(a_html)
        if len(user):
            return dict(user)

def search(username, stay=False):
    start_browser()
    user = _search(username)
    print "user={0}.".format(pp.pformat(user))
    if stay:
        loop_forever()
    sponsor = _search(user['Sponsor'])
    return user, sponsor

def register(username):
    user, sponsor = search(username)
    skype=''
    myapp.ToolsRegister.insert_and_email_affiliate(
        user['Email'], user['Username'], user['Name'], user['Phone'],
        skype,
        sponsor['Username'], sponsor['Email'],
        'http://j.mp/17y4bFj')

def units():
    start_browser()
    driver.get(units_url)
    driver.find_element_by_class_name('sorting_asc').click()
    select = Select(
        driver.find_element_by_name('cab_comm_history_table_length'))
    select.select_by_visible_text('50')
    loop_forever()


if __name__ == '__main__':
    parser = argh.ArghParser()
    parser.add_commands([email, search, register, units])
    parser.dispatch()
