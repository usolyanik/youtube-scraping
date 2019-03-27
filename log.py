# -*- coding: utf-8 -*-

import os
import datetime
from pprint import pprint

path = os.path.dirname(os.path.realpath(__file__))
ROOTPATH = '/'.join(path.split('/')[:-1])

class Log:

    @staticmethod
    def write(message,
              data_path='./',
              print_it=False):

        time = datetime.datetime.now()

        msg = '\n' + str(time) + ': ' + str(message) + '\t!&&&\n'

        f = open(data_path + 'log_exception.txt', 'a')
        f.write(msg)
        f.close()

        if print_it:
            pprint(msg)
