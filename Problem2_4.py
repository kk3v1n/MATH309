

#Write a program to simulate the spread of a disease.


#import numpy as np
#from matplotlib import pyplot as plt
import random

class problem_two:

    def problem_two_four():

        def population(N):

            total_population_count = N #we have N people

            rows,columns = (total_population_count,4) #each person has 4 parameters, resistance, recovery, activity, and transmission
            total_population_list = [[random.uniform(0,1)for i in range(columns)] for j in range(rows)] # we are creating an array element for each person inside one big array


            for count in range(0, total_population_count):
                total_population_list[count].insert(0,count) #adding person's id to in front of each array
                total_population_list[count].insert(5,0) #adding person's #of exposure at end of array

            #print(total_population_list) #print the array to seeing data for each person including thier id in index 0


            #index 0 - thier id starting from 0 to N-1
            #index 1 - chance of being infected
            #index 2 - chance of recovering
            #index 3 - % exposing out of total population without exposing themselves
            #index 4 - % infecting the total population that can be infected that was exposed
            #index 5 - the count of times they were exposed to certain individual 


            only_infected_list = []
            for i in range(0, total_population_count): #trying to figure out who is infected

                resistance = total_population_list[i][1]   #getting their probability of resistence to disease

                if (resistance < 0.6):  #they WILL be infected if their resistance is less than 60% 
                    only_infected_list.append(total_population_list[i]) #add it to new array to randomly choose who to start from that WILL be infected and transmit for sure


            starting_with_person = random.choice(only_infected_list) # we will start with this person for this certain iteration
            starting_with_person[5] +=1 #since we start with this person, they are now exposed (index 5 = # of exposure)


            total_population_list_no_starter = total_population_list.copy() #copies the list to still have total array for every N in the population

            total_population_list_no_starter.pop(starting_with_person[0]) #remove the starting person since we are starting with them
            total_population_count_no_starter = len(total_population_list_no_starter)# get the total population count without the starter


            recovery_of_starting_person = starting_with_person[2] #gives us the starter recovery rate

            if(recovery_of_starting_person<=0.40): #they did NOT recover and will have a chance to transmit to another person)

                activity_of_starting_person = starting_with_person[3]
                people_exposed = activity_of_starting_person*total_population_count_no_starter #calculating people exposed
                number_of_people_exposed_rounded = round(people_exposed) #gives us # of people exposed
                #print("count of people exposed by this person: ",number_of_people_exposed_rounded)
                
                total_exposed = number_of_people_exposed_rounded

                for count in range(number_of_people_exposed_rounded): #increasing exposure count in index5
                    exposed_person = random.choice(total_population_list_no_starter)
                    exposed_person[5] += 1


                who_can_be_infected = 0 # who actually can be infected due to resistance being low and exposure being high

                for counter in range(0, total_population_count_no_starter):
                    if(total_population_list_no_starter[counter][5]>0 and total_population_list_no_starter[counter][1] < 0.6):
                        who_can_be_infected +=1

                #print("max that can be infected due to resistance and exposure count (being a factor): ", who_can_be_infected)



                #number_of_people_exposed_rounded  = number of people exposed

                infection_rate_to_others_starting_person = starting_with_person[4]
                number_of_people_they_infected = infection_rate_to_others_starting_person*number_of_people_exposed_rounded #calculating number of people they infected
                number_of_people_they_infected_rounded = round(number_of_people_they_infected) #rounding to check #of exposures



                if(number_of_people_they_infected_rounded <= who_can_be_infected): #checking for those who are exposed and have low resistance 
                    #print("count of people they did infect:", number_of_people_they_infected_rounded)
                    total_infected = number_of_people_they_infected_rounded
                else:
                    total_infected = who_can_be_infected
                    #print("count of people they did infect 100%", who_can_be_infected)

            else: #the person did recover
                total_exposed = 0
                total_infected = 0

            return [total_infected,total_exposed]


        def simulation(N, nsteps):

            rows,columns = (nsteps,0)
            total_simulation_list = [[(0)for i in range(columns)] for j in range(rows)] # we are creating an array element

            #index 0 - run id starting from 1 to nsteps
            #index 1 - how many infected in total from prev runs
            #index 2 - exposure count for the current run

            counter_of_infected = 0

            for i in range(0, nsteps):
                total_simulation_list[i].insert(0,i+1) #adding run's id (stage) in front 
                total_simulation_list[i].extend(population(N)) #adding number of people to element 1  and total infected to element 2 within each array

            total_simulation_count = len(total_simulation_list)# gets the count of the list
            
            for k in range(0, total_simulation_count):
                counter_of_infected += total_simulation_list[k][1] #infection in each run increases if there is exposure
                total_simulation_list[k][1] = counter_of_infected #swapping the numbers


            #print("lists",total_simulation_list)


        return simulation(1000, 15) #1000 people and 15 simulation runs


problem_two.problem_two_four()