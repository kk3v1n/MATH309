# MATH 309: Group Project

Group 3: Kevin Karmacharya, Justin Wong, Briana Sze, Elyssa M. Tapawan 

Problems: 1.2, 2.4, 3

## Section 1, Question 2
The following figure shows a mass M attached to a slender steel rod of mass m:

![image](https://user-images.githubusercontent.com/70128989/142186557-7ab79256-f647-4928-a08f-b2b93cb98eed.png)

The frequency equation for the free undamped longitudinal vibration is

![image](https://user-images.githubusercontent.com/70128989/142186632-161ae960-b3c1-42ff-aec9-0b5a0e89caac.png)
![image](https://user-images.githubusercontent.com/70128989/142186662-11ca99c2-c260-4977-b0aa-dd85f07f6795.png)

Use Newton’s method to find the smallest positive root of the frequency equation if m/M = 0.40.

## Section 2, Question 4
The spread of a contagious disease and the propagation of a rumor have a great deal in common. Write a program to simulate the spread of a disease or a rumor. You might proceed as follows: establish a population of N individuals, and assign to each individual four parameters (perhaps different numbers to various individuals):

(a) a “resistance” parameter: the probability that the individual will be infected by the disease (rumor) upon transmission from a carrier

(b) a “recovery” (or “forgetting”) parameter: the probability that the infected individual will recover from the disease (forget the rumor) before transmitting it to others in the population

(c) an “activity” parameter: the probability that the individual will contact another person

(d) a “transmission” parameter: the probability that the individual will in fact transmit the disease (rumor) to another person they contact.

A person who comes in contact with an infected person either becomes infected or does not; a random number can be compared with the individual’s resistance parameter to determine the result.

Once a person is infected, that is, becomes a carrier, another random number can be compared with their recovery (forgetting) parameter to determine whether or not they will recover from the disease (forget the rumor) before contacting other persons.

The activity parameter of a person who does not recover from the disease (forget the rumor) before contacting other persons determines how many persons they will contact. The transmission parameter determines the actual number of persons to whom the disease (rumor) will be transmitted. The specific individuals can then be selected at random from the population and the disease (rumor) transmitted to them.

Select one individual to initiate the process. Keep track of the number of persons infected in each stage and the “degrees of exposure (credibility),” that is, the number of persons exposed once, twice, and so on. Your program should output two plots:

Plot 1. Number of infected persons vs the stage/step of the infection (simulation)

Plot 2. Number of infected vs number of exposed 

Your program should take in the following inputs:

• size of the population N

• the number of simulation steps (nsteps)

The resistance, recovery, activity and transmission parameters for each person are probabilities and as such should be assigned to a random number between 0 and 1.

## Section 3
The problem in this section is the same for all groups.

Simpson’s rule is another method of integration that generally produces better approximations than the midpoint or trapezoidal methods. Simpson’s rule approximates a function over each subinterval as a quadratic polynomial. The interval [a, b] is divided into an even number n of subintervals, each of length h = b − a / n and the integral is approximated as

![image](https://user-images.githubusercontent.com/70128989/142188529-225c4845-ca4f-41a8-82cd-e72957ddfe40.png)

The familiar equation work = force × distance can be used to compute the work done by a force whose line of action is in the direction of displacement. However, if the force is applied at some angle to the direction of motion, and the angle and the applied force vary as a function of the displacement s, then the work done is given by

![image](https://user-images.githubusercontent.com/70128989/142188552-2bdf0ff9-e7da-4421-ba83-78d64d21e0b7.png)

where F(s) and θ(s) are the varying applied force and angle of application respectively, at displacement s. Write a program that asks the user to enter values for. a and b, that reads a value for n and the values of F(s) and θ(s) at n + 1 equally spaced points along the path of motion from a data file, and that then uses Simpson’s rule to approximate this integral. The program should then compute and display the work done. Run your program using a = 20.0m, b = 50.0m, and the following pairs of values of F(s) and θ(s) at points a, a + h, a + 2h,. . ., b (all in newtons and radians):

![image](https://user-images.githubusercontent.com/70128989/142188650-0e5dfc78-28f1-4f27-bd8d-b162a2afa6b5.png)
