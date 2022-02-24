# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:25:27 2022

@author: zzw
"""

class harmless:
    def __init__(self):
        '''constructor for the birds'''
        # class for the harmless birds
        self.name = 'harmless'
        self.Birds = self.Birds()
    class Birds:
        def __init__(self):
            '''constructor for the birds'''
            # define birds types
            self.members = ['duck','sparrow','robin']
            
        def printMembers(self):
            print('The birds classes')
            for member in self.members:
                print(member)