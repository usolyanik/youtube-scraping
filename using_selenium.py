# -*- coding: utf-8 -*-

import re
from pprint import pprint as pp
import time
import inspect

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys

from log import Log
from debug import Debug

def line_num():
    print(inspect.currentframe().f_back.f_lineno)

binary = FirefoxBinary('/usr/bin/firefox')
url = 'https://www.youtube.com/watch?v=p9DWfW2JYs8'
page_load_timeout = 120

try:
            
    driver = webdriver.Firefox(firefox_binary=binary)
    driver.set_page_load_timeout(page_load_timeout)
    driver.get(url)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#    driver.execute_script('data.countText()')
    
    #views_class = 'view-count style-scope yt-view-count-renderer'
    comments_class = 'count-text style-scope ytd-comments-header-renderer'
    #comments_class = 'ytd-comments-header-renderer'
    #for view_num in driver.find_elements_by_class_name(views_class):
    #    print 'Number of views: ' + view_num.text.replace(' views', '')
    
    source = None
#    element = WebDriverWait(driver, page_load_timeout).until(
#        EC.presence_of_element_located((By.CLASS_NAME, 
#                                        comments_class)))
    
#    WebDriverWait(driver, page_load_timeout)
#
#    
#    element = driver.find_element_by_class_name(comments_class)
#    element.location_once_scrolled_into_view
#    element.send_keys(Keys.END)
    
    SCROLL_PAUSE_TIME = 0.5

    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
#    driver.execute_script('data.countText()')
    
    line_num()
    page = driver.find_element_by_tag_name('body')
    for i in range(10):
        page.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
    line_num()
    
    source = driver.page_source
    
#    for comment_num in driver.find_elements_by_class_name(comments_class):
#        print u'Number of comments: ' + comment_num.text
except:
    print('except')
    source = driver.page_source
    Debug.print_exception_info()
finally:
    try:
        print('finally')
        driver.quit()
    except:    
        Debug.print_exception_info()

#rex = comments_class + r'[~>]*?>([~<]*?)<'
#arr = re.findall(rex, source)
#pp(arr)
line_num() 
p = source.find(comments_class)
print(source[p:p+150])




























