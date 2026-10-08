from functions import flower_coord_import, single_pt_crossover, two_pts_crossover
from classes import Hive
from jpg_generator import create_jpg
from constants import NB_PARENTS

import matplotlib.pyplot as plt
import time

start_time = time.time()

## Initialize

field = flower_coord_import('Champ de pissenlits et de sauge des pres')

# Integrity test
integrity_test = False

# Img output
img_creation = True
all_img = False

# Mutation
natural_rate = 0.000
stagnation_rate = 0.1
var_mut = False

# Stagnation definition
stag_gen = 5
stagnation_def = 0.05

# Selection
input_method = 'sort'
sort_pop = 80

# Evolution
gen_nb = 5000
seq_len = 35

hive1 = Hive(field, method=input_method, sort_pop=sort_pop)

# Average distance of the hive at each generation
evol = [hive1.average_dist()]

# First generation hive routes if ON
if img_creation:
    create_jpg(field,hive1,'gen ' + str(0),freq_wdth=True)

# Loop on generation number
for i in range(1,gen_nb):
    for j in range(0,NB_PARENTS,2):
        parent1 = hive1.bees[j]
        parent2 = hive1.bees[j+1]
        
        child1 = hive1.bees[j+NB_PARENTS]
        child2 = hive1.bees[j+NB_PARENTS+1]

        # Bee reproduction
        if seq_len == 0:
            single_pt_crossover(parent1, parent2, child1, child2)

        else:
            two_pts_crossover(parent1, parent2, child1, child2,lrg=seq_len)


        # If natural mutation ON
        if natural_rate !=0:
            child1.mutation(rate=natural_rate)
            child2.mutation(rate=natural_rate)

    # Bee selection in hive   
    hive1.selection()

    # Integrity check if ON
    if integrity_test:
        if not hive1.integrity():
            print(hive1.integrity(),'generation',i)

    # Score record over generations
    evol.append(hive1.average_dist())
                
    # Last generation hive routes if ON
    if img_creation and (all_img or i == gen_nb - 1):
        create_jpg(field,hive1,'gen ' + str(i),freq_wdth=True)
 
    # Mutation when evolution stagnates
    if i > stag_gen:

        if var_mut:
            if i == 100 or i == 200 or i == 300 :
                stagnation_rate = stagnation_rate * 3

        if (evol[-stag_gen] - evol[-1])/evol[-stag_gen] < stagnation_def and \
            (evol[-stag_gen] - evol[-1]) >= 0:
            
            if stagnation_rate == 0:
                print('stop at gen',i)
                break

            for bee in hive1.bees:
                bee.mutation(rate=stagnation_rate)


print('\nSelection method : ' + input_method + '\nSort population size  : ' + str(sort_pop) \
            + '\nCrossover sequence lenght : ' + str(seq_len) \
            + '\nNatural mutation rate : ' + str(natural_rate) + '\nStagnation mutation rate : ' + str(stagnation_rate) \
            + '\nVariable mutation rate : ' + str(var_mut) \
            + '\nStagnation generation comparison : ' + str(stag_gen) + '\nStagnation thresold  : ' + str(stagnation_def))

print('\nFirst generation mean score : '+ str(evol[0]) + '\nLast generation mean score : ' + str(evol[-1]))

print('\nExecution time',round(time.time()-start_time,2),'s\n')

# Plotting evolution scores

plt.plot(range(len(evol)),evol,label= 'Select method : ' + input_method + '\nSort pop size  : ' + str(sort_pop) \
        + '\nCrossover seq len : ' + str(seq_len) \
        + '\nNatural mutation rate : ' + str(natural_rate) + '\nStag mutation rate : ' + str(stagnation_rate) \
        + '\nVariable mutation rate : ' + str(var_mut) \
        + '\nStag gen comp : ' + str(stag_gen) + '\nStag thresold  : ' + str(stagnation_def))

plt.legend()
plt.title("Average distance evolution")
plt.xlabel("Generation")
plt.ylabel("Average distance")
plt.show()