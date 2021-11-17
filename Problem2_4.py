import random
import numpy as np
from matplotlib import pyplot as plt

class problem_two:
    def problem_two_four(total_population_count, nsteps):

        total_exposed_in_currentSimulation = 0 #the total for the current simulation
        total_exposed = 0 #the total over all the simulations
        total_infected_in_currentSimulation = 0 #the total for the current simulation
        total_infected = 0 #the total over all the simulations

        simulation_runs = []
        for i in range(1,nsteps+1): #making a list from 1 - nsteps so we can use it to plot
            simulation_runs.append(i)

        #list created to keep track for total and per each simulation
        total_exposed_in_currentSimulation_list =[]
        total_exposed_list = []
        total_infected_in_currentSimulation_list = []
        total_infected_list = []

        rows, columns = (total_population_count,4) #4 parameters for each person
        total_population_list = [[random.uniform(0,1) for i in range(columns)] for j in range(rows)]

        for count in range(0, total_population_count):
            total_population_list[count].insert(0,count) #add parameter for person's id
            total_population_list[count].insert(5,0) #adding parameter for how many times person is exposed
        
        #index 0 - their id starting from 0 to N-1
        #index 1 - chance of being infected
        #index 2 - chance of recovering
        #index 3 - % exposing out of total population without exposing themselves
        #index 4 - % infecting the total population that can be infected that was exposed
        #index 5 - the count of times they were exposed to certain individual 

        nsteps_process = 0

        only_infected_list = [] #making new list to keep track of infected people 
        for i in range(0, total_population_count): #trying to figure out who is infected
            resistance = total_population_list[i][1]   #getting their probability of resistence to disease
            if (resistance < 0.6):  #they WILL be infected if their resistance is less than 60% 
                only_infected_list.append(total_population_list[i])
    
        while(nsteps_process<nsteps): #running the simulation nsteps times
            
            only_infected_count = len(only_infected_list) #how many people can be infected

            if(only_infected_count == 0): #if everyone's resistance is high enough there will be no new exposures and no infections
                total_exposed += 0
                total_infected += 0
                total_infected_in_currentSimulation = 0
                total_exposed_in_currentSimulation = 0

                total_exposed_in_currentSimulation_list.append(total_exposed_in_currentSimulation)
                total_exposed_list.append(total_exposed)
                total_infected_in_currentSimulation_list.append(total_infected_in_currentSimulation)
                total_infected_list.append(total_infected)
                nsteps_process+=1
                continue #skips the rest of loop as we reached 0 in list

            starter_person = random.choice(only_infected_list) #pick random person who is infected from infected list

            #print(nsteps_process ,only_infected_list)

            if(nsteps_process == 0):
                starter_person[5] +=1 #since we start with this person, they are now exposed (index 5 = # of exposure)
                total_exposed +=1 #initial person is exposed
                total_infected +=1 #initial person is infected
                total_infected_in_currentSimulation +=1 #initial person is infected
                total_exposed_in_currentSimulation +=1 #initial person is exposed
            
            total_population_list_no_starter = total_population_list.copy() #copies the list to still have total array for every N in the population
            total_population_list_no_starter.pop(starter_person[0]) #remove the starting person since we are starting with them
            total_population_count_no_starter = len(total_population_list_no_starter) # get the total population count without the starter

            activity_of_starting_person = starter_person[3]
            people_exposed_count = activity_of_starting_person*total_population_count_no_starter #calculating people exposed
            people_exposed_count_rounded = round(people_exposed_count) #gives us # of people exposed

            if(nsteps_process == 0): #if we are in the first iteration then we will add to 1 in the first run
                total_exposed_in_currentSimulation += people_exposed_count_rounded
                total_exposed += people_exposed_count_rounded
            else:
                total_exposed_in_currentSimulation = people_exposed_count_rounded
                total_exposed += people_exposed_count_rounded


            for count in range(people_exposed_count_rounded): #increasing exposure count for random people who come in contact
                exposed_person = random.choice(total_population_list_no_starter)
                exposed_person[5] += 1 #increase count of thier exposure
                exposed_person[1] += 0.002 #their resistance increases if they have been exposed

            infection_rate_to_others_starter_person = starter_person[4]
            people_they_infected_count = infection_rate_to_others_starter_person*people_exposed_count_rounded #calculating number of people they infected
            people_they_infected_count_rounded = round(people_they_infected_count) #rounding to check #of exposures

            infected_certain_list = [] 
            who_can_be_infected = 0 # who actually can be infected due to resistance being low and exposure being high
            
            for counter in range(0, total_population_count_no_starter):
                if(total_population_list_no_starter[counter][5]>0 and total_population_list_no_starter[counter][1] < 0.6):
                    infected_certain_list.append(total_population_list_no_starter[counter])
                    who_can_be_infected +=1

            if(people_they_infected_count_rounded <= who_can_be_infected): #checking for those who are exposed and have low resistance
                if(nsteps_process == 0):
                    total_infected += people_they_infected_count_rounded
                    total_infected_in_currentSimulation += people_they_infected_count_rounded
                else:
                    total_infected += people_they_infected_count_rounded
                    total_infected_in_currentSimulation = people_they_infected_count_rounded
            else:
                if(nsteps_process == 0):
                    total_infected += who_can_be_infected
                    total_infected_in_currentSimulation += who_can_be_infected
                else:
                    total_infected_in_currentSimulation = who_can_be_infected
                    total_infected += who_can_be_infected

            total_exposed_in_currentSimulation_list.append(total_exposed_in_currentSimulation)
            total_exposed_list.append(total_exposed)
            total_infected_in_currentSimulation_list.append(total_infected_in_currentSimulation)
            total_infected_list.append(total_infected)

            only_infected_list =[] #we know need to get someone who is infected and cannot recover in order to continue simulation
            for a in range(0, who_can_be_infected): #we need to add to the count of those who are exposing others since they are infected
                recovery_of_person_infected = infected_certain_list[a][2] #check if they recover

                if (recovery_of_person_infected<=0.40): #these did not recover, so they will exposed others
                    only_infected_list.append(infected_certain_list[a])
                    infected_certain_list[a][1]+= 0.004

                else: #they did recover, so increase thier resistance a bit
                    infected_certain_list[a][1]+= 0.006

            nsteps_process+=1 #keep iterating the simulation
            
        #print("simulation_runs",simulation_runs)
        #print("total_exposed_in_currentSimulation_list",total_exposed_in_currentSimulation_list)
        #print("total_exposed_list",total_exposed_list)
        #print("total_infected_in_currentSimulation_list",total_infected_in_currentSimulation_list)
        #print("total_infected_list",total_infected_list)
            
        a = np.asarray(simulation_runs) #numpy array for simulation_runs
        b = np.asarray(total_exposed_in_currentSimulation_list) #numpy array for total_exposed_in_currentSimulation_list     
        c = np.asarray(total_exposed_list) #numpy array for total_exposed_list
        d = np.asarray(total_infected_in_currentSimulation_list) #numpy array for total_infected_in_currentSimulation_list
        e = np.asarray(total_infected_list) #numpy array for total_infected_list

        #plot1
        plot1 = plt.figure(1)
        plt.title("Number of Infected Persons vs Stage of Infection")
        plt.xlabel('Stage of Infection')
        plt.ylabel('Number of Infected Persons')
        plt.plot(a, d, 'b')
         
        #plot2
        plot2 = plt.figure(2)
        plt.title("Number of Infected Persons vs Number of Exposed")
        plt.xlabel('Number of Infected Persons Total')
        plt.ylabel('Number of Exposed Total')
        plt.plot(e, c, 'g')
        
        plt.show()
        #fix
        
problem_two.problem_two_four(1000,100) #1000 people and 100 nsteps

