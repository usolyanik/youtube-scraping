# -*- coding: utf-8 -*-

import os
import requests
import re
import time
import codecs

path = os.getcwd()
os.chdir(path)

from text_processor import TextProcessor as tp
from debug import Debug
from log import Log

USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
headers = {'User-Agent': USER_AGENT}
timeout_connection = 30
timeout_read = 30
target_path = 'target/'

"""
<span class="view-count style-scope 
yt-view-count-renderer">162&nbsp;798 просмотров</span>

<yt-formatted-string class="count-text style-scope 
ytd-comments-header-renderer">148&nbsp;комментариев</yt-formatted-string>

"""

url = 'https://www.youtube.com/watch?v=p9DWfW2JYs8'

########################################################################

def get_html_from_web_page(url,
                           timeout_connection=5,
                           timeout_read = 5):
    
    try:        
        r = requests.get(url,
                         timeout=(timeout_connection, timeout_read)) #,
#                         headers=headers)
        				 
        html = str(r.content)
        
        return html
    
    except:
        Log.write(Debug.exception_info(), print_it=True)
        return ''
    
####################################################



html = get_html_from_web_page(url)

print('len(html):', len(html))

f = open('time2.txt', 'w')
f.write(html)
f.close()









