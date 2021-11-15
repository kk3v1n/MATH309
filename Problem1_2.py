import math

class problemone:
    def overallProblem(length_of_rod, young_modulus, mass_per_unit, stepsize, tol, x0):

        def ctrdiff(f,x,h): #centered differemce formula
            return (f(x+h) - f(x-h)) / (2.0*h)

        def my_newton(f, x, h, tol): #newton's method
            iterations = 0

            while abs(f(x)) > tol and iterations < 5000:
                x = x -f(x) / ctrdiff(f,x,h)
                iterations += 1

            return x

        f = lambda x: ((x * (length_of_rod / math.sqrt(young_modulus/mass_per_unit))) * math.tan(x * (length_of_rod/ math.sqrt(young_modulus/mass_per_unit)))) - 0.40
        
        smallestPostiveRoot = my_newton(f, x0, stepsize, tol)
        return smallestPostiveRoot
        

print(problemone.overallProblem(115, 3*(10**7), 7.2*(10**-4), 0.01, 1e-6, 100))