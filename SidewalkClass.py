# -*- coding: utf-8 -*-
"""
Created on Thu Mar 3 2022
Script for Tyree's Sidewalk Project'

@author: Crystal Posey
"""

class Sidewalk():
    def __init__(self, cross_slope, sidewalk_width, roadway_slope, sidewalk_slope, vertical_c, ramp_comp, driveway_comp, stairs, ped_barrier):
        self.cross_slope = cross_slope
        self.sidewalk_width = sidewalk_width
        self.roadway_slope = roadway_slope
        self.sidewalk_slope = sidewalk_slope
        self.vertical_c = vertical_c
        self.ramp_comp = ramp_comp
        self.driveway_comp = driveway_comp
        self.stairs = stairs
        self.ped_barrier = ped_barrier
        self.Reclass()
        
    def is_red():
        return 'red'
    def is_yellow():
        return 'yellow'
    def is_green():
        return 'green'
    
    def Reclass(self):
        if self.cross_slope>3.5:
           self.correct=Sidewalk.is_red()
        elif self.sidewalk_width<=3:
            self.correct=Sidewalk.is_red()
        elif self.vertical_c == 'No': ## NEED MORE CLARIFICATION ON REQUIREMENTS
            self.correct=Sidewalk.is_red() ## NEED MORE CLARIFICATION ON REQUIREMENTS
        elif self.stairs == 'Yes':
            self.correct=Sidewalk.is_red()
        elif self.ped_barrier =='Yes':
            self.correct=Sidewalk.is_red()
        elif self.sidewalk_slope>5:
            if self.roadway_slope == (self.sidewalk_slope+1.5) or self.roadway_slope == (self.sidewalk_slope+1.5):
                self.correct=Sidewalk.is_yellow()
            else:
                self.correct=Sidewalk.is_red()   
        elif(self.cross_slope<3.5 and self.cross_slope>2.5):
            self.correct=Sidewalk.is_yellow()
        elif self.sidewalk_width>3 and self.sidewalk_width<=4:
            self.correct=Sidewalk.is_yellow()
        elif self.ramp_comp =='No': #'Yes' ?
            self.correct=Sidewalk.is_yellow()
        elif self.driveway_comp =='No':
            self.correct=Sidewalk.is_yellow()
        else:
            self.correct=Sidewalk.is_green()
    def get_correct(self):
        return self.correct
            
slope = Sidewalk(2.4,5,8, 4, 'Yes', 'Yes', 'Yes', 'No', 'Yes')
Sidewalk.get_correct(slope)
            
