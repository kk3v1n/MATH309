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

def calculation():
    forces_array, angle_array = getFile("forceAndAngle.csv")
    #print("this is forces_array:\n",forces_array)
    #print("\nthis is angle_array:\n",angle_array)

    a = int(input("Enter a bottom bound(a): "))
    #a = 20
    
    b = int(input("Enter a value for top bound(a): "))
    #b = 50
    
    n = int(input("Enter a even number: "))
    #n = 2 #you can change this to whatever
    
    h = (b - a) / n
    x = np.linspace(a, b, n)

    #print("\nthis is x:\n",x)

    #forces_array_count = len(forces_array)
    #angle_array_count = len(angle_array)
    
    #f = np.cos(x)
    f = forces_array * np.cos(angle_array)

    #print("\nthis is f:\n", f)

    I_simp = (h/3) * (f[0] + 2*sum(f[:n-2:2]) \
        + 4*sum(f[1:n-1:2]) + f[n-1])

    return(I_simp)
    #print(I_simp)

print(calculation())

# a = 20 and b = 50
#N = 2, 8.123154146025467
#N = 4, 25.11697540637516
#N = 3, 
#N = 23, 351.3709607391776
