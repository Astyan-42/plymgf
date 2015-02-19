#!/usr/bin/env python
# encoding: utf-8
"""mgfreader.py is a reader for mgf files 
@author: Vezin Aurelien
@license: CeCILL-B"""


import sys
from classlexer import read_mgf


class MGFReader:
    """ This class is use to read an MGF File """
    
    def __init__(self, mgf_path):
        """ init of the class """
        self._data = read_mgf(mgf_path)
        self._ions = 0
    
    def get_raw_data(self):
        """return the pure data """
        return self._data
        
    
        
    

if __name__ == "__main__":
    TEST = MGFReader(sys.argv[1])
    print TEST.get_raw_data()
