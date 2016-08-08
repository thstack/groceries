#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: SimonLuo <simonluo@thstack.com>
from groceries.tests import *


class ClientCase(unittest.TestCase):
    def test_client(self):
        print 'g_client.get_configs_by_gkey()'
        s, m, configs2 = g_client.get_configs_by_gkey()
        self.assertTrue(s == 0)

        print 'g_client.get_templateconfigs()'
        s, m, configs = g_client.get_templateconfigs()
        self.assertTrue(s == 0)

        for t, v in settings.TOPIC_INCLUDES.items():
            print 'g_client.get_templateconfigs(topic=%s)' % t
            s, m, r = g_client.get_templateconfigs(topic=t)
            self.assertTrue(s == 0)

        print '\nGet Template files ----------'
        for g_key, v in configs2.items():
            print 'vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv'
            print 'g_key=<%s>' % g_key

            s, m, r = g_client.get_templatefiles([g_key])
            print "g_client.get_templatefiles(['%s']):" % g_key 
            self.assertTrue(s==0)

            if v['g_type'] == 'file':
                print "g_client.get_templatefile_content(g_key='%s'):" % g_key
                s, m, r = g_client.get_templatefile_content(g_key)
                self.assertTrue(s==0)
            elif v['g_type'] == 'dir':
                for filename, c in v['files'].items():
                    print "g_client.get_templatefile_content(g_key='%s', filename='%s'):" % (g_key, filename)
                    s, m, r = g_client.get_templatefile_content(g_key, filename)
                    self.assertTrue(s==0)
            print '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ \n'


if __name__ == "__main__":
    unittest.main()
