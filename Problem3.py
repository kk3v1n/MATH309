
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


    def simpsons_rule(self, n): 
        a = 20.0
        b = 50.0 
        h = b - a / n
        x = np.linspace(a, b , n + 1)
        f = lambda x : self.applied_forces * np.cos(self.angle_of_applications)
        y = f(x)
        simpson = h / 3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
        return simpson

    
if __name__ == "__main__":
    problem = problem_3()
    #problem.simpsons_rule(10)
    print(problem.applied_forces)
    print(problem.simpsons_rule(10))

