#!/usr/bin/env python
#encoding: utf-8
import os

for osdir in os.walk("code"):
    for fich in osdir[2]:
        if fich.split('.')[-1] == "pyc":
            os.remove(os.path.join(os.getcwd(), osdir[0], fich))

