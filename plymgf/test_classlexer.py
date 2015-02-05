#!/usr/bin/env python
# encoding: utf-8
# pylint: disable=too-many-public-methods
"""test_classlexer.py is units test for classlexer
@author: Vezin Aurelien
@license: CECILL-B"""

import unittest
import os

from classlexer import read_mgf

class TestReadMGF(unittest.TestCase):
    """Class to test read_mgf function"""
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_10_read_mgf(self):
        res = read_mgf(os.path.join(".", "plymgf", "files", "test.mgf"))
        
