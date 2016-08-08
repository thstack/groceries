#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: SimonLuo <simonluo@thstack.com>
from groceries.tests import *


class SettingsCase(unittest.TestCase):
    def test_settings(self):
        for k1, v1 in settings.TEMPLATES.items():
            for k2, v2 in v1.items():
                print "key=(%s %s)\tg_key=<%s>\tg_type=<%s>\tg_dirname=<'%s'>"% (k1, k2, v2['g_key'], v2['g_type'], v2['g_dirname'])
                print "files = ", v2['files']
                self.assertTrue(v2['g_key'])
                self.assertTrue(v2['alias'])
                self.assertTrue(v2['g_type'] in ['file', 'dir'])
                self.assertTrue(v2['g_dirname'])
                self.assertTrue('files' in v2)
                if v2['g_type'] == 'file':
                    self.assertTrue(v2['files']['filename'] and v2['files']['is_text'] in [True, False])
                if v2['g_type'] == 'dir':
                    for filename, c in  v2['files'].items():
                        self.assertTrue('is_text' in c and c['is_text'] in [True, False])

                print '------------------------------------------------------ \n'


if __name__ == "__main__":
    unittest.main()
