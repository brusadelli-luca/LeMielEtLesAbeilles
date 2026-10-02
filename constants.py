# Constants used by all files

NB_FLOWERS = 50                 # number of flowers visited in a route
NB_BEES = 100                   # number of bees in the hive
NB_PARENTS = NB_BEES // 2       # number of parents (the other half of the hive is replaced by their children)
HIVE = [500, 500]               # hive coordinates (start and end of every route)
ROUTE_LEN = NB_FLOWERS + 2      # hive + flowers + hive
