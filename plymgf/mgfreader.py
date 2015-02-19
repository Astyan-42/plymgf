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
    
    def get_cle(self):
        """return the enzyme use to make the disgestion"""
        return self._data["meta"]["cle"]
    
    def get_accession(self):
        """return the database entries to be search"""
        return self._data["meta"]["accession"]
    
    def get_itol(self):
        """return the error tolerance (depend of itolu)"""
        return self._data["meta"]["itol"]
    
    def get_itolu(self):
        """return the error tolerance unit"""
        return self._data["meta"]["itolu"]
    
    def get_mass(self):
        """return the type of the mass Monoisotopic/Average"""
        return self._data["meta"]["mass"]
        
    def get_precursor(self):
        """return the precursor mass"""
        return self._data["meta"]["precursor"]
        
    def get_seg(self):
        """return the protein mass in KDa"""
        return self._data["meta"]["seg"]
    
    def get_taxonomy(self):
        """return the taxonomy"""
        return self._data["meta"]["taxonomy"]
    
    def get_usermail(self):
        """return the mail of the user"""
        return self._data["meta"]["usermail"]
    
    def get_charge(self):
        """return the meta charges"""
        return self._data["meta"]["charges"]
    
    def next_ion(self):
        """go to the next ion"""
        if len(self._data["ions"]) > self._ions + 1:
            self._ions = self._ions + 1
    
    def get_ion_charge(self):
        """return the charge of the ion"""
        return self._data["ions"][self._ions]["charges"]
    
    def get_ion_pepmass(self):
        """return the mass and the intensity of the peptide"""
        return self._data["ions"][self._ions]["pepmass"]
    
    def get_ion_rtinseconds(self):
        """return the time when the ion was analyse"""
        return self._data["ions"][self._ions]["rtinseconds"]
    
    def get_ion_seq(self):
        """return the sequence of the ion"""
        return self._data["ions"][self._ions]["seq"]

    def get_ion_title(self):
        """return the title of the ion"""
        return self._data["ions"][self._ions]["title"]
    
    def get_ion_tol(self):
        """return the error tolerance (depend of tolu) of the ion"""
        return self._data["ions"][self._ions]["tol"]
    
    def get_ion_tolu(self):
        """return the error tolerance unit of the ion"""
        return self._data["ions"][self._ions]["tolu"]
    
    def get_ion_peaks(self):
        """return the list of peak of the ion"""
        return self._data["ions"][self._ions]["peaklist"]

if __name__ == "__main__":
    TEST = MGFReader(sys.argv[1])
    TEST.next_ion()
    TEST.next_ion()
    print TEST.get_ion_peaks()
    
