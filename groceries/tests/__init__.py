import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import unittest

from groceries import settings
from groceries import groceriesclient as g_client


class TestCase(unittest.TestCase):
    def setUp(self):
        print '[TestCase] ', self.__doc__, '......'
        print self.__class__

    def tearDown(self):
        session.remove()
        print '[TestCase] ', self.__doc__, '......', '\tEND\n'
