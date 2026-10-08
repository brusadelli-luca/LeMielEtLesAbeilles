# LeMielEtLesAbeilles
* Algorithm class project.
* Genetic algorithm used to determine shortest path of 50 points.
* Bees are travelling from flower to flower.
* Every route starts and ends at the hive (coordinates 500, 500) and visits the 50 flowers once.


## Requirements
* Python 3
* Pillow and matplotlib :

```
python -m pip install pillow matplotlib
```

* arial.ttf is needed to generate routes viz (already available on Windows, otherwise copy an arial.ttf file in the project folder)
* Flower coordinates file : `Champ de pissenlits et de sauge des pres.csv` (columns x,y, one flower per line, 50 flowers). The file name is set in main.py.


## Instructions
* Flower coordinates are given
* Set parameters in main.py (see below).
* Run main.py :

```
python main.py
```

* Close the graph window at the end to stop the program.


## Output
* Console : parameters used, first and last generation mean score, execution time.
* Window : evolution of the average distance over generations.
* Images (if img_creation = True) : `gen 0.jpg` (first generation) and the last generation (for example `gen 4999.jpg`). With all_img = True, one image per generation.


## Files
* main.py : parameters and evolution loop
* classes.py : Bee and Hive classes
* functions.py : flower coordinates import, distance, crossovers
* jpg_generator.py : routes viz
* constants.py : number of flowers, number of bees, hive coordinates...


## Parameters
### Data set
* field : Set coord data file

### Integrity test
* integrity_test = Set True to perform routes integrity test (default = False)

### Img output
* img_creation : Set True to create first and last generation routes viz (default = True)
* all_img : Set True to create all generation route viz (default = False)

### Mutation
* natural_rate : Set natural mutation rate (default = 0.000). Mutation will be run at each reproduction.
* stagnation_rate : Set stagnation mutation rate (default = 0.1). Mutation will be run only if evolution stagnates (see Stagnation definition). If set to 0, evolution stops when it stagnates.
* var_mut : Set True to set a variable mutation rate (x 3 at generations 100, 200 and 300). Default = False

### Stagnation definition
* stag_gen : Number of generations width to be compared (default = 5).
* stagnation_def : Stagnation threshold (If performance evolution rate is lower, mutation is run). Default = 0.05

### Selection
* input_method : Set selection method (sort / roulette / random). Default = sort
  * Random : Chooses 50 random individuals in population to create 50 new individuals
  * Sort : Chooses 50 random individuals between (N) best (see below)
  * Roulette : Chooses individuals randomly weighted by position in performance ranking. List is completed to 50 individuals with the remaining bees, sorted by performance.

* sort_pop : Size of population used in Sort method to choose individuals (N). Default = 80

### Evolution
* gen_nb : Number of generations in evolution (default = 5000)
* seq_len : Sequence length crossed in crossover (default = 35). If set to 0, single point crossover is used, otherwise two points crossover.


## Classes
### Bee class :
* route = chromosome (hive, 50 flowers, hive)
* dist = length of the route (Manhattan distance), the lower the better
* repair : replaces double flowers (= genes) with missing flowers after a crossover
* mutation : swaps two flowers in the route

### Hive class :
* bees = list of 100 bees with their distance
* selection : bee selection (sort / roulette / random)
* average_dist : average distance of the hive
* integrity : checks that all routes are correct


## Necessary functions
* Import flower coordinates
* Manhattan distance evaluation
* Single point crossover
* Two points crossover


## Img generator
* Creates flowers and routes img viz
* Hive in brown, flowers in yellow, routes in black (line width increases with the number of bees using the same path), generation number at the top right.


## Known limits
* Distance is evaluated with Manhattan definition, but routes are drawn as straight lines.
* The image size is 3000 x 3000 px : creating an image for every generation (all_img) is slow and takes a lot of disk space.
