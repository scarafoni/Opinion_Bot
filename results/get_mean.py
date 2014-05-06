#!/usr/bin/python
import numpy
import sys
lines = [line.strip() for line in open(sys.argv[1])] 
with open(sys.argv[2],'w') as fw:
    fw.write('n,mean,std')
    for line in lines:
        line = line.split(',')
        if(len(line) < 2): continue
        line = [float(x) for x in line]
        fw.write(str(len(line))+','+str(numpy.mean(line))+','+str(numpy.std(line))+'\n')
    fw.close()
        
