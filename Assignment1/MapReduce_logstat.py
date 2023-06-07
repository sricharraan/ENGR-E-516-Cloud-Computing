import Map_logstat
import Reduce_logstat
import os

#print("Hello")
##Map_logstat.map_logstat()
Map_logstat.map_logstat2()

Reduce_logstat.reduce_logstat()
os.remove("Mapper2.txt")