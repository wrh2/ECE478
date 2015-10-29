from __future__ import division
import random

# python class for einstein
class Einstein:

    def slide(num):
        """
        This function takes in a slide number or interaction number
        it then determines what action einstein takes
        """

        # generate random int, convert to percentage
        chance = random.randint(1,10)/10

        # interaction 1.2 or slide 1.6
        if(num == 1.2 or num == 1.6):
            if(chance > self.niceness):
                return 'Einstein attacks, Newton keeps distance'
            else:
                return 'Newton attacks, Einstein keeps distance'

        # interaction 1.3 or slide 1.7
        if(num == 1.3 or num == 1.7):
            if(chance > self.niceness):
                return 'Einstein looks angrily at Bohr'
            else:
                return 'Einstein calmly smokes his pipe, while looking intently at Bohr'

        # slide 1.11
        if(num == 1.11):
            return 'Einstein grabs violin, points to Mary, then looks at Newton and Bohr'
    
    def mood(self):
        """
            Function returns string that represents mood
        """
        
        #random chance
        chance = random.randint(1,10) / 10
        
        # nicer, and chance > meanness
        if(self.niceness > self.meanness and  chance > self.meanness):
            return 'Einstein is groovy baby'
            
        # nicer, chance < meanness
        elif(self.niceness > self.meanness and chance < self.meanness):
            return 'Einstein is ok'
        
        # meaner, chance > meanness
        elif(self.niceness < self.meanness and chance > self.meanness):
            return 'Einstein is meh'
            
        # meaner, chance < meanness
        elif(self.niceness < self.meanness and chance < self.meanness):
            return 'Einstein says fuck off!'
    
    def personality(self):
        """
            Function returns personality traits for Einstein
        """
        return (self.niceness, self.meanness)
        
    def reaction(self, Action):
        """
            Function takes Action (integer 1 to 10)
            and generates a reaction from Einstein
            based on some probablistic bullshit I made up
        """
        
        # keep it within the proper range
        if(Action > 10 or Action < 0):
            Action = random.randint(1, 10)
            
        # initialize chance
        chance = 0
        
        # add up five random integers between 1-10
        for i in range(5):
            chance += random.randint(1,10)
            
        # divide by max (10, 5 times = 50)
        chance /= 50
        Action /= 50

        # initialize chance2
        chance2 = 0
        
        # this weighs the reaction towards a nice one or a mean one
        if(random.randint(1,10) <= 5):
            chance2 = self.niceness
        else:
            chance2 = self.meanness
        
        # get reaction
        if(chance*chance2 > Action):
            return 'Einstein reacted nicely'
        else:
            return 'Einstein reacted badly'
        
    def __init__(self, niceness, meanness):
        """
            Initialization of Einstein
        """
        
        # need to make sure we get reasonable numbers for niceness and meanness
        if(niceness < 0 and meanness < 0 or niceness == meanness):
            
            # niceness and meanness were both less than 0 which doesn't make sense
            # or they were equal to each other which also doesn't make sense
            
            # choose random number between 1 & 10 then divide by 10 for both
            # this gives us a percentage of this quality
            self.niceness = random.randint(1,10) / 10
            self.meanness = random.randint(1,10) / 10
            
            # need to make sure those numbers aren't equal to each other
            while(self.niceness == self.meanness):
                # they were so pick a new one 
                meanness = random.randint(1,10) / 10
                
        # max is 10, min is 0
        # convert into percentage
        if(niceness > 10):
            self.niceness = 1
        elif(niceness < 0):
            self.niceness = 0
        else:
            self.niceness = niceness / 10
        if(meanness > 10):
            self.meanness = 1
        elif(meanness < 0):
            self.meanness = 0
        else:
            self.meanness = meanness / 10

# this is some other stuff for reading text files that we will probably use later            
#with open("fname.text", "r") as f:
#    content = [x.strip('\n') for x in f.readlines()]
#    for stuff in content:
#        print stuff
