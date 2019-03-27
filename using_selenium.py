# -*- coding: utf-8 -*-

import re
from pprint import pprint as pp

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys

binary = FirefoxBinary('/usr/bin/firefox')
url = 'https://www.youtube.com/watch?v=p9DWfW2JYs8'
page_load_timeout = 60

try:
            
    driver = webdriver.Firefox(firefox_binary=binary)
    driver.set_page_load_timeout(page_load_timeout)
    driver.get(url)
#    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
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
    
    WebDriverWait(driver, page_load_timeout)

    
    element = driver.find_element_by_class_name(comments_class)
    element.location_once_scrolled_into_view
    element.send_keys(Keys.END)
    
#    driver.execute_script('data.countText()')
    
    source = driver.page_source
    
#    for comment_num in driver.find_elements_by_class_name(comments_class):
#        print u'Number of comments: ' + comment_num.text
except:
    source = driver.page_source
finally:
    try:
        pass
        driver.quit()
    except:
        pass

#rex = comments_class + r'[~>]*?>([~<]*?)<'
#arr = re.findall(rex, source)
#pp(arr)
        
p = source.find(comments_class)
print(source[p:p+150])




























