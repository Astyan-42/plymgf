#!/usr/bin/env python
#encoding: utf-8
import os

for osdir in os.walk("code"):
    for dirn in osdir[1]:
        if dirn == "__pycache__":
            os.remove(os.path.join(os.getcwd(), osdir[0], dirn))

