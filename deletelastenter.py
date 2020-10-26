# -*- coding: utf-8 -*-
"""
Created  Oct 26 19:24:25 2020

@author: salorsmile
function: delete \n at last
"""

import os


path_dir = r'../.../////'                   # root path
dirs = ['test', 'train', 'val']             # file dirs

for dir0 in dirs:
    file_path = os.path.join(path_dir, dir0)
    files_list = os.listdir(file_path)

    for file in files_list:
        f = open(os.path.join(file_path, file), 'r')
        fstr = f.read()
        newstr = fstr[len(fstr) - 1:]
        res = fstr[0:len(fstr) - 1] + newstr.replace("\n", "")  # nothing can be ""
        f = open(os.path.join(file_path, file), 'w')
        f.write(res)
        f.close()

print('done')
