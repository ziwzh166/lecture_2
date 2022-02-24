# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:21:13 2022

@author: zzw
"""


class Fishs:
    def __init__(self):
        '''constructor'''
        # name of the mammals
        self.member = ['sharks','piranha','swordfish']
    def printMembers(self):
        print('The fish classes')
        for member in self.member:
            print(member)