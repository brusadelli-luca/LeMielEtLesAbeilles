# LeMielEtLesAbeilles
    * Algorithm class project.
    * Genetic algorithm used to determine shortest path of 50 points.
    * Bees are travelling from flower to flower.


## Instructions
    * Flower coordinates are given
    * arial.ttf is needed to generate routes viz
    * Set parameters list (see below). 
    * Run main.py
    
## Parameters
### Data set
   * field : Set coord data file

### Integrity test
   * integrity_test = Set True to perform routes integrity test (default = False)

### Img output
   * img_creation : Set True to create first and last generation routes viz
   * all_img : Set True to create all generation route viz

### Mutation
   * natural_rate : Set natural mutation rate (default = 0.000). Mutation will be run att each reproduction.
   * stagnation_rate : Set stagnation mutation rate. Mutation will be run only if evolution stagnates (see Stagnation definition).
   * var_mut : Set True to set a variable mutation rate (x 3 every 100 generation).

### Stagnation definition
   * stag_gen : Number of generations widht to be compared.
   * stagnation_def : Stagnation threshold (If performance evolution rate is lower, mutation is run).

### Selection
   * input_method : Set selection method (sort / roulette / random)
      * Random : Chooses 50 random individuals in population to create 50 new individuals
      * Sort : Chooses 50 random individuals between (N) best (see below)
      * Roulette : Chooses individuals randomly weighted by position in performance ranking. List completed to 50 individuals with S

   * sort_pop : Size of population used in Sort method to choose individuals (N)

### Comparison
   * param_list : Set parameter to be modified if comparision needed.
      Warning : variable parameter to be set in loop.
    

### Evolution
   * gen_nb : Number of generations in evolution
   * seq_len : Sequence lenght crossed in crossover


## Classes
### Bee class : 
    * chromosome = route
    * distance = 1 / fitness

### Hive class : 
    * bees = list of bees with fitness


## Necessary functions
    * Import flower coordinates
    * Manhattan distance evaluation
    * Euclidian distance evaluation
    * Single point crossover
    * Two points crossover


## Img generator
    * Creates flowers and routes img viz
