import csv
import random

from constants import NB_FLOWERS, ROUTE_LEN

# Necessary functions


# Import flower coord from given csv file
def flower_coord_import(file_name):

    with open(file_name + '.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        field = list(reader)

        field.remove(['x','y'])

        for i in range(len(field)):
            field[i][0] = int(field[i][0])
            field[i][1] = int(field[i][1])

    return field


# Calculate distance with mahattan definition
def manhattan(fl1,fl2):

    return abs(fl2[0] - fl1[0])+ abs(fl2[1] - fl1[1])


# Bee reproduction with single point crossover technique
def single_pt_crossover(parent1, parent2, child1, child2):
    
    k = random.randint(1, ROUTE_LEN - 1)

    child1.route = parent1.route[0:k] + parent2.route[k:ROUTE_LEN] 
    child2.route = parent2.route[0:k] + parent1.route[k:ROUTE_LEN]

    child1.repair()
    child2.repair()

    child1.dist = child1.dist_calc()
    child2.dist = child2.dist_calc()
    

# Bee reproduction with two point crossover technique    
def two_pts_crossover(parent1, parent2, child1, child2, lrg = 0):
    
    if lrg == 0:

        k = sorted(random.sample(range(2, NB_FLOWERS + 1), 2))
    
    else:
        k = []
        k.append(random.randint(2, ROUTE_LEN - 1))
        
        if k[0] > NB_FLOWERS // 2:
            k.append(max(1, k[0]-lrg))
        else:
            k.append(min(NB_FLOWERS, k[0]+lrg))

        k = sorted(k)

    child1.route = parent1.route[0:k[0]] + parent2.route[k[0]:k[1]] + parent1.route[k[1]:ROUTE_LEN] 
    child2.route = parent2.route[0:k[0]] + parent1.route[k[0]:k[1]] + parent2.route[k[1]:ROUTE_LEN]

    child1.repair()
    child2.repair()

    child1.dist = child1.dist_calc()
    child2.dist = child2.dist_calc()