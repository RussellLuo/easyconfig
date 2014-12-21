#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from easyconfig.dictproxy import DictProxy


class DictProxyTest(unittest.TestCase):

    def test_basic(self):
        p = DictProxy({'username': 'russell', 'password': '123456'})
        self.assertEqual(p.username, 'russell')
        self.assertEqual(p.password, '123456')

        p.username = 'tracey'
        p.password = '12**56'
        self.assertEqual(p.username, 'tracey')
        self.assertEqual(p.password, '12**56')


if __name__ == '__main__':
    unittest.main()
