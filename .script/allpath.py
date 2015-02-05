#!/usr/bin/env python
#encoding: utf-8
import os

lpath = []
slpath = ""

for osdir in os.walk("."):
    for fich in osdir[2]:
        if fich.split('.')[-1] == "py":
            lpath.append(osdir[0])
            break

for path in lpath:
    slpath = slpath+os.path.join(path,"*.py")+" "
    
print slpath
