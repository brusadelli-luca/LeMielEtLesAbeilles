from functions import *
from classes import *
from jpg_generator import *

import matplotlib.pyplot as plt
import time

start_time = time.time()

## Initialize

field = flower_coord_import('Champ de pissenlits et de sauge des pres')

# Integrity test
integrity_test = False

# Img output
img_creation = True

# Mutation
natural_rate = 0.000
stagnation_rate = 0.01
var_mut = False

# Stagnation definition
stag_gen = 5
stagnation_def = 0.05

# Selection
input_method = 'sort'
sort_pop = 80

# Comparison
param_list = [1] #,5,10]
graf_nb = 0

# Evolution
gen_nb = 500
seq_len = 35
evol=[]


# Loop on parameter if comparison requested

for param in param_list:
    graf_nb = graf_nb + 1
    
    hive1 = Hive(field, method=input_method, sort_pop=sort_pop)
    
    evol.append([])
    evol.append([])
    evol[graf_nb].append(hive1.average_dist())

    # First generation hive routes if ON
    if img_creation:
        # field = flower_coord_import('Champ de pissenlits et de sauge des pres')
        createJPG(field,hive1,'gen ' + str(0),freq_wdth=True)

    # Loop on generation number
    for i in range(1,gen_nb):
        for j in range(0,50,2):
            bee_P1 = hive1.bees[j]
            bee_P2 = hive1.bees[j+1]
            
            bee_D1 = hive1.bees[j+50]
            bee_S2 = hive1.bees[j+51]

            # Bee reproduction
            if seq_len == 0:
                single_pt_crossover(bee_P1, bee_P2, bee_D1, bee_S2)

            else:
                two_pts_crossover(bee_P1, bee_P2, bee_D1, bee_S2,lrg=seq_len)


            # If natural mutation ON
            if natural_rate !=0:
                bee_D1.Mutation(rate=natural_rate)
                bee_S2.Mutation(rate=natural_rate)

        # Bee selection in hive   
        hive1.Selection()

        # Integrity check if ON
        if integrity_test:
            if not hive1.integrity():
                print(hive1.integrity(),'generation',i)

        # Score record over generations
        evol[graf_nb].append(hive1.average_dist())
        evol[0].append(round((evol[graf_nb][i-1]-evol[graf_nb][i])/evol[graf_nb][i-1]*100,2))
                    
        # Last generation hive routes if ON
        if img_creation: # and i == gen_nb - 1:
            # field = flower_coord_import('Champ de pissenlits et de sauge des pres')
            createJPG(field,hive1,'gen ' + str(i),freq_wdth=True)
 
        # Mutation when evolution stagnates
        if i > stag_gen:

            if var_mut:
                if i == 100 or i == 200 or i == 300 :
                    stagnation_rate = stagnation_rate * 3

            if (evol[graf_nb][-stag_gen] - evol[graf_nb][-1])/evol[graf_nb][-stag_gen] < stagnation_def and \
                (evol[graf_nb][-stag_gen] - evol[graf_nb][-1]) >= 0:
                
                if stagnation_rate == 0:
                    print('stop at gen',i)
                    break

                # print('Mutation at generation',i)
                for bee in hive1.bees:
                    bee.Mutation(rate=stagnation_rate)

print('Execution time',round(time.time()-start_time,2),'s')

# Plotting evolution scores

gen = [*range(0,i+1,1)]

for i in range(0,len(param_list)):
    # + '\nSort pop size  : ' + str(sort_pop) \
    plt.plot(gen,evol[i+1],label= 'Sorting method : ' + input_method + '\nSort pop size  : ' + str(sort_pop) \
            + '\nCrossover seq len : ' + str(seq_len) \
            + '\nNatural mutation rate : ' + str(natural_rate) + '\nStag mutation rate : ' + str(stagnation_rate) \
            + '\nStag gen comp : ' + str(stag_gen) + '\nStag thresold  : ' + str(stagnation_def))
            

# print(evol[0])

plt.legend()
plt.title("Average distance evolution")
plt.xlabel("Generation")
plt.ylabel("Average distance")
plt.show()