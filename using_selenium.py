# -*- coding: utf-8 -*-

import re
from pprint import pprint as pp
import time
import inspect

from selenium import webdriver
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys

from log import Log
from debug import Debug

binary = FirefoxBinary('/usr/bin/firefox')
url = 'https://www.youtube.com/watch?v=p9DWfW2JYs8'
page_load_timeout = 120
scrolling_timeout = 120

views_class= 'view-count style-scope yt-view-count-renderer'
comments_class = 'count-text style-scope ytd-comments-header-renderer'

rex_views = views_class + r'.{150}'
rex_comments = comments_class + r'.{150}'

def line_num():
    print(inspect.currentframe().f_back.f_lineno)
    
def get_views_num(html):
    lst = re.findall(rex_views, html)
    return lst[0]

def get_comments_num(html):
    lst = re.findall(rex_comments, html)
    return lst[0]
#########################################################################

try:
            
    driver = webdriver.Firefox(firefox_binary=binary)
    driver.set_page_load_timeout(page_load_timeout)
    driver.get(url)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    source = None

    page = driver.find_element_by_tag_name('body')
    for i in range(10):
        page.send_keys(Keys.PAGE_DOWN)
        time.sleep(scrolling_timeout)
        source = driver.page_source
        views_num = get_views_num(source)
        comments_num = get_comments_num(source)
        print(comments_num)
        if 'text="[[data.count' in comments_num: 
            continue
        else:
            break

except:
    print('except')
    source = driver.page_source
    Log.write(Debug.exception_info(), print_it=True)
finally:
    try:
        print('finally')
        driver.quit()
    except:    
        Log.write(Debug.exception_info(), print_it=True)

#rex = comments_class + r'[~>]*?>([~<]*?)<'
#arr = re.findall(rex, source)
#pp(arr)

p = source.find(comments_class)
print(source[p:p+150])


#data.countText


























