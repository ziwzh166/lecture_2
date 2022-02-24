# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:32:39 2022

@author: zzw
"""

class dangerous:
    def __init__(self):
        '''constructor for the birds'''
        # class for the dangerous fishes
        self.name = 'dangerous'
        self.Fish = self.Fish()
    class Fish:
        def __init__(self):
            '''constructor'''
            # name of the mammals
            self.member = ['sharks','piranha','swordfish']
        def printMembers(self):
            print('The fish classes')
            for member in self.member:
                print(member)
    