import random

class problem_two:

    def population(N):


        total_possibly_infected = N #we have N people

        exposed_to_others = 0 #how many people the person exposes if they are infected
        exposed_by_others = 0  #how many times the person is exposed

        infected_people_count = 0 #how many people are infected


        rows,columns = (total_possibly_infected,4) #each person has 4 parameters, resistance, recovery, activity, and transmission
        population_chances = [[random.uniform(0,1)for i in range(columns)] for j in range(rows)] # we are creating an array element for each person inside one big array


        for count in range(0, total_possibly_infected):
            population_chances[count].insert(0,count) #adding person's id to in front of each array

        #print(population_chances) #print the array to seeing data for each person including thier id in index 0


        infected_people_for_certain_if_close_contact = [] #creating a list of people who we know will be infected due to their "resistance" %

        for i in range(0, total_possibly_infected): #trying to figure out who is infected

            resistance = population_chances[i][1]   #getting their probability of resistence to disease

            if (resistance<0.6):  #they WILL be infected if their resistance is less than 60% and contacted with person who starts infection
                infected_people_for_certain_if_close_contact.append(population_chances[i]) #add it to new array to randomly choose who to start from that WILL be infected for sure


        print("All these people will have a chance of being infected if in contact: ",infected_people_for_certain_if_close_contact)

        size_of_infected_people = len(infected_people_for_certain_if_close_contact)#getting size of array the infected people population
        print("the max that could be infected due to their %: (no changes, no edits, just flat number) ",size_of_infected_people)


        starting_with_person = random.choice(infected_people_for_certain_if_close_contact) # we will start with this person for this certain iteration
        print("We are starting with: ",starting_with_person)

        size_of_infected_people = size_of_infected_people - 1 #we can now exclude the person that is infected since we are initally working with them

        total_possibly_infected_without_startingPerson = N - 1 #we can now exclude the person that is infected for sure from total population


        recovery_of_starting_person = starting_with_person[2]
        if(recovery_of_starting_person<=0.35): #they did NOT recover and will have a chance to transmit to another person)

            activity_of_starting_person = starting_with_person[3]
            people_exposed = activity_of_starting_person*total_possibly_infected_without_startingPerson #calculating people exposed
            number_of_people_exposed_rounded = round(people_exposed) #gives us # of people exposed
            print("count of people exposed by this person: ",number_of_people_exposed_rounded)

            infection_rate_to_others_starting_person = starting_with_person[4]
            number_of_people_they_infected = infection_rate_to_others_starting_person*number_of_people_exposed_rounded #calculating number of people they infected
            number_of_people_they_infected_rounded = round(number_of_people_they_infected) #rounding to check #of exposures

            if(number_of_people_they_infected_rounded <= size_of_infected_people):
                print("count of people they did infect:", number_of_people_they_infected_rounded)
            else:
                print("count of people they did infect 100%", size_of_infected_people)

        else:
            print("person recovered and will not infect others :D")


problem_two.population(100)

