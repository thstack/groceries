#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: SimonLuo <simonluo@thstack.com>
import sys,os,re
reload(sys)
sys.setdefaultencoding('utf8')
import unittest

from groceries.tests.test_settings import SettingsCase
from groceries.tests.test_client import ClientCase


def suite():
    suite = unittest.TestSuite()

    suite.addTest(      # 创建默认用户
        SettingsCase('test_settings'))

    suite.addTest(      # 创建默认用户
        ClientCase('test_client'))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
