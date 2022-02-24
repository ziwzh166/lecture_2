# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 13:55:59 2022

@author: zzw
"""

class Birds:
    def __init__(self):
        '''constructor for the birds'''
        # define birds types
        self.members = ['duck','sparrow','robin']
        
    def printMembers(self):
        print('The birds classes')
        for member in self.members:
            print(member)
            