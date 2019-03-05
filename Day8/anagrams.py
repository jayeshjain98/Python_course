# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:17:42 2019

@author: Jayesh Jain
"""

import os
os.chdir ="C:/Users/Jayesh Jain/Downloads"

with open('anagram.txt', 'r') as fp:
    line = fp.readlines()

def make_anagram_dict(line):
    d = {}  # avoid using 'dict' as variable name

    for word in line:
        word = word.lower()  # call lower() only once
        key = ''.join(sorted(word))
        if key in d:  # no need to call keys()
            d[key].append(word)
        else:
            d[key] = [word]  # you can initialize list with the initial value

    return d  # just return the mapping to process it later

if __name__ == '__main__':
    d = make_anagram_dict(line)

    for words in d.values():
        if len(words) > 1:  # several anagrams in this group
            print('Anagrams: {}'.format(', '.join(words)))