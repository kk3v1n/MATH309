import math

class problemone:
    def overallProblem(length_of_rod, young_modulus, mass_per_unit, stepsize, tol, x0):

        def ctrdiff(f,x,h): #centered difference formula
            return (f(x+h) - f(x-h)) / (2.0*h) #f(x+h)-f(x-h)/2*h

        def my_newton(f, x, h, tol): #newton's method
            iterations = 0

            while abs(f(x)) > tol and iterations < 5000:
                x = x - f(x) / ctrdiff(f,x,h) #derivative can be computed with the centered difference
                iterations += 1

            return x

        f = lambda x: ((x * (length_of_rod / math.sqrt(young_modulus/mass_per_unit))) * math.tan(x * (length_of_rod/ math.sqrt(young_modulus/mass_per_unit)))) - 0.40
        #f(x) = x(115)/sqrt(3*10^7/7.2*10^-4)*tan(x(115)/sqrt(3*10^7/7.2*10^-4))-0.40 
        smallestPostiveRoot = my_newton(f, x0, stepsize, tol)
        return smallestPostiveRoot
        
print(problemone.overallProblem(115, 3*(10**7), 7.2*(10**-4), 0.01, 1e-6, 1))
#length in rod: 115 in
#young's modulus: 3 * 10^7 psi
#mass per unit volume: 7.2 * 10^-4 lb 8 sec^2/in^4
#in this print statment, we test out h=0.01 and x0=1
