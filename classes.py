from functions import *
import random

# Bee class creation : 
class Bee():
    def __init__(self,field):
        self.route = [[500,500]] + random.sample(field,50) + [[500,500]]
        self.dist = self.dist_calc()


    # Calculates distance (= score) by chosen technique
    def dist_calc(self):
        dist = 0

        for i in range(51):
            dist = dist + manhattan(self.route[i],self.route[i+1])

        return dist


    # Replaces double coordinates (= genes) with missing coordinates
    def Repair(self):
        field = flower_coord_import('Champ de pissenlits et de sauge des pres')
        missing = []

        for flower in field:
            if not flower in self.route:
                missing.append(flower)
        
        for i_miss in range(len(missing)):
            for j1 in range(1,51):
                for j2 in range(1,51):
                    if (self.route[j1] == self.route[j2]) and (j1 != j2):
                        self.route[j1] = missing[i_miss]
        

    # Swaps two coordinates (= genes) in bee route
    def Mutation(self,rate=0):
        if random.random() < rate:
            k = random.sample(range(1, 51), 2)
            tmp = self.route[k[0]]
            self.route[k[0]] = self.route[k[1]]
            self.route[k[1]] = tmp
            

    # Checks if bee route (= chromosome) has correct structure
    def integrity(self, field):
              
        for flwr in field:
            if (not flwr in self.route) or ([500, 500] in self.route[1:51]):
                return False
        return True


# Hive class creation : 
    # bees = list of bees with fitness
    # method = selection method
    # sort_pop = population size if using sort selection method

class Hive():
    def __init__(self, field, method = 'sort', sort_pop = 50):
        self.field = field
        self.bees = []
        self.method = method
        self.sort_pop = sort_pop

        for i in range(100):
            self.bees.append(Bee(field))
        
        self.Selection()

    # Bee selection method : roulette / random / sort
    def Selection(self):
        if self.method == 'roulette':
            tmp_bees = []
            for k in range(100):
                rd = random.random()

                if rd < (1 - 3 * k / 100):
                    tmp_bees.append(self.bees[k])
            
            if len(tmp_bees) < 100:
                
                tmp_bees_2 = sorted(self.bees, key=lambda bee: bee.dist)
                
                for bee in tmp_bees_2:
                    if not bee in tmp_bees:
                        tmp_bees.append(bee)
        
            self.bees = tmp_bees

        elif self.method == 'random':

            self.bees = random.sample(self.bees[0:100], 100)

        else:
            # self.method == 'sort'
            tmp_bees = sorted(self.bees, key=lambda bee: bee.dist)
            self.bees = random.sample(tmp_bees[0:self.sort_pop], self.sort_pop) + tmp_bees[self.sort_pop:100]


    # Calculates average distance (= score) in hive
    def average_dist(self):
        hive_dist = 0
        for bee in self.bees:
            hive_dist = hive_dist + bee.dist
        
        return hive_dist/100

    # Checks if each bee route (= chromosome) in hive has correct structure
    def integrity(self):
        for bee in self.bees:
            if not bee.integrity(self.field):
                return False
        return True