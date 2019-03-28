# -*- coding: utf-8 -*-

import re
from pprint import pprint as pp
import time
import inspect

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys

from log import Log
from debug import Debug

binary = FirefoxBinary('/usr/bin/firefox')
url = 'https://www.youtube.com/watch?v=p9DWfW2JYs8'
page_load_timeout = 120
scrolling_timeout = 2

views_class= 'view-count style-scope yt-view-count-renderer'
comments_class = 'count-text style-scope ytd-comments-header-renderer'

reg_expr_views = views_class + r'.{150}'
reg_expr_comments = comments_class + r'.{150}'

def line_num():
    print(inspect.currentframe().f_back.f_lineno)
    
def get_value_html(reg_expr, html):
    if not html:
        return ''
    lst = re.findall(reg_expr, html)
    if len(lst) > 0:
        return lst[0]
    else:
        return ''
    
#########################################################################

try:
            
    driver = webdriver.Firefox(firefox_binary=binary)
    driver.set_page_load_timeout(page_load_timeout)
    driver.get(url)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    source = None
    page = None
    
    i = 0
    while not page:
        print(i)
        i += 1
        page = driver.find_element_by_tag_name('body')
        time.sleep(1)
        
    for i in range(10):
        
        print(i)
        page.send_keys(Keys.PAGE_DOWN)  # scroll down
        time.sleep(scrolling_timeout)   # until comments number is generated
        
        source = driver.page_source
        views_num = get_value_html(reg_expr_views, source)
        comments_num = get_value_html(reg_expr_comments, source)
        
        print('################')
        print(views_num)
        print('-----------------')
        print(comments_num)
        print('-----------------')
        if ('text="[[data.countText' in comments_num) or not comments_num.strip(): 
            continue
        else:
            break

except:
    print('except')
    source = driver.page_source
    Log.write(Debug.exception_info(), print_it=True)
finally:
    print('finally')
    try:
        driver.quit()
    except:    
        Log.write(Debug.exception_info(), print_it=True)

pos = source.find(views_class)
html_views = source[pos:pos+150]
print(html_views)
print('..................................')
pos = source.find(comments_class)
html_comments = source[pos:pos+150]
print(html_comments)
























