# -*- coding: utf-8 -*-

import sys
import re
import time
import argparse

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys

from log import Log
from debug import Debug


parser=argparse.ArgumentParser()
parser.add_argument('--url', help='input "url" argument')
args=parser.parse_args()
url = args.url
if not url:
    print('url value is empty. aborting the program.')
    sys.exit(0)
    
binary = FirefoxBinary('/usr/bin/firefox')
#url = 'https://www.youtube.com/watch?v=p9DWfW2JYs8'
page_load_timeout = 120
scrolling_timeout = 2

views_class= 'view-count style-scope yt-view-count-renderer'
comments_class = 'count-text style-scope ytd-comments-header-renderer'

  
def get_value(class_, html):
    value = None
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
    
    while not page:
        page = driver.find_element_by_tag_name('body')
        time.sleep(1)
        
    for i in range(10):
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
        
        if not views_num:
            print('views number value is empty, maybe the url is wrong. aborting...')
            sys.exit(0)

except:
    source = driver.page_source
    Log.write(Debug.exception_info(), print_it=False)
finally:
    try:
        driver.quit()
    except:    
        Log.write(Debug.exception_info(), print_it=False)

if views_num:
    print('Number of views: {0}'.format(views_num))
else:
    print('No value for number of views.')

if comments_num:
    print('Number of comments: {0}'.format(comments_num))
else:
    print('No value for number of comments')
    
    
    
    























