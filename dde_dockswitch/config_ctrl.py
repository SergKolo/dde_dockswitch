# -*- coding: utf-8 -*-
import json,os
from collections import OrderedDict as od

def read_config_file(conf_file):
    with open(conf_file) as fd:
         return od(json.load(fd))

def write_config_file(conf_file,conf):
    with open(conf_file,"w") as fd:
        json.dump(conf,fd,indent=4,sort_keys=True)

def remove_config_file(conf_file):
    os.unlink(conf_file)
