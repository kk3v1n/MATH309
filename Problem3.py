# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 17:14:48 2021

@author: elyssa
"""

import numpy as np

def getFile(file_input):
    applied_forces = []
    angle_of_applications = []
    with open(file_input, "r") as data_file:
        data_file.readline() #ignore header
        for line in data_file:
            force, angle = line.split(',')
            applied_forces.append(float(force))
            angle_of_applications.append(float(angle))

    return (applied_forces, angle_of_applications)


getFile("forceAndAngle.csv")
#print(getFile("forceAndAngle.csv"))