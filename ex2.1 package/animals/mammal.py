# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 13:45:41 2022

@author: zzw
"""

class Mammals:
    def __init__(self):
        '''constructor'''
        # name of the mammals
        self.member = ['tiger','elephant','wild cat']
    def printMembers(self):
        print('The mammals classes')
        for member in self.member:
            print(member)
    