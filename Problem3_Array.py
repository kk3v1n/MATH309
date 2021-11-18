# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 02:16:21 2021

@author: Justin Wong
"""

import numpy as np

class problem_3():
    
    def __init__(self):
        parsefile = self.getFile("forceAndAngle.csv")
        
        self.applied_forces = parsefile[0]
        self.angle_of_applications = parsefile[1]

    
    def getFile(self, file_input):
        
        applied_forces = []
        angle_of_applications = []
        with open(file_input, "r") as data_file:
            data_file.readline() #ignore header
            for line in data_file:
                force, angle = line.split(',')
                applied_forces.append(float(force))
                angle_of_applications.append(float(angle))

        return (applied_forces, angle_of_applications)
    
    def simpsons_rule(self, f, a, b, n):
        h = (b - a) / n 
        k = 0.0
        x = a + h
        for i in range (1, n//2 + 1):
            k += 4*f(x)
            x += 2*h
            
        x = a + 2*h
        for i in range(1, n//2):
            k += 2*f(x)
            x += 2*h
            
        return (h/3) *( f(a)+ f(b) + k)

if __name__ == "__main__":
    problem = problem_3()
    #problem.simpsons_rule(10)
    #print(len(problem.applied_forces))
    #print(len(problem.angle_of_applications))
    print(problem.simpsons_rule(lambda x: problem.applied_forces * np.cos(problem.angle_of_applications), 20, 50, 22 ))
    
    #N = 23 559.20575724
