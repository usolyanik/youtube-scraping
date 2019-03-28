# -*- coding: utf-8 -*-

import re
import time

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

  
def get_value(class_, html):
    if not html:
        return ''
    lst = re.findall(class_ + r'([^<]*?)<', html)
    if lst:
        value_html = lst[0]
    value = re.sub(r'[^\d]', '', value_html) # remove not-digits
    if value:
        return value
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
        i += 1
        page = driver.find_element_by_tag_name('body')
        time.sleep(1)
        
    for i in range(10):
        
        print(i)
        page.send_keys(Keys.PAGE_DOWN)  # scroll down
        time.sleep(scrolling_timeout)   # until comments number is generated
        
        source = driver.page_source
        
        views_num = get_value(views_class, source)
        comments_num = get_value(comments_class, source)

        if not views_num:
            continue

        if not comments_num: 
            continue
        else:
            break

except:
    source = driver.page_source
    Log.write(Debug.exception_info(), print_it=False)
finally:
    try:
        driver.quit()
    except:    
        Log.write(Debug.exception_info(), print_it=True)

if views_num:
    print('Number of views: {0}'.format(int(views_num)))
else:
    print('No value for number of views.')

if comments_num:
    print('Number of comments: {0}'.format(int(comments_num)))
else:
    print('No value for number of comments')
    
    
    
    























