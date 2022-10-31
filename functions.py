import csv
import math
import random

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


# Calculate distance with euclidian definition
def euclidian(fl1,fl2):

    return math.sqrt((fl2[0] - fl1[0]) **2 + (fl2[1] - fl1[1]) **2)


# Calculate distance with mahattan definition
def manhattan(fl1,fl2):

    return abs(fl2[0] - fl1[0])+ abs(fl2[1] - fl1[1])


# Bee reproduction with single point crossover technique
def single_pt_crossover(bee_P1, bee_P2, bee_D1, bee_S2):
    
    k = random.randint(1, 51)

    bee_D1.route = bee_P1.route[0:k] + bee_P2.route[k:53] 
    bee_S2.route = bee_P2.route[0:k] + bee_P1.route[k:53]

    bee_D1.Repair()
    bee_S2.Repair()

    bee_D1.dist = bee_D1.dist_calc()
    bee_S2.dist = bee_S2.dist_calc()
    

# Bee reproduction with two point crossover technique    
def two_pts_crossover(bee_P1, bee_P2, bee_D1, bee_S2, lrg = 0):
    
    if lrg == 0:

        k = sorted(random.sample(range(2, 51), 2))
    
    else:
        k = []
        k.append(random.randint(2, 51))
        
        if k[0] >= 26:
            k.append(max(1, k[0]-lrg))
        else:
            k.append(min(50, k[0]+lrg))

        k = sorted(k)

    bee_D1.route = bee_P1.route[0:k[0]] + bee_P2.route[k[0]:k[1]] + bee_P1.route[k[1]:52] 
    bee_S2.route = bee_P2.route[0:k[0]] + bee_P1.route[k[0]:k[1]] + bee_P2.route[k[1]:52]

    bee_D1.Repair()
    bee_S2.Repair()

    bee_D1.dist = bee_D1.dist_calc()
    bee_S2.dist = bee_S2.dist_calc()


# Bee reproduction with other two point crossover technique    
def two_pts_crossover_bis(bee_P1, bee_P2, bee_D1, bee_S2, lrg = 0):
    
    if lrg == 0:

        k = sorted(random.sample(range(2, 51), 2))
    
    else:
        k = []
        k.append(random.randint(2, 51))
        
        if k[0] >= 26:
            k.append(max(1, k[0]-lrg))
        else:
            k.append(min(50, k[0]+lrg))

        k = sorted(k)

    tmp1 = []
    tmp2 = []

    for i in range(k[0]):
        tmp1.append([500, 500])
    
    for i in range(k[1],53):
        tmp2.append([500, 500])

    bee_D1.route = tmp1 + bee_P2.route[k[0]:k[1]] + tmp2 
    bee_S2.route = tmp1 + bee_P1.route[k[0]:k[1]] + tmp2

    bee_D1.Repair()
    bee_S2.Repair()

    bee_D1.dist = bee_D1.dist_calc()
    bee_S2.dist = bee_S2.dist_calc()